"""
Custom exception
"""


class NonValidColumnsException(Exception):
    """
    Validation exception for dataset columns names
    """

    def __init__(self):
        """
        init class method
        """
        super().__init__()
        self.message = "invalid csv columns"


class AppException(Exception):
    """
    Main app exception
    """
