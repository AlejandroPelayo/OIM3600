SELECT name
FROM songs
WHERE tempo > (SELECT AVG(tempo) FROM songs);
