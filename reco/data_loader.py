# reco/data_loader.py

import pandas as pd


def load_data(file_path):
    """
    Load user interaction data from a CSV file.

    :param file_path: Path to the CSV file
    :return: DataFrame containing user interaction data
    """
    data = pd.read_csv(file_path)
    return data
