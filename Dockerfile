# --- Build Dependencies Stage ---
  FROM python:3.13-bullseye as requirements-stage
  WORKDIR /app

  # Install Poetry
  RUN pip install poetry

  # Copy dependency files
  COPY pyproject.toml poetry.lock /app/

  # Install dependencies without installing the project itself
  RUN poetry config virtualenvs.create false && \
      poetry install --no-root --only main

  # --- Final Image ---
  FROM python:3.13-bullseye as final
  WORKDIR /code

  # Copy dependencies from the requirements stage
  COPY --from=requirements-stage /usr/local /usr/local

  # Install system dependencies
  RUN apt-get update \
    && apt-get install -y kafkacat libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

  # Copy application code
  COPY . /code

  # Make scripts executable
  RUN chmod +x /code/entrypoint.sh

  # Set the entrypoint
  CMD ["sh", "/code/entrypoint.sh"]
