from logger import get_logger

logger = get_logger(__name__)


def transform_repository_data(repo_data: dict) -> dict:
    """
    Transform raw GitHub repository data into a clean dictionary.
    """
    logger.info("Transforming repository data")

    clean_data = {
        "repository_name": repo_data.get("name"),
        "owner": repo_data.get("owner", {}).get("login"),
        "description": repo_data.get("description"),
        "stars": repo_data.get("stargazers_count"),
        "forks": repo_data.get("forks_count"),
        "open_issues": repo_data.get("open_issues_count"),
        "language": repo_data.get("language"),
        "default_branch": repo_data.get("default_branch"),
        "created_at": repo_data.get("created_at"),
        "updated_at": repo_data.get("updated_at"),
    }

    logger.info("Repository data transformed successfully")
    return clean_data