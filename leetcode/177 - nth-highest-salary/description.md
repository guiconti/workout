Write a SQL query to get the _n_<sup>th</sup> highest salary from the `` Employee `` table.

<pre>
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
</pre>

For example, given the above Employee table, the _n_<sup>th</sup> highest salary where _n_ = 2 is `` 200 ``. If there is no _n_<sup>th</sup> highest salary, then the query should return `` null ``.

<pre>
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
</pre>