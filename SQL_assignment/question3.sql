-- Using the existing database
USE Tech4Girls_DB;

-- Creating the Courses table
CREATE TABLE IF NOT EXISTS Courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

-- Creating the User_Courses table (intermediate table)
CREATE TABLE IF NOT EXISTS User_Courses (
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    PRIMARY KEY (user_id, course_id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);

-- Inserting sample data into the Courses table
INSERT INTO Courses (course_name) VALUES
('Web Development'),
('Data Science'),
('Cybersecurity'),
('Artificial Intelligence');

-- Inserting sample data into the User_Courses table
INSERT INTO User_Courses (user_id, course_id) VALUES
(1, 1), -- ama enrolled in Web Development
(1, 2), -- ama enrolled in Data Science
(2, 2), -- Abena enrolled in Data Science
(2, 3), -- Abena enrolled in Cybersecurity
(3, 1), -- Adjoa enrolled in Web Development
(3, 4); -- Adjoa enrolled in Artificial Intelligence
