-- Select the title column from the tv_shows table
SELECT tv_shows.title
FROM tv_shows
-- Join the tv_show_genres table on the show_id column
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Join the tv_genres table on the genre_id column
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Filter the results to only include shows with the genre 'Comedy'
WHERE tv_genres.name = 'Comedy'
-- Order the results by the title column in ascending order
ORDER BY tv_shows.title ASC;
