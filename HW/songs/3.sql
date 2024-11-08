SELECT artists.name, COUNT(songs.id) AS song_count 
FROM artists
JOIN songs ON artists.id
GROUP BY artists.id
ORDER BY song_count DESC
LIMIT 1;