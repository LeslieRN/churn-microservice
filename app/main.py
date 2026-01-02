from fastapi import FastAPI, HTTPException
from app.schemas import ChurnInput
from app.model import model_service
import pandas as pd

app = FastAPI(
    title="Netflix Churn Prediction API",
    version="1.0.0"
)

CSV_PATH = "clientes_limpio.csv"

def load_csv():
    return pd.read_csv(CSV_PATH)

@app.get("/item/{item_id}")
def get_item(item_id: str):
    df = load_csv()

    # Filtrando por public id (string comparison)
    result = df[df["public_id"] == item_id]

    if result.empty:
        raise HTTPException(
            status_code=404,
            detail=f"Información con id '{item_id}' no fue encontrado"
        )

    # Convertir csv a JSON-dict
    row_dict = result.to_dict(orient="records")[0]

    return {"status": "success", "data": row_dict}


@app.get("/items")
def get_all_items():
    df = load_csv()
    return {
        "status": "success",
        "total": len(df),
        "data": df.to_dict(orient="records")
    }


@app.post("/predict")
def predict(data: ChurnInput):
    try:
        df = pd.DataFrame([data.dict()])
        result = model_service.predict(df)

        return result
    
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))