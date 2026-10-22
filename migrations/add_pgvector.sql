CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE menu_item_embeddings (
    id SERIAL PRIMARY KEY,
    menu_item_id INTEGER REFERENCES menu_items(id) ON DELETE CASCADE,
    embedding vector(384),
    content TEXT
);