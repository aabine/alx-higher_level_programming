-- Select the title of TV shows and their corresponding genre IDs
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- Perform a left join between the tv_shows and tv_show_genres tables
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Order the results in ascending order by title and genre ID
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
