
import os

BASE_URL = os.getenv(
    "BASE_URL",
    "http://127.0.0.1:5000"
)

HEADLESS = os.getenv(
    "HEADLESS",
    "false"
).lower() == "true"

WAIT_TIME = 10
