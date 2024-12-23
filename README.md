# Virtual Environment
## Activate
1. Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.
2. Run `./venv/Scripts/activate`.

## Deactivate
Run `deactivate`.

# Packages
1. Run `pip install -r requirements.txt`

# Environment Variable
Get `.env` file from Jerri

# Running the application
1. Make sure `.env` file with the API token is in the directory.
2. Run `python ./runner.py <expected number of posts (default 10)>`