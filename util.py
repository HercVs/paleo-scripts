import pandas as pd


def load_from_csv(filepath, header=0, index=0):
    return pd.read_csv(filepath, header=header, index_col=index)


def to_percentages(dataframe):
    return dataframe.div(dataframe.sum(axis=1), axis=0) * 100