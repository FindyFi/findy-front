CREATE TABLE IF NOT EXISTS users (
    email VARCHAR(255),
    password VARCHAR(64)
);

-- inserts user 'test@findy.fi' and a 'test' hashed password
INSERT INTO users (email, password) VALUES ('test@findy.fi', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08');
