-- 코드를 작성해주세요
-- 사원별(HR_EMPLOYEES.EMP_NO), 평가등급(GRADE) 성과금(BONUS) 정보 
    -- 점수(SCORE) 별 평가등급, 성과금 계산 
-- HR_EMPLOYEES.EMP_NO, HR_EMPLOYEES.EMP_NAME, GRADE, BONUS

WITH 
GRADE_BONUS AS (SELECT EMP_NO, 
                        CASE WHEN AVG(SCORE) >= 96 THEN 'S'
                             WHEN AVG(SCORE) >= 90 THEN 'A'
                             WHEN AVG(SCORE) >= 80 THEN 'B'
                        ELSE 'C' END AS GRADE
                    FROM HR_GRADE
                    GROUP BY 1)         
    SELECT G.EMP_NO, EMP_NAME, GRADE,
                CASE GRADE WHEN 'S' THEN 0.2 * SAL
                           WHEN 'A' THEN 0.15 * SAL
                           WHEN 'B' THEN 0.1 * SAL
                ELSE 0 END AS BONUS 
        FROM GRADE_BONUS G, HR_EMPLOYEES E
        WHERE G.EMP_NO = E.EMP_NO
        ORDER BY 1;