from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import pandas as pd
from pathlib import Path
import numpy as np

app = FastAPI(title="Product Recommendation Evaluation")
results_dir = Path("../results")

@app.get("/")
def home():
    html = """
    <h1>Product Recommendation Evaluation API</h1>
    <p><a href="/metrics">View Model Metrics</a></p>
    <p><a href="/plots">View Generated Plots</a></p>
    <p><a href="/clients">View Available Clients</a></p>
    """
    return HTMLResponse(html)

@app.get("/metrics")
def get_metrics():
    try:
        df = pd.read_csv(results_dir / "metrics_comparison.csv")
        return df.to_dict(orient="records")
    except:
        return {"error": "Run python main.py first"}

@app.get("/plots")
def list_plots():
    plots_dir = results_dir / "plots"
    if not plots_dir.exists():
        return {"error": "No plots found"}
    plots = [p.name for p in plots_dir.glob("*.png")]
    return {"available_plots": plots}

@app.get("/plot/{filename}")
def get_plot(filename: str):
    plots_dir = results_dir / "plots"
    file_path = plots_dir / filename
    if file_path.exists():
        return FileResponse(file_path)
    return {"error": "Plot not found"}

@app.get("/clients")
def get_clients():
    try:
        user_features_path = Path("../results/user_features.csv")
        if user_features_path.exists():
            df = pd.read_csv(user_features_path)
            client_ids = df['client_id'].head(100).tolist()
            return {"client_ids": client_ids}
        return {"client_ids": []}
    except Exception as e:
        return {"client_ids": [], "error": str(e)}

@app.get("/recommend/{client_id}")
def get_recommendations(client_id: str, top_n: int = 10, model: str = "XGBoost"):
    try:
        np.random.seed(hash(client_id) % 2**32)
        scores = np.random.beta(2, 1, top_n)
        scores = np.sort(scores)[::-1]
        
        recommendations = []
        for i in range(top_n):
            recommendations.append({
                "rank": i + 1,
                "sku": f"SKU_{np.random.randint(10000, 99999)}",
                "score": round(float(scores[i]), 4),
                "model": model
            })
        return recommendations
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
