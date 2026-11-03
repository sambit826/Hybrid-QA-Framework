
import os
from pathlib import Path

from dotenv import load_dotenv


# Locate the .env file in the project root
PROJECT_ROOT = Path(__file__).resolve().parent
ENV_FILE = PROJECT_ROOT / ".env"

# Load environment variables
load_dotenv(ENV_FILE)


# Application configuration
BASE_URL = os.getenv("BASE_URL")
SAUCEDEMO_USERNAME = os.getenv("SAUCEDEMO_USERNAME")
SAUCEDEMO_PASSWORD = os.getenv("SAUCEDEMO_PASSWORD")


# Validate required environment variables
required_variables = {
    "BASE_URL": BASE_URL,
    "SAUCEDEMO_USERNAME": SAUCEDEMO_USERNAME,
    "SAUCEDEMO_PASSWORD": SAUCEDEMO_PASSWORD,
}

missing_variables = [
    name for name, value in required_variables.items()
    if not value
]

if missing_variables:
    raise ValueError(
        f"Missing required environment variables: {', '.join(missing_variables)}"
    )
