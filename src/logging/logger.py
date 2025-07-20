import logging
import os
from datetime import datetime

# Create "logs" directory if it doesn't exist
# logs_path=os.path.join(os.getcwd(), "logs",LOG_FILE)
# os.makedirs(logs_path,exist_ok=True)

logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir,exist_ok=True)

# Timestamped log file inside logs
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)
LOG_PATH = os.path.join(logs_dir,LOG_FILE)

# Set up logging 
logging.basicConfig(
    filename=LOG_PATH,
    format="[ %(asctime)s]  %(lineno)d %(name)s - %(levelname)s - %(message)s ",
    level = logging.INFO
)

## new code
logger = logging.getLogger(__name__)
