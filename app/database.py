"""SQLAlchemy database setup primitives.

This module provides a declarative base that ORM models can inherit from.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""
