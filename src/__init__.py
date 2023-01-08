import pandas as pd

import file_reader
from src.single_context_api import SingleContextAPI
import subprocess
from constant import *


def single_context(df, sheet):
    question_dict: dict = {}
    for index, row in df.iterrows():

        if row['id'] not in question_dict:
            question_dict[row['id']] = [row['question content'] + '\n(' + row['subsection id'] + ') ' + row['question']]
        else:
            question_dict[row['id']].append('\n(' + row['subsection id'] + ') ' + row['question'])

    for index, row in df.iterrows():
        if not pd.isna(df.iloc[index]['answer']):
            continue
        print('Running query on:\n', sheet, row['id'], row['subsection id'])

        questions: list = question_dict[row['id']]
        command = ["python3", "single_context_api.py"]
        command.extend(questions)

        data = subprocess.run(command, capture_output=True)
        print(data.stdout)
        responses = data.stdout.decode().split(response_separator)[:-1]

        for idx, response in enumerate(responses):
            df._set_value(index + idx, 'answer', response)

        print('Finished:\n', sheet, row['id'], row['subsection id'])
        print(df['answer'])

    return df


if __name__ == '__main__':
    file_reader = file_reader.FileReader()
    sheets = file_reader.get_sheet_names(output_file_xlsx)

    for sheet in sheets:
        df = file_reader.read_xlsx(output_file_xlsx, sheet)
        df = single_context(df, sheet)

        file_reader.replace_sheet(output_file_xlsx, sheet, df)
        print("Sheet", sheet, "completed.")
