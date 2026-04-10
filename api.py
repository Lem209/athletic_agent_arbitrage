from fastapi import FastAPI
import subprocess
import json

app = FastAPI()

@app.get("/run-scan")
def run_scan():
    subprocess.run(["py", "run_scan.py"], check=True)
    return {"status": "Scan completed"}

@app.get("/opportunities")
def get_opportunities():
    with open("outputs/latest_opportunities.json") as f:
        return json.load(f)

@app.get("/summary")
def get_summary():
    with open("outputs/latest_summary.json") as f:
        return json.load(f)