1.
SELECT
AVG(energy) AS average_energy
AVG(valence) AS average_valence
AVG(danceability) AS average_danceability
FROM songs;

This will get you the average values for energy, valence, and danceability assuming a listeners top 100 songs are the same as the ones found on songs.db
High energy can show that the listener likes songs that are very energetic(pop, hip hop, etc)
High valence can show that the listener likes songs that are more happy(pop, etc)
High danceability can show that the listener likes songs that are easy to dance to (hip hop, edm, etc)


2.
It can be unraliable if the listener listenes to very diverse music like if they listen to very upbeat music and very slow music the average might return something in the middle which the listener might not actually like

It is also missing context. For example, I dont like heavy metal or rock but I listen to it a lot in the gym. I also dont like "low-fi" music but I listen to it while studying/working. But these are very different from what I listen to for "fun". So if it gave me a combination of metal and indie music it might not be what I want to listen to on a daily basis