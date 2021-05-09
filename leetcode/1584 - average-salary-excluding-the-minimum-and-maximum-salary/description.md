Given an array of __unique__ integers `` salary ``&nbsp;where `` salary[i] `` is the salary of the employee `` i ``.

Return the average salary of employees excluding the minimum and maximum salary.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> salary = [4000,3000,1000,2000]
<strong>Output:</strong> 2500.00000
<strong>Explanation: </strong>Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> salary = [1000,2000,3000]
<strong>Output:</strong> 2000.00000
<strong>Explanation: </strong>Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000)/1= 2000
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> salary = [6000,5000,4000,3000,2000,1000]
<strong>Output:</strong> 3500.00000
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> salary = [8000,9000,2000,3000,6000,1000]
<strong>Output:</strong> 4750.00000
</pre>

&nbsp;

__Constraints:__

*   `` 3 &lt;= salary.length &lt;= 100 ``
*   `` 10^3&nbsp;&lt;= salary[i] &lt;= 10^6 ``
*   `` salary[i] `` is unique.
*   Answers within `` 10^-5 `` of the actual value will be accepted as correct.