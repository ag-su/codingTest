-- 코드를 입력하세요
-- 2022년 4월 13일 취소되지 않은 (APPOINTMENT.APNT_CNCL_YMD != 2022년 4월 13)
-- 흉부외과 (CS) 진료 예약 내역 (MCDP_CD = CS)

-- 출력 컬럼: APNT_NO, PT_NAME, PT_NO, MCDP_CD, DR_NAME, APNT_YMD
-- 정렬: APNT_YMD ASC

SELECT APNT_NO, PT_NAME, P.PT_NO, MCDP_CD, DR_NAME, APNT_YMD
    FROM (SELECT APNT_YMD, APNT_NO, PT_NO, MDDR_ID
            FROM APPOINTMENT
            WHERE MCDP_CD = 'CS'
                    AND DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = "2022-04-13"
                    AND APNT_CNCL_YN = 'N') A,
         PATIENT P,
         DOCTOR D
    WHERE A.PT_NO = P.PT_NO 
            AND A.MDDR_ID = D.DR_ID
    ORDER BY APNT_YMD;
    
    