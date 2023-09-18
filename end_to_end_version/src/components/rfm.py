#----------------------------------------------------------------------
#-------------------------Features Engineering-------------------------
#----------------------------------------------------------------------
# Módulo encargado de realizar el análisis rfm a partir del fichero "sales_data_sample.csv"

from pandas import DataFrame, to_datetime
from datetime import timedelta
from pandas import read_csv, DataFrame, qcut

def get_dataset()->DataFrame:
    return read_csv("../../../sales_data_sample.csv", encoding='ISO-8859-1')

def rfm_features(dataset:DataFrame)->DataFrame:
    '''
    Función que recibe el fichero "sales_data_sample.csv" en forma de DataFrame y retorna un DataFrame con el análisis RFM.

    :param dataset: DataFrame
    :return: DataFrame
    '''
    dataset["ORDERDATE"] = to_datetime(dataset["ORDERDATE"])
    current_date = dataset["ORDERDATE"].max() + timedelta(days=1)
    recency = dataset.groupby("CUSTOMERNAME")["ORDERDATE"].apply(lambda x: (current_date-x.max()).days)
    frecuency = dataset.groupby("CUSTOMERNAME")["ORDERNUMBER"].count()
    monetary_value = dataset.groupby(["CUSTOMERNAME"])["SALES"].sum()

    data = {
        "Customer name": recency.index,
        "Recency": recency.values,
        "Frecuency": frecuency.values,
        "Monetary value": monetary_value.values
    }
    return DataFrame(data)

def rfm_score_features(dataset:DataFrame)->DataFrame:
    '''
    Función que recibe el fichero "sales_data_sample.csv" en forma de DataFrame y retorna un DataFrame con el análisis RFM con valores y escala de valores 1-5.

    :param dataset: DataFrame
    :return: DataFrame
    '''
    rfm = rfm_features(dataset)
    r = qcut(rfm["Recency"], q=5, labels=range(5, 0, -1))
    f = qcut(rfm["Frecuency"], q=5, labels=range(1, 6))
    m = qcut(rfm["Monetary value"], q=5, labels=range(1, 6))
    rfm = rfm.assign(R_score=r, F_score=f, M_score=m)

    rfm["R_score"] = rfm["R_score"].astype(int)
    rfm["F_score"] = rfm["F_score"].astype(int)
    rfm["M_score"] = rfm["M_score"].astype(int)
    rfm["RFM_score"] = rfm["R_score"] + rfm["F_score"] + rfm["M_score"]
    return rfm
    pass
