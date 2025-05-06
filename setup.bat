call pip install virtualenv
call python -m venv .venv
call .\\.venv\\Scripts\\activate
call pip install -r requirements.txt
start cmd /k "call .\\.venv\\Scripts\\activate && python launch.py"
timeout /t 10 /nobreak
call py base_client.py
:: Wait for 20 seconds
timeout /t 20 /nobreak
:: Kill the FastAPI server (finds uvicorn or python process and kills it)
for /f "tokens=5" %%i in ('netstat -aon ^| findstr :80') do taskkill /f /pid %%i
echo "Done Setup"
pause