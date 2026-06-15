-- 'second_table' cədvəlindəki bütün qeydləri score və name sütunları olmaqla siyahılayır.
-- Nəticələri score sütununa görə azalan sıra ilə (ən yüksək xal birinci) nizamlayır.
SELECT score, name FROM second_table ORDER BY score DESC;
