-- 코드를 입력하세요
-- 입양을 못 간 동물 = ANIMAL_OUTS에 데이터가 없음 
-- 가장 오래 보호소에 있었던 동물 3마리 = 위의 조건 + DATETIME 오름차순 LIMIT 3
-- 출력 컬럼: NAME, ANIMAL_INS.DATETIME 
-- 정렬: ANIMAL_INS.DATETIME 

SELECT NAME, DATETIME
    FROM ANIMAL_INS
    WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID 
                                FROM ANIMAL_OUTS)
    ORDER BY 2 
    LIMIT 3;