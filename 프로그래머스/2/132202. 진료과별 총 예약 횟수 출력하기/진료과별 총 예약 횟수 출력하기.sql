-- 코드를 입력하세요
-- 진료과 코드(MCDP_CD) 별 2022년 5월(APNT_YMD) 예약 환자 수 
-- 진료과 코드, 5월 예약건수 
-- 정렬: 5월예약건수 ASC, 진료과 코드 ASC 
SELECT MCDP_CD AS "진료과코드", COUNT(*) AS "5월예약건수"
    FROM APPOINTMENT 
    WHERE DATE_FORMAT(APNT_YMD, '%Y-%m') = "2022-05"
    GROUP BY 1
    ORDER BY 2, 1;
    