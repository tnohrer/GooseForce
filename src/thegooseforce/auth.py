import os
from dotenv import load_dotenv
from simple_salesforce import Salesforce

load_dotenv()  # Load environment variables from .env file

def get_salesforce_client():
    """Establishes a connection to Salesforce"""
    try:
        sf = Salesforce(
            username=os.getenv("SALESFORCE_USERNAME"),
            password=os.getenv("SALESFORCE_PASSWORD"),
            security_token=os.getenv("SALESFORCE_SECURITY_TOKEN"),
        )
        return sf
    except Exception as e:
        print(f"Error connecting to Salesforce: {e}")
        return None
