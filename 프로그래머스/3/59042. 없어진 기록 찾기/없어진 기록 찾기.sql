-- 코드를 입력하세요
-- 입양을 간 기록은 있어 = ANIMAL_OUTS 테이블에 데이터 존재 
-- 보호소에 들어온 기록은 없어 = ANIMAL_OUTS 테이블에 데이터 존재 AND ANIMAL_INS 테이블에 데이터 존재 안 한다. 

-- 출력 컬럼: ANIMAL_ID, NAME
-- 정렬: ANIMAL_ID ASC 

SELECT ANIMAL_ID, NAME
    FROM ANIMAL_OUTS O 
    WHERE NOT EXISTS (SELECT 1 
                    FROM ANIMAL_INS I 
                    WHERE O.ANIMAL_ID = I.ANIMAL_ID)
    ORDER BY 1;
    
SELECT ANIMAL_ID, NAME
    FROM ANIMAL_OUTS
    WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID
                                FROM ANIMAL_INS)
    ORDER BY 1;