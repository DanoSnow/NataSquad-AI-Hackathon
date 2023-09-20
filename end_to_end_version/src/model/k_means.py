#---------------------------------------------------------------------
#--------------------------------Model--------------------------------
#---------------------------------------------------------------------
# Módulo encargado de utilizar el modelo entrenado de la versión jupyter
# notebook para predecir los grupos a los que pertenecen los clientes

from pandas import DataFrame
import pickle

def predict(rfm_scaled_dataset:DataFrame,
            rfm_scored_dataset:DataFrame)->DataFrame:
    '''
    Función que recibe los DataFrame con el análisis RFM escalado estándar como dato de entrada del modelo de segmentación y el no escalado donde se van a almacenar las categorías/segmentos a los que pertenecen los clientes.

    :param rfm_scaled_dataset: DataFrame
    :param rfm_scored_dataset: DataFrame
    :return: DataFrame
    '''
    kmeans_model = pickle.load(open('src/model/model.pickle', 'rb'))
    labels = kmeans_model.predict(rfm_scaled_dataset)
    rfm_scored_dataset['Labels'] = labels
    return rfm_scored_dataset
