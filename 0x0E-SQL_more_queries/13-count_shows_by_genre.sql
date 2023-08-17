-- This query retrieves the genres and the number of
-- shows for each genre from the TV genres table.
-- It joins the TV genres table with the TV show 
-- genres table using the genre ID.
-- The result is grouped by genre and ordered by
-- the number of shows in descending order.

SELECT tv_genres.genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.genre
ORDER BY number_of_shows DESC;
