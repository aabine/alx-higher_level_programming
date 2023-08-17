-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the cities table if it doesn't already exist
CREATE TABLE IF NOT EXISTS cities (
  id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each city
  state_id INT NOT NULL, -- Foreign key referencing the states table
  name VARCHAR(256) NOT NULL, -- Name of the city
  FOREIGN KEY (state_id) REFERENCES states(id) -- Establish a foreign key relationship with the states table
);
