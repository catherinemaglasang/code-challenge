/*
    Questions 1 (SQL):
    
    Given two tables. 
    What is the SQL syntax to get IDs from Table 1 that are not in Table 2? 
    (t1id is the primary key for Table 1, t2id is matching primary key from table 2)
*/

SELECT 
    GROUP_CONCAT(t1.`t1id`) AS `Table1IdsNotInTable2`
FROM 
    table1 t1 
    LEFT JOIN table2 t2 
        ON t1.`t1id` = t2.`t2id`
WHERE 1 = 1 
    AND t2.`t2id` IS NULL