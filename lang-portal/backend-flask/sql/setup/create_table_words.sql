CREATE TABLE IF NOT EXISTS words (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  latin_spelling TEXT NOT NULL,
  origin_language TEXT NOT NULL,
  arabic_spelling TEXT, -- can be null for a French word
  english TEXT NOT NULL
);