from fastapi import FastAPI
import subprocess
import json
import os

app = FastAPI()

OUTPUTS_DIR = "outputs"
OPPORTUNITIES_FILE = os.path.join(OUTPUTS_DIR, "latest_opportunities.json")
SUMMARY_FILE = os.path.join(OUTPUTS_DIR, "latest_summary.json")

# Ensure the outputs directory exists
os.makedirs(OUTPUTS_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"message": "Athletic Agent Arbitrage API is running"}

@app.get("/run-scan")
def run_scan():
    subprocess.run(["python", "run_scan.py"], check=True)
    return {"status": "Scan completed"}

@app.get("/opportunities")
def get_opportunities():
    if not os.path.exists(OPPORTUNITIES_FILE):
        return {"message": "No opportunities found. Please run /run-scan first."}
    with open(OPPORTUNITIES_FILE) as f:
        return json.load(f)

@app.get("/summary")
def get_summary():
    if not os.path.exists(SUMMARY_FILE):
        return {"message": "No summary found. Please run /run-scan first."}
    with open(SUMMARY_FILE) as f:
        return json.load(f)
