-- 'second_table' adlı cədvəli lazımi sütunlarla (id, name, score) yaradır.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Yaradılmış cədvələ tələb olunan 4 fərqli qeydi (sətri) daxil edir.
INSERT INTO second_table (id, name, score) VALUES 
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
