/* Write your PL/SQL query statement below */

SELECT C.name
FROM Customer C
WHERE C.referee_id IS NULL or C.referee_id != 2