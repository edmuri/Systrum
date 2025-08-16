CREATE TABLE songs(
    album_name TEXT NOT NULL,
    artist TEXT NOT NULL,
    id TEXT PRIMARY KEY NOT NULL
    name TEXT NOT NULL,
    url TEXT NOT NULL
);

CREATE TABLE covers(
    album_name TEXT NOT NULL,
    artist TEXT NOT NULL,
    link TEXT NOT NULL
);