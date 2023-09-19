from pandas import DataFrame, read_csv

def get_dataset()->DataFrame:
    return read_csv("../sales_data_sample.csv", encoding='ISO-8859-1')