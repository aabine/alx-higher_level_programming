-- Script to list all records of the table second_table in the database hbtn_0c_0
-- The database name will be passed as an argument of the mysql command.

USE hbtn_0c_0;

SELECT score, name
FROM second_table
ORDER BY score DESC;
