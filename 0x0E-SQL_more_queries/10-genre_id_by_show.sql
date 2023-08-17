-- Select the title and genre_id from the tv_shows and tv_show_genres tables
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- Join the tv_shows and tv_show_genres tables on the show_id column
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Order the results by title in ascending order, then by genre_id in ascending order
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
