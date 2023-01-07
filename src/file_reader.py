import os

import pandas as pd


class FileReader:
    base_folder_path = None
    dataset_path = None

    def __init__(self):
        self.base_folder_path = os.getcwd().split(os.sep + 'src')[0]
        self.dataset_path = os.path.join(self.base_folder_path, 'dataset')
        print("Dataset Path: " + self.dataset_path)

    def read_xlsx(self, file_name) -> pd.DataFrame:
        return pd.read_excel(os.path.join(self.dataset_path, file_name))
