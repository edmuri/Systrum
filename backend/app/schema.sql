CREATE TABLE songs(
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    album_name TEXT NOT NULL,
    id TEXT PRIMARY KEY NOT NULL
);

CREATE TABLE covers(
    album_name TEXT NOT NULL,
    link TEXT NOT NULL,
    FOREIGN KEY (album_name) REFERENCES songs(album_name)
);