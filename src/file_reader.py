import os

import pandas as pd


class FileReader:
    base_folder_path = None
    dataset_path = None

    def __init__(self):
        self.base_folder_path = os.getcwd().split(os.sep + 'src')[0]
        self.dataset_path = os.path.join(self.base_folder_path, 'dataset')
        print("Dataset Path: " + self.dataset_path)

    def read_xlsx(self, file_name, sheet_name) -> pd.DataFrame:
        return pd.read_excel(os.path.join(self.dataset_path, file_name), sheet_name)

    def get_sheet_names(self, file_name):
        x1 = pd.ExcelFile(os.path.join(self.dataset_path, file_name))
        return x1.sheet_names

    def replace_sheet(self, file_name, sheet, df: pd.DataFrame):

        with pd.ExcelWriter(os.path.join(self.dataset_path, file_name), engine="openpyxl", mode="a",
                            if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheet_name=sheet, index=False)