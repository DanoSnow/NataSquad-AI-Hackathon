#---------------------------------------------------------------------
#-----------------------------Main program----------------------------
#---------------------------------------------------------------------
#---------------------------------API---------------------------------
#---------------------------------------------------------------------

from src.components import get_dataset
from src.components.rfm import rfm_score_features
from src.model.preprocessing import rfm_input
from src.model.k_means import predict
import src.components.graphics as gr
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse
from schemas.models import Sale

ds = get_dataset()
scored = rfm_score_features(ds)
inputs = rfm_input(scored)
customers = predict(inputs, scored)

app = FastAPI(
    title="Customer segmentation",
    description="Customer segmentation end to end version",
    version="0.1.1"
)

@app.get('/')
async def root():
    return "Customer segmentation: End to end"

@app.get('/plot')
async def plot(kind:str='swarm'):
    try:
        gr.categorical_plot(customers, kind)
        categorical_plot_path = "src/output/categorical.png"
        return FileResponse(categorical_plot_path, media_type="image/png")
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e.args[0]))

@app.post('/newsale')
async def new_sale(sale: Sale):
    return sale