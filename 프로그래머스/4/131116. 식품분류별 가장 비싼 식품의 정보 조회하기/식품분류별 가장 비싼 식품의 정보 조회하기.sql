-- 코드를 입력하세요
-- 식품분류(CATEGORY)별 가격(PRICE)이 가장 비싼 물품 
-- CATEGORY, PRICE, PRODUCT_NAME
-- 식품분류(CATEGORY)가 '과자', '국', '김치', '식용유'인 경우만 출력
-- 정렬: 식품 가격 (PRICE) DESC 
# SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
#     FROM FOOD_PRODUCT 
#     WHERE PRICE IN (SELECT CATEGORY, PRODUCT_NAME, MAX(PRICE)
#                             FROM FOOD_PRODUCT
#                             WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
#                             GROUP BY CATEGORY)
#     ORDER BY 2 DESC; 
    
    
WITH
CATEGORY_MAX_PRICE AS (SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
                            FROM FOOD_PRODUCT
                            WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
                            GROUP BY CATEGORY)

    SELECT A.CATEGORY, B.MAX_PRICE, A.PRODUCT_NAME
        FROM FOOD_PRODUCT A, CATEGORY_MAX_PRICE B
        WHERE A.CATEGORY = B.CATEGORY AND A.PRICE = B.MAX_PRICE
        ORDER BY 2 DESC;