from enum import Enum


class EnvironmentEnum(str, Enum):
    """Enumeration for possible application environments.

    Attributes:
        LOCAL (str): Local development environment.
        DEV (str): Development environment.
        STG (str): Staging environment.
        PROD (str): Production environment.

    """

    LOCAL = "LOCAL"
    DEV = "DEV"
    STG = "STG"
    PROD = "PROD"

    def __str__(self) -> str:
        """Return the string representation of the environment.

        Returns:
            str: The string representation of the environment.

        """
        return self.value
