# Database Design

## Overview
This document outlines the database schema and relationships for our Python application.

## Database Technology
- Primary: PostgreSQL
- ORM: SQLAlchemy
- Migration Tool: Alembic

## Schema Design

### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Example SQLAlchemy Model
```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
```

## Relationships
- One-to-Many: User -> Posts
- Many-to-Many: Users <-> Roles

## Indexing Strategy
- Index on username and email for fast lookups
- Index on foreign keys for relationship queries
- Composite indexes for common query patterns

## Data Access Patterns
```python
# Example repository pattern
class UserRepository:
    def __init__(self, db_session):
        self.db_session = db_session
    
    async def get_by_id(self, user_id: int) -> Optional[User]:
        return await self.db_session.get(User, user_id)
    
    async def create(self, user: UserCreate) -> User:
        db_user = User(**user.dict())
        self.db_session.add(db_user)
        await self.db_session.commit()
        return db_user
```

## Migration Strategy
- Use Alembic for schema migrations
- Always provide both upgrade and downgrade paths
- Include data migrations when necessary 