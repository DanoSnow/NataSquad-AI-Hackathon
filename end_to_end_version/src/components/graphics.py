#----------------------------------------------------------------------
#----------------------------Visualization-----------------------------
#----------------------------------------------------------------------
# Módulo encargado de realizar las visualizaciones de los datos

import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame
import os

def categorical_plot(clustered_dataset:DataFrame, plot_type:str='swarm'):
    '''
    Función que recibe el dataset segmentado para visualizar en el eje categórico los datos.

    :param clustered_rfm: DataFrame
    :param plot_type: str=['swarm', 'violin', 'both']
    :return: None
    '''
    if plot_type == 'swarm':
        sns.swarmplot(data=clustered_dataset, x='Labels', y='RFM_score',
                      hue='Labels', palette=sns.color_palette('hls', 4),
                      dodge=False, legend=False, s=3)
    elif plot_type == 'violin':
        sns.violinplot(data=clustered_dataset, x='Labels', y='RFM_score',
                       hue='Labels', palette=sns.color_palette('hls', 4),
                       dodge=False)
    elif plot_type == 'both':
        sns.catplot(data=clustered_dataset, x='Labels', y='RFM_score',
                    kind="violin", color=".9", inner=None)
        sns.swarmplot(data=clustered_dataset, x='Labels', y='RFM_score',
                      hue='Labels', palette=sns.color_palette('hls', 4),
                      size=3)
        plt.ylim(2,16)
    else:
        raise ValueError("Invalid plot type. Allowed values are 'swarm', 'violin', or 'both'.")

    fig_path = os.path.join('src/output/','categorical.png')
    plt.savefig(fig_path)
    plt.clf()
