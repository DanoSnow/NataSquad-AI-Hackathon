from src.components import get_dataset
from src.components.rfm import rfm_score_features
from src.model.preprocessing import rfm_input
from src.model.k_means import predict
import matplotlib.pyplot as plt
import seaborn as sns

ds = get_dataset()
scored = rfm_score_features(ds)
input = rfm_input(scored)
customers = predict(input, scored)

_, axes = plt.subplots(2,2)
for i, score in enumerate(customers.columns[4:8]):
    sns.swarmplot(data=customers, x='Labels', y=score, ax=axes[i//2][i%2],
                  hue='Labels', palette=sns.color_palette('hls',4))
    ax=axes[i//2][i%2].set_title(f'Labels According to {score}')
plt.show()
