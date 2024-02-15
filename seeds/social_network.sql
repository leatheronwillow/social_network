DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS post_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT,
    username TEXT
);

CREATE SEQUENCE IF NOT EXISTS post_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    views INT,
    user_id INT,
    CONSTRAINT fk_users FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON DELETE CASCADE
);

INSERT INTO users (email, username) VALUES ('m.h.azad-14@outlook.com', 'batpadman');
INSERT INTO users (email, username) VALUES ('f.p.ghouri@yahoo.com', 'leatheronwillow');

INSERT INTO posts (title, content, views, user_id) VALUES ('LOL', 'Laugh Out Loud', 25, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('ROFL', 'Rolling on the Floor with Laughter', 10, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('YOLO', 'you only live okay', 1000, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Dunno', 'I don''t know', 1000, 2);