import pandas as pd


def read_csv(file):

    df = pd.read_csv(file, header=None)

    return df.to_string(index=False, header=False)
