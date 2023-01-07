import file_reader
from src.single_context_api import SingleContextAPI


def single_context(df):
    question_dict: dict = {}
    for index, row in df.iterrows():

        if row['id'] not in question_dict:
            question_dict[row['id']] = [row['question content'] + '\n(' + row['subsection id'] + ') ' + row['question']]
        else:
            question_dict[row['id']].append('\n(' + row['subsection id'] + ') ' + row['question'])

    print(question_dict)
    for key in question_dict:
        questions: list = question_dict[key]

        single_context = SingleContextAPI()
        for question in questions:
            print(question)
            print(single_context.get_api_response(question))


if __name__ == '__main__':
    file_reader = file_reader.FileReader()
    df = file_reader.read_xlsx('testing.xlsx')

    single_context(df)
