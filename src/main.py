import json

from config import GITHUB_API, LOG_LEVEL
from logger import get_logger
from extract.github_extractor import fetch_repository_data
from transform.data_transformer import transform_repository_data

logger = get_logger(__name__)


def main():
    """
    Entry point of the GitHub Analytics Data Platform.
    """
    logger.info("Application started")
    logger.info("Waiting for user input...")    
    logger.info(f"GitHub API URL: {GITHUB_API}")
    logger.info(f"Log level: {LOG_LEVEL}")

    owner = input("Enter GitHub Owner: ")
    repo = input("Enter Repository Name: ")

    repo_data = fetch_repository_data(owner, repo)

    if repo_data:
        
        # Save raw JSON response
        with open("data/cpython.json", "w") as file:
          json.dump(repo_data, file, indent=4)

        logger.info("Repository data saved successfully.")

        # Transform raw data
        clean_data = transform_repository_data(repo_data)
        # Save transformed data
        with open("data/clean_repository_data.json", "w") as file:
            json.dump(clean_data, file, indent=4)

        logger.info("Clean repository data saved successfully.")

        logger.info(f"Repository Name: {clean_data.get('repository_name')}")
        logger.info(f"Owner: {clean_data.get('owner')}")
        logger.info(f"Description: {clean_data.get('description')}")
        logger.info(f"Stars: {clean_data.get('stars')}")
        logger.info(f"Forks: {clean_data.get('forks')}")
        logger.info(f"Open Issues: {clean_data.get('open_issues')}")
        logger.info(f"Language: {clean_data.get('language')}")
        logger.info(f"Default Branch: {clean_data.get('default_branch')}")
        logger.info(f"Created At: {clean_data.get('created_at')}")
        logger.info(f"Updated At: {clean_data.get('updated_at')}")
    else:
        logger.error("No repository data received")

    logger.info("Application finished successfully")


if __name__ == "__main__":
    main()