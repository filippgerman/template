import asyncio
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.asyncio import AsyncEngine

from alembic import context
from app.config.app import get_config
from app.infrastructure.database.base import Base

# Получаем конфигурацию приложения
config_app = get_config()

# Создаем URL базы данных из конфигурации
DATABASE_URL = (
    f"postgresql+asyncpg://{config_app.DATABASE_USER}:{config_app.DATABASE_PASSWORD}"
    f"@{config_app.DATABASE_SERVER}:{config_app.DATABASE_PORT}/{config_app.DATABASE_DB}"
)

# Устанавливаем URL базы данных в конфигурации Alembic
config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Настройка логирования
fileConfig(config.config_file_name)

# Указываем метаданные для автогенерации
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = AsyncEngine(
        engine_from_config(
            config.get_section(config.config_ini_section),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
            future=True,
        ),
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
