import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional


@dataclass
class Film:
    title: str
    type: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = field(default=None)
    certificate: Optional[str] = field(default=None)
    file_path: Optional[str] = None
    rating: float = field(default=0.0)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Genre:
    name: str
    description: Optional[str] = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class GenreFilmWork:
    genre_id: uuid.UUID
    film_work_id: uuid.UUID
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Person:
    full_name: str
    birth_date: Optional[datetime] = field(default=None)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class PersonFilmWork:
    film_work_id: uuid.UUID
    person_id: uuid.UUID
    role: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    id: uuid.UUID = field(default_factory=uuid.uuid4)
