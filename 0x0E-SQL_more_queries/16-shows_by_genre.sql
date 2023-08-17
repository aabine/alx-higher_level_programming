-- This SQL query retrieves the titles of TV shows that belong to the 'Comedy' genre, ordered alphabetically.

-- SELECT statement to retrieve the title column from the tv_shows table.
-- Alias the table as 'tv_shows'.
SELECT tv_shows.title

-- JOIN tv_show_genres table with tv_shows table using the id column from both tables.
-- Alias the table as 'tv_show_genres'.
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id

-- JOIN tv_genres table with tv_show_genres table using the genre_id column from both tables.
-- Alias the table as 'tv_genres'.
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id

-- WHERE clause to filter the results to only include the genre with the name 'Comedy'.
WHERE tv_genres.name = 'Comedy'

-- ORDER BY clause to sort the results in ascending order based on the title column.
ORDER BY tv_shows.title ASC;
