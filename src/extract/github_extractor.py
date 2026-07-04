import requests

from config import GITHUB_API
from logger import get_logger

logger = get_logger(__name__)


def fetch_repository_data(owner: str, repo: str):
    """
    Fetch repository information from GitHub API.
    """

    if not owner or not repo:
        logger.error("Owner or repository name is empty")
        return None

    url = f"{GITHUB_API}/repos/{owner.strip()}/{repo.strip()}"

    try:
        logger.info(f"Starting GitHub API request → {owner}/{repo}")

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            logger.info("GitHub API request successful")
            return response.json()

        elif response.status_code == 404:
            logger.error("Repository not found (404)")
            return None

        elif response.status_code == 403:
            logger.error("Access forbidden or rate limit exceeded (403)")
            return None

        else:
            logger.error(f"Unexpected status code: {response.status_code}")
            return None

    except requests.exceptions.Timeout:
        logger.error("Request timed out")
        return None

    except requests.exceptions.ConnectionError:
        logger.error("Network connection error")
        return None

    except requests.exceptions.RequestException as error:
        logger.error(f"Unexpected request error: {error}")
        return None

    except Exception as e:
        logger.error(f"Unexpected system error: {str(e)}")
        return None

    finally:
        logger.warning("Request cycle completed")