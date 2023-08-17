-- Retrieves all genres from the hbtn_0d_tvshows table and displays the number of shows associated with each genre.
-- Retrieves all rows from the database that meet a specified condition.

SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
