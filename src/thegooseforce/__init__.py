"""TheGooseForce CLI Entry Point"""
import argparse
from .server import run_mcp_server

def main():
    """TheGooseForce: Salesforce integration for Goose."""
    parser = argparse.ArgumentParser(
        description="Salesforce integration for GooseForce CLI"
    )
    parser.parse_args()  # ✅ Fixed parsing issue
    run_mcp_server()  # ✅ Calls the correct function to start the MCP server

if __name__ == "__main__":
    main()
