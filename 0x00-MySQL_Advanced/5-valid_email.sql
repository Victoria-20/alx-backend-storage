--  script that creates a trigger that resets the attribute 
-- valid_email only when the email has been changed.
CREATE TRIGGER reset_attribute_valid_email BEFORE UPDATE ON `users`.'email'
FOR EACH ROW
BEGIN
SET NEW.`valid_email` = `users`.`email`
END;