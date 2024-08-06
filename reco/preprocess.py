# reco/preprocess.py

import pandas as pd


def preprocess_data(data):
    """
    Preprocess the user interaction data.

    :param data: DataFrame containing user interaction data
    :return: Preprocessed DataFrame
    """
    # Example preprocessing steps
    data = data.dropna()  # Drop missing values
    data['interaction_time'] = pd.to_datetime(
        data['interaction_time'])  # Convert time to datetime
    return data
