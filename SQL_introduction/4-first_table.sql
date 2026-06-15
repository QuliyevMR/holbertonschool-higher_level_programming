-- Cari verilənlər bazasında 'first_table' adlı cədvəl yaradır.
-- Cədvəlin sütunları: id (tam ədəd) və name (maksimum 256 simvollu mətn).
-- Cədvəl artıq mövcuddursa, xəta vermir.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
