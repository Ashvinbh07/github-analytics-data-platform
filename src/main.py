from config import GITHUB_API, LOG_LEVEL
from logger import get_logger
from extract.github_extractor import fetch_repository_data

logger = get_logger(__name__)


def main():
    """
    Entry point of the GitHub Analytics Data Platform.
    """
    logger.info("Application started")
    logger.info(f"GitHub API URL: {GITHUB_API}")
    logger.info(f"Log level: {LOG_LEVEL}")

    repo_data = fetch_repository_data("python", "cpython")

    if repo_data:
        logger.info(f"Repository Name: {repo_data.get('name')}")
        logger.info(f"Owner: {repo_data.get('owner', {}).get('login')}")
        logger.info(f"Stars: {repo_data.get('stargazers_count')}")
        logger.info(f"Forks: {repo_data.get('forks_count')}")
        logger.info(f"Open Issues: {repo_data.get('open_issues_count')}")
        logger.info(f"Default Branch: {repo_data.get('default_branch')}")
        logger.info(f"Language: {repo_data.get('language')}")
    else:
        logger.error("No repository data received")

    logger.info("Application finished successfully")


if __name__ == "__main__":
    main()