if (Test-Path .\venv) {
    Write-Host "Venv already exists. Skipping creation."
} else {
    python -m venv venv
}
.\venv\Scripts\activate
pip install -r .\tools\config\requirements.txt
python .\tools\selenoid_start.py