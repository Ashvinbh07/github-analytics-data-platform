import requests

from config import GITHUB_API
from logger import get_logger

logger = get_logger(__name__)


def fetch_repository_data(owner: str, repo: str):
    """
    Fetch repository information from GitHub API.
    """
    url = f"{GITHUB_API}/repos/{owner}/{repo}"

    try:
        logger.info(f"Fetching repository data for {owner}/{repo}")

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            logger.info("Repository data fetched successfully")
            return response.json()

        if response.status_code == 404:
            logger.error(f"Repository not found: {owner}/{repo}")
            return None

        logger.error(f"Failed to fetch data. Status code: {response.status_code}")
        return None

    except requests.exceptions.Timeout:
        logger.error("Request timed out")
        return None

    except requests.exceptions.ConnectionError:
        logger.error("Connection error. Please check your internet connection")
        return None

    except requests.exceptions.RequestException as error:
        logger.error(f"Unexpected request error: {error}")
        return None