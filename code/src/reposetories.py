import json
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / 'data.json'
TTL_SECONDS = 3600


def is_cache_alive() -> bool:
    if not FILE_PATH.exists() or FILE_PATH.stat().st_size == 0:
        return False

    file_mod_time = FILE_PATH.stat().st_mtime
    if (time.time() - file_mod_time) > TTL_SECONDS:
        FILE_PATH.unlink()  
        return False

    return True

def to_cache(obj: json):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(obj, file, ensure_ascii=False, indent=4)
        
def get_cache():
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)