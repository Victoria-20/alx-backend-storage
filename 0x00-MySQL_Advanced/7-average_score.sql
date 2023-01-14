-- SQL script that creates a stored procedure 
-- ComputeAverageScoreForUser that computes and store the 
-- average score for a student
CREATE PROCEDURE ComputeAverageScoreForUser @user_id
AS
UPDATE users
SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = @user_id)
GO;
