-- Get the title and genre_id of TV shows that don't have a corresponding genre_id in tv_show_genres table
SELECT 
    tv_shows.title, 
    tv_show_genres.genre_id
FROM 
    tv_shows
LEFT JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE 
    tv_show_genres.genre_id IS NULL
ORDER BY 
    tv_shows.title ASC, tv_show_genres.genre_id ASC;

-- Explanation of the query:
-- 1. We select the title and genre_id columns from tv_shows table and tv_show_genres table.
-- 2. We perform a LEFT JOIN between tv_shows and tv_show_genres on the show_id column.
-- 3. We filter the result to only include rows where genre_id is NULL in tv_show_genres table.
-- 4. We sort the result by title in ascending order, and then by genre_id in ascending order.
