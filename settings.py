import os
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

SESAME_AUTH_TOKEN = os.getenv('SESAME_AUTH_TOKEN')
SESAME_DEVICE_ID = os.getenv('SESAME_DEVICE_ID')
INTERVAL_SEC = os.getenv('INTERVAL_SEC')
GPIO_PIN = os.getenv('GPIO_PIN')
