from dotenv import load_dotenv
import os

load_dotenv()

CUBESANDBOX_URL = os.getenv(
    "CUBESANDBOX_URL",
    "http://127.0.0.1:13000"
)