from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
from pathlib import Path

app = FastAPI(title="Product Recommendation Evaluation")

results_dir = Path("results")

@app.get("/")
def home():
    html = """
    <h1>AI Product Recommendation Evaluation</h1>
    <p><a href="/metrics">View Model Metrics</a></p>
    <p><a href="/plots">View Generated Plots</a></p>
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
        return {"error": "No plots found. Run python main.py first."}
    plots = [p.name for p in plots_dir.glob("*.png")]
    return {"available_plots": plots}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
