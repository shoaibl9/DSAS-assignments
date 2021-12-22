/*
Shoaib Laghari
Coursera Data Science at Scale Specialization
Assignment 2
11/25/21
*/

--Problem 1

/*
(a) select: Write a query that is equivalent to the following relational algebra expression.

σdocid=10398_txt_earn(frequency)
*/

SELECT count(*) FROM Frequency WHERE docid="10398_txt_earn";

/*
(b) select project: Write a SQL statement that is equivalent to the following relational algebra expression.

πterm(σdocid=10398_txt_earn and count=1(frequency))
*/

SELECT count(*) 
FROM (
    SELECT * 
    FROM Frequency
    WHERE docid="925_txt_trade" AND count=1
);

/*
(c) union: Write a SQL statement that is equivalent to the following relational algebra expression. (Hint: you can use the UNION keyword in SQL)

πterm(σdocid=10398_txt_earn and count=1(frequency)) U πterm(σdocid=925_txt_trade and count=1(frequency))
*/

SELECT count(*) 
FROM (
    SELECT term
    FROM (
        SELECT * 
        FROM Frequency
        WHERE docid="10398_txt_earn" AND count=1
    )

    UNION

    SELECT term
    FROM (
        SELECT * 
        FROM Frequency
        WHERE docid="925_txt_trade" AND count=1
    )
);

/*
(d) count: Write a SQL statement to count the number of unique documents containing the word "law" or containing the word "legal"  (If a document contains both law and legal, it should only be counted once)
*/

SELECT count(*)
FROM (
    SELECT DISTINCT docid FROM Frequency WHERE term="law" OR term="legal"
);

/*
(e) big documents: Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms. (Hint: You can use the HAVING clause, or you can use a nested query. Another hint: Remember that the count column contains the term frequencies, and you want to consider duplicates.) (docid, term_count)
*/

SELECT count(*)
From (
    SELECT * FROM Frequency GROUP BY docid HAVING sum(count) > 300
);

/*
(f) two words: Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'.  (Hint: Find the docs that contain one word and the docs that contain the other word separately, then find the intersection.)
*/
SELECT count(*)
FROM (
    SELECT docid FROM Frequency WHERE term="transactions"
    INTERSECT
    SELECT docid FROM Frequency WHERE term="world"
);

