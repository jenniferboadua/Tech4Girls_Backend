--  Using the existing database
USE Tech4Girls_DB;

--  Creating the Posts table
CREATE TABLE IF NOT EXISTS Posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Inserting sample data into the Posts table
INSERT INTO Posts (user_id, title, content, created_at) VALUES
(1, 'Introduction to Programming', 'Programming is a vital skill in tech.', '2024-11-01 11:00:00'),
(1, 'Getting Started with Python', 'Python is a versatile and beginner-friendly language.', '2024-11-01 15:00:00'),
(2, 'Tech Trends 2024', 'Exploring the latest innovations in technology.', '2024-11-02 13:00:00'),
(3, 'Why Data Science Matters', 'Data science is transforming industries.', '2024-11-03 15:30:00'),
(3, 'Steps to Learn SQL', 'SQL is essential for managing databases effectively.', '2024-11-03 16:00:00');
