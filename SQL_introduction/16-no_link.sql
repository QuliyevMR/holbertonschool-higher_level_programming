-- Lists all records of the table second_table
-- Filters out rows without a name value and sorts by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ""
ORDER BY score DESC;
