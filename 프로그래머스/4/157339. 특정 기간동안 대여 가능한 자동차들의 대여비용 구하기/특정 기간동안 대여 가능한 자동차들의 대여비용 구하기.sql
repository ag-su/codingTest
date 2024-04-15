-- 코드를 입력하세요
-- 자동차 종류(CAR_RENTAL_COMPANY_CAR.CAR_TYPE)가 '세단' 또는 'SUV'
-- 2022년 11월 1일 ~ 2022년 11월 30일 까지 대여 가능 (-> START_DATE~END_DATE 제외)
-- 30일 간의 대여 금액이 50만원 이상 200만원 미만인 자동차 (CAR_RENTAL_COMPANY_CAR.DAILY_FEE * 30)

-- CAR_ID, CAR_TYPE, FEE
-- 정렬: FEE DESC, CAR_TYPE ASC, CAR_ID DESC

SELECT CAR_ID, A.CAR_TYPE, ROUND(DAILY_FEE * (1-DISCOUNT_RATE) * 30) AS FEE 
    FROM CAR_RENTAL_COMPANY_CAR A, (SELECT CAR_TYPE, CAST(REPLACE(DISCOUNT_RATE, '%', '') AS DECIMAL(10, 2)) / 100 AS DISCOUNT_RATE
                                        FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                        WHERE DURATION_TYPE = '30일 이상') B 
    WHERE A.CAR_TYPE = B.CAR_TYPE 
            AND A.CAR_TYPE IN ("세단", 'SUV')
            AND DAILY_FEE * (1-DISCOUNT_RATE) * 30 >= 500000 AND DAILY_FEE * (1-DISCOUNT_RATE) * 30< 2000000
            AND CAR_ID NOT IN (SELECT DISTINCT CAR_ID
                                FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                                WHERE (START_DATE LIKE '2022-11-%' OR END_DATE LIKE '2022-11-%')
        OR
        (START_DATE <= '2022-11-01' AND END_DATE >= '2022-11-30'))
    ORDER BY 3 DESC, 2, 1 DESC;