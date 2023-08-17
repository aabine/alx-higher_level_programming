-- Select the name column from the tv_genres table
-- This table stores the different genres of TV shows
SELECT tv_genres.name
FROM tv_genres

-- Join the tv_genres table with the tv_show_genres table
-- This table links genres to the TV shows they belong to
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id

-- Join the tv_show_genres table with the tv_shows table
-- This table stores information about TV shows
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id

-- Filter the results to only include TV shows with the title 'Dexter'
WHERE tv_shows.title = 'Dexter'

-- Order the results by genre name in ascending order
ORDER BY tv_genres.name ASC;
