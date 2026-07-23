import pandas as pd


def read_excel(file):

    df = pd.read_excel(file, header=None)

    return df.to_string(index=False, header=False)
