-- 코드를 작성해주세요
-- 2022년 평가 점수(HR_GRADE.SCORE)가 가장 높은 사원 정보 
-- HR_GRADE.SCORE, HR_EMPLOYEES.EMP_NO, HR_EMPLOYEES.EMP_NAME, HR_EMPLOYEES.POSITION, HR_EMPLOYEES.EMAIL

SELECT SCORE, E.EMP_NO, EMP_NAME, POSITION, EMAIL 
    FROM HR_EMPLOYEES E,
            (SELECT EMP_NO, SUM(SCORE) AS SCORE
                FROM HR_GRADE
                GROUP BY EMP_NO) G
    WHERE E.EMP_NO = G.EMP_NO
    ORDER BY 1 DESC LIMIT 1; 