from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

db_url = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

def connect_to_db():
    return create_engine(db_url,connect_args={'connect_timeout': 60})