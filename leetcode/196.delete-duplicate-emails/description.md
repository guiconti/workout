Write a SQL query to __delete__ all duplicate email entries in a table named `` Person ``, keeping only unique emails based on its _smallest_ __Id__.

<pre>
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
</pre>

For example, after running your query, the above `` Person `` table should have the following rows:

<pre>
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
</pre>

__Note:__

Your output is the whole `` Person ``&nbsp;table after executing your sql. Use `` delete `` statement.