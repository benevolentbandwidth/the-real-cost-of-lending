from app.core.config import settings


def get_storage_path(object_name: str) -> str:
    return f"gs://{settings.storage_bucket}/{settings.storage_prefix}{object_name}"

