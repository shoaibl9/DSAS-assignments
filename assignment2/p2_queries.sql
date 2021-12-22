/*
Shoaib Laghari
Coursera Data Science at Scale Specialization
Assignment 2
11/25/21
*/

--explanation of matrices: https://www.varsitytutors.com/hotmath/hotmath_help/topics/matrix-multiplication

--Problem 2

/*
The matrix A and matrix B are both square matrices with 5 rows and 5 columns each.

(g) multiply: Express A X B as a SQL query, referring to the class lecture for hints.
*/

SELECT A.row_num, B.col_num, sum(A.value * B.value)
FROM A, B
WHERE A.col_num = B.row_num
GROUP BY A.row_num, B.col_num
