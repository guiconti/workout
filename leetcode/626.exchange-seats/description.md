Mary is a teacher in a middle school and she has a table `` seat `` storing students' names and their corresponding seat ids.

The column __id__ is continuous increment.

Mary wants to change seats for the adjacent students.

Can you write a SQL query to output the result for Mary?

&nbsp;

<pre>
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
</pre>

For the sample input, the output is:

<pre>
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
</pre>

__Note:__

If the number of students is odd, there is no need to change the last one's seat.