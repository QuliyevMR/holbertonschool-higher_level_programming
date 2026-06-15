-- 'second_table' cədvəlində xalı 10 və ya daha çox olan qeydləri seçir.
-- Nəticəni xala görə azalan sıra ilə düzür.
SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC;
