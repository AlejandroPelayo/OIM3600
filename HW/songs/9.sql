SELECT artists.name, AVG(songs.danceability) AS avg_danceability
FROM artists
JOIN songs ON artists.id = songs.artist_id
GROUP BY artists.id
HAVING COUNT(songs.id) > 2;

