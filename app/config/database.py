from pydantic import BaseModel, Field


class DatabaseConfig(BaseModel):
    """Configuration settings for the database."""

    DATABASE_SERVER: str = Field(..., json_schema_extra={"env": "DATABASE_SERVER"})
    DATABASE_USER: str = Field(..., json_schema_extra={"env": "DATABASE_USER"})
    DATABASE_PASSWORD: str = Field(..., json_schema_extra={"env": "DATABASE_PASSWORD"})
    DATABASE_DB: str = Field(..., json_schema_extra={"env": "DATABASE_DB"})
    DATABASE_PORT: str = Field(..., json_schema_extra={"env": "DATABASE_PORT"})
    DATABASE_ECHO: bool = Field(..., json_schema_extra={"env": "DATABASE_ECHO"})
