CREATE TABLE IF NOT EXISTS songs(
    album TEXT NOT NULL,
    artist TEXT NOT NULL,
    id TEXT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    word TEXT NOT NULL,
    url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS covers(
    album TEXT NOT NULL,
    artist TEXT NOT NULL,
    link TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tokens(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    spotify_id TEXT NOT NULL,
    access_token TEXT NOT NULL,
    refresh_token TEXT NOT NULL,
    is_logged_in INT NOT NULL
);

CREATE TABLE IF NOT EXISTS contact(
    name TEXT,
    role TEXT,
    github TEXT,
    linkedin TEXT
);