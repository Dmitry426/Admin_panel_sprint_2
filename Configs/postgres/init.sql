CREATE SCHEMA IF NOT EXISTS content;
CREATE SCHEMA IF NOT EXISTS django;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE content.film_work (
    id UUID NOT NULL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    creation_date DATE,
    certificate TEXT,
    file_path VARCHAR(200),
    rating NUMERIC (2, 1),
    type VARCHAR(20) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);
CREATE TABLE content.genre(
    id UUID NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE content.person (
    id UUID NOT NULL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    birth_date DATE,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE content.genre_film_work(
    id UUID NOT NULL PRIMARY KEY,
    film_work_id UUID REFERENCES content.film_work (id) ON DELETE CASCADE,
    genre_id UUID REFERENCES content.genre (id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE content.person_film_work(
    id UUID NOT NULL PRIMARY KEY,
    film_work_id UUID REFERENCES content.film_work (id) ON DELETE CASCADE,
    person_id UUID REFERENCES content.person (id) On DELETE CASCADE,
    role VARCHAR(20) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE
);
CREATE UNIQUE INDEX film_work_person ON content.person_film_work (film_work_id, person_id, role);
CREATE UNIQUE INDEX film_work_genre ON content.genre_film_work (film_work_id, genre_id);