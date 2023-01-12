--  SQL script that creates a trigger that decreases
-- the quantity of an item after adding a new order
CREATE TRIGGER dec_qty BEFORE INSERT ON `items`
FOR EACH ROW
BEGIN
SET `items`.`quantity` = `items`.`quantity` - 1
END;