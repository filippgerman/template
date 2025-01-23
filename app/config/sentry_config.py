from pydantic import BaseModel, Field


class SentryConfig(BaseModel):
    SENTRY_DSN: str = Field(..., json_schema_extra={"env": "SENTRY_DSN"})
