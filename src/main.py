from config import GITHUB_API, LOG_LEVEL
from logger import get_logger

logger = get_logger(__name__)


def main():
    try:
         logger.info("Application started")
         logger.info(f"GitHub API URL: {GITHUB_API}")
         logger.info(f"Log level: {LOG_LEVEL}")
         logger.info("Application finished successfully")

    except Exception as e:
         logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()