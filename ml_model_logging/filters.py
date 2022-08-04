"""Filters for adding extra info to log records."""
import os
import logging
from typing import List
import platform


class HostnameFilter(logging.Filter):
    """Logging filter that adds the hostname to log records."""

    def filter(self, record):
        record.hostname = platform.uname()[1]
        return True


class EnvironmentInfoFilter(logging.Filter):
    """Logging filter that adds information to log records from environment variables."""

    def __init__(self, env_variables: List[str]):
        super().__init__()
        self._env_variables = env_variables

    def filter(self, record):
        for env_variable in self._env_variables:
            record.__setattr__(env_variable.lower(), os.environ.get(env_variable, "N/A"))
        return True
