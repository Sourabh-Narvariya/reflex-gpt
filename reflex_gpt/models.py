"""Database models for Reflex-GPT application.

This module defines SQLModel database schemas for storing chat messages,
user sessions, and other persistent data. All models are fully typed and
documented for production use.
"""

from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Column, DateTime, Text
import uuid


class ChatMessage(SQLModel, table=True):
    """Chat message database model.
    
    Stores individual messages in conversations with timestamps and metadata.
    """
    __tablename__ = "chat_messages"
    
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        primary_key=True,
        description="Unique identifier for the message"
    )
    session_id: str = Field(
        foreign_key="chat_session.id",
        description="Reference to the chat session"
    )
    user_id: Optional[str] = Field(
        default=None,
        description="User who sent the message"
    )
    content: str = Field(
        sa_column=Column(Text),
        description="Message content"
    )
    is_bot: bool = Field(
        default=False,
        description="Whether message is from bot (AI) or user"
    )
    role: str = Field(
        default="user",
        description="Role: 'user', 'assistant', or 'system'"
    )
    created_at: datetime = Field(
        sa_column=Column(DateTime),
        default_factory=datetime.utcnow,
        description="Timestamp when message was created"
    )
    tokens_used: Optional[int] = Field(
        default=None,
        description="Approximate tokens used by OpenAI API"
    )


class ChatSession(SQLModel, table=True):
    """Chat session database model.
    
    Represents a conversation session with multiple messages.
    """
    __tablename__ = "chat_session"
    
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        primary_key=True,
        description="Unique identifier for the session"
    )
    user_id: Optional[str] = Field(
        default=None,
        description="User who owns this session"
    )
    title: str = Field(
        default="New Chat",
        description="Session title/name"
    )
    description: Optional[str] = Field(
        default=None,
        sa_column=Column(Text),
        description="Optional session description"
    )
    created_at: datetime = Field(
        sa_column=Column(DateTime),
        default_factory=datetime.utcnow,
        description="Timestamp when session was created"
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime),
        default_factory=datetime.utcnow,
        description="Timestamp when session was last updated"
    )
    is_active: bool = Field(
        default=True,
        description="Whether session is active/archived"
    )
    total_messages: int = Field(
        default=0,
        description="Total messages in this session"
    )
    total_tokens: int = Field(
        default=0,
        description="Total tokens used in this session"
    )
    # Relationship
    messages: List[ChatMessage] = []


class User(SQLModel, table=True):
    """User profile database model.
    
    Stores user information and preferences.
    """
    __tablename__ = "users"
    
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        primary_key=True,
        description="Unique user identifier"
    )
    username: str = Field(
        unique=True,
        index=True,
        description="Unique username"
    )
    email: str = Field(
        unique=True,
        index=True,
        description="User email address"
    )
    created_at: datetime = Field(
        sa_column=Column(DateTime),
        default_factory=datetime.utcnow,
        description="Account creation timestamp"
    )
    last_login: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime),
        description="Last login timestamp"
    )
    is_active: bool = Field(
        default=True,
        description="Whether account is active"
    )
    total_sessions: int = Field(
        default=0,
        description="Total chat sessions created"
    )
