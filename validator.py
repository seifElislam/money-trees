"""
Validation module
"""
import os
from logs import log_exceptions, logger


@log_exceptions
def check_input_files(file_paths):
    """
    Checks if all required input files exist.
    Logs an error and exits the program if any file is missing.

    Args:
        file_paths (list): List of file paths to check.

    Returns:
        bool: True if all files exist, False otherwise.
    """
    missing_files = [file for file in file_paths if not os.path.isfile(file)]

    if missing_files:
        error_message = "The following required files are missing:\n" + "\n".join(f"- {file}" for file in missing_files)
        raise FileNotFoundError(error_message)

    logger.info("All required files are present.")
    return True
