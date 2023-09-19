#---------------------------------------------------------------------
#----------------------------Preprocessing----------------------------
#---------------------------------------------------------------------
# Módulo encargado de realizar el preprocesamiento del análisis rfm
# Se realiza la estandarización de los datos para que tengan media de
# valor 0 y desviación estándar de valor 1. Tiene la utilida de centrar
# los datos y eliminar la influencia de la escala y la varianza de los
# valores.

from sklearn.preprocessing import StandardScaler
from pandas import DataFrame

def rfm_scale(rfm_scored_dataset:DataFrame)->DataFrame:
    '''
    Función que recibe el DataFrame con el análisis RFM, y retorna un DataFrame con los valores RFM estandarizados.

    :param rfm_scored_dataset: DataFrame
    :return: DataFrame
    '''
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_scored_dataset[rfm_scored_dataset.columns[1:4].values])
    return DataFrame(rfm_scaled, columns=rfm_scored_dataset.columns[1:4].values)

def rfm_input(rfm_scored_dataset:DataFrame)->DataFrame:
    '''
    Función que recibe el DataFrame con el análisis RFM, y retorna un DataFrame con los valores RFM estandarizados y los puntajes como datos de entrada del modelo K-Means.

    :param rfm_scored_dataset: DataFrame
    :return: DataFrame
    '''
    rfm_scaled = rfm_scale(rfm_scored_dataset)
    rfm_scaled = rfm_scaled.assign(R_score=rfm_scored_dataset["R_score"],
                                   F_score=rfm_scored_dataset["F_score"],
                                   M_score=rfm_scored_dataset["M_score"],
                                   RFM_score=rfm_scored_dataset["RFM_score"])
    return rfm_scaled
    pass