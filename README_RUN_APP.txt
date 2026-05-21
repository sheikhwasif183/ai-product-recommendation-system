AI Product Recommendation Studio - Streamlit Demo

How to run:

1. Open terminal inside this folder.
2. Setup VNVE

* Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
* py -3.11 -m venv venv
* .\venv\Scripts\activate

2. Install dependencies:

   pip install -r requirements.txt
pip install xgboost
pip install torch


3. Run Streamlit:
	python -m streamlit run dashboard.py
4. Run API
*cd api
* python main.py

  

Required files:
- streamlit_app.py
- outputs/metrics.csv
- outputs/demo_recommendations.csv
- outputs/user_profiles.csv
- outputs/confusion_matrices/

Important:
This demo uses pre-generated recommendation outputs.
It does not load the full Synerise dataset.
