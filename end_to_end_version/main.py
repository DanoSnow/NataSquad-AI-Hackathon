from src.components import get_dataset
from src.components.rfm import rfm_score_features
from src.model.preprocessing import rfm_input
from src.model.k_means import predict
import src.components.graphics as gr

ds = get_dataset()
scored = rfm_score_features(ds)
inputs = rfm_input(scored)
customers = predict(inputs, scored)

gr.categorical_plot(customers, 'both')

