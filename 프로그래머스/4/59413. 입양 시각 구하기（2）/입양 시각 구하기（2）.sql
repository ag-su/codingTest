-- 코드를 입력하세요
-- 시간대 별 (0~23) 카운트
-- 정렬: HOUR ASC
WITH RECURSIVE numbers AS (
        SELECT 0 AS HOUR
        UNION ALL
        SELECT HOUR + 1 FROM numbers WHERE HOUR < 23
    ),
     CNT AS (
        SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT 
        FROM ANIMAL_OUTS
        GROUP BY 1
    )
        SELECT A.HOUR, IFNULL(COUNT, 0)
        FROM NUMBERS A LEFT JOIN CNT B
                ON A.HOUR = B.HOUR 
        ORDER BY 1; 
