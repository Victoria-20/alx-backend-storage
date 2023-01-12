-- SQL script that creates a stored procedure 
-- ComputeAverageScoreForUser that computes and store the 
-- average score for a student
CREATE PROCEDURE ComputeAverageScoreForUser @user_id
AS
SELECT AVG(score) FROM corrections WHERE users.id = @user_id
GO;
