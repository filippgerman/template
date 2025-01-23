from enum import Enum


class EnvironmentEnum(str, Enum):
    """Enumeration for possible application environments."""

    LOCAL = "LOCAL"
    TEST = "TEST"
    DEV = "DEV"
    STG = "STG"
    PROD = "PROD"

    def __str__(self) -> str:
        """Return the string representation of the environment."""
        return self.value
