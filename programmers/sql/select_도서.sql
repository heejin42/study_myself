SELECT BOOK_ID, date_format(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE FROM BOOK
WHERE PUBLISHED_DATE LIKE '2021%' AND CATEGORY = '인문'
ORDER BY PUBLISHED_DATE;

# SELECT BOOK_ID, date_format(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
# FROM BOOK
# WHERE CATEGORY ='인문' AND YEAR(PUBLISHED_DATE) = 2021
# ORDER BY PUBLISHED_DATE;

