import subprocess
import pandas as pd

from constant import *
from src.file_reader import FileReader


def __construct_question(row, skip_main_question: bool) -> str:
    main_question = ''
    if not pd.isna(row['question content']) and skip_main_question is False:
        main_question += row['question content']

    subsection: str = '\n'
    if not pd.isna(row['subsection id']):
        subsection += '(' + subsection + ') '

    return main_question + subsection + row['question']


def __generate_question_dict(df):
    question_dict: dict = {}
    for index, row in df.iterrows():

        if row['id'] not in question_dict:
            question_dict[row['id']] = [__construct_question(row, False)]
        else:
            question_dict[row['id']].append(__construct_question(row, True))

    return question_dict


def generate_shared_context():
    file_reader = FileReader()
    sheets = file_reader.get_sheet_names(output_file_xlsx)

    for sheet in sheets:

        df = file_reader.read_xlsx(output_file_xlsx, sheet)
        question_dict = __generate_question_dict(df)

        for index, row in df.iterrows():
            if not pd.isna(df.iloc[index][shared_context_answer_col]):
                continue
            print('Shared context', 'Running query on:\n', sheet, row['id'], row['subsection id'])

            questions: list = question_dict[row['id']]
            command = ["python3", "shared_context_api.py"]
            command.extend(questions)

            data = subprocess.run(command, capture_output=True)
            responses = data.stdout.decode().split(response_separator)[:-1]

            for idx, response in enumerate(responses):
                df._set_value(index + idx, shared_context_answer_col, response)

            print('Shared context', 'Finished:\n', sheet, row['id'], row['subsection id'])
            file_reader.replace_sheet(output_file_xlsx, sheet, df)

        print('Shared context', "Sheet", sheet, "completed.")


def generate_separate_context():
    file_reader = FileReader()
    sheets = file_reader.get_sheet_names(output_file_xlsx)

    for sheet in sheets:
        df = file_reader.read_xlsx(output_file_xlsx, sheet)

        for index, row in df.iterrows():
            if not pd.isna(df.iloc[index][separate_context_answer_col]):
                continue
            print('Separate context', 'Running query on:\n', sheet, row['id'], row['subsection id'])

            question = __construct_question(row, False)
            command = ["python3", "separate_context_api.py", question]

            data = subprocess.run(command, capture_output=True)
            response = data.stdout.decode().strip()
            df._set_value(index, separate_context_answer_col, response)

            print('Separate context', 'Finished:\n', sheet, row['id'], row['subsection id'])
            print(df[separate_context_answer_col])
            file_reader.replace_sheet(output_file_xlsx, sheet, df)

        print('Separate context:', "Sheet", sheet, "completed.")
