import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent / '.env'

load_dotenv(dotenv_path=env_path)

class Config:
    WEATHER_API_URL = os.environ.get('WEATHER_API_URL')