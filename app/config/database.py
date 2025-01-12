from pydantic import Field


class DatabaseConfig:
    """Configuration settings for the database.

    Attributes:
        DATABASE_SERVER (str): The database server address.
        DATABASE_USER (str): The username for the database.
        DATABASE_PASSWORD (str): The password for the database.
        DATABASE_DB (str): The name of the database.
        DATABASE_PORT (str): The port number for the database connection.

    """

    DATABASE_SERVER: str = Field(..., env="DATABASE_SERVER")
    DATABASE_USER: str = Field(..., env="DATABASE_USER")
    DATABASE_PASSWORD: str = Field(..., env="DATABASE_PASSWORD")
    DATABASE_DB: str = Field(..., env="DATABASE_DB")
    DATABASE_PORT: str = Field(..., env="DATABASE_PORT")
