-- 코드를 입력하세요
WITH USER_INFO_2021 AS (
    SELECT USER_ID
    FROM USER_INFO
    WHERE YEAR(JOINED) = 2021) 

SELECT 
    YEAR(SALES_DATE) AS YEAR,
    MONTH(SALES_DATE) AS MONTH,
    COUNT(DISTINCT A.USER_ID) AS PUCHASED_USERS,
    ROUND(COUNT(DISTINCT A.USER_ID)/(SELECT COUNT(*) FROM USER_INFO_2021), 1) AS PUCHASED_RATIO
FROM ONLINE_SALE AS A 
LEFT JOIN USER_INFO AS B 
ON A.USER_ID = B.USER_ID
WHERE YEAR(JOINED) = "2021"
GROUP BY YEAR, MONTH 
ORDER BY YEAR, MONTH;