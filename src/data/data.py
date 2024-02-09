import pandas as pd

class Data:
    def __init__(self) -> None:
        pass

    def load_data(self, path_to_file: str) -> pd.DataFrame:
        pass

    def clean_data(self, raw_data: pd.DataFrame) -> pd.DataFrame:
        pass

    def generate_features(self, processed_data: pd.DataFrame) -> pd.DataFrame:
        pass

    def process(self, path_to_file: str) -> pd.DataFrame:
        pass
