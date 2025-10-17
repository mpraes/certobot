"""
Database configuration and connection management.
Handles PostgreSQL connection using SQLAlchemy with async support.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.core.settings import settings

# Create async engine
engine = create_async_engine(
    settings.database_url,
    echo=settings.is_development,  # Log SQL queries in development
    future=True,
)

# Create async session factory
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base class for SQLAlchemy models
Base = declarative_base()


async def get_db() -> AsyncSession:
    """
    Dependency to get database session.
    Use this in FastAPI endpoints to get a database session.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


async def init_db():
    """Initialize database tables."""
    async with engine.begin() as conn:
        # Import all models here to ensure they are registered
        # from backend.models import debtor, debt, conversation, message, outcome
        
        # Create all tables
        await conn.run_sync(Base.metadata.create_all)


async def close_db():
    """Close database connections."""
    await engine.dispose()