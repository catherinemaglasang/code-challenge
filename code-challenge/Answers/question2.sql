/*
    Question 2 (SQL):
    
    Given a table that has multiple rows per id; 
    what is the SQL syntax to get the IDs and values of the rows with the latest modifiedDTS? 
*/

SELECT 
    t3.*
FROM 
    table3 t3 
WHERE 1 = 1 
    AND t3.`ModifiedDTS` = (
    	SELECT 
    		MAX(subt3.`ModifiedDTS`)
    	FROM 
    		table3 subt3
    	 WHERE 1 = 1
    	 	AND t3.`t3id` = subt3.`t3id`
    )
