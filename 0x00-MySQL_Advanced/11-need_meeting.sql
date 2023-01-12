-- create view statement
CREATE VIEW need_meeting AS
SELECT * FROM students
WHERE score < 80 AND last_meeting IS NULL OR last_meeting > 1;