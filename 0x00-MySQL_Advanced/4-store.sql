--  SQL script that creates a trigger that decreases
-- the quantity of an item after adding a new order
CREATE TRIGGER dec_qty BEFORE INSERT ON items
FOR EACH ROW SET @qty = @qty - NEW.quantity