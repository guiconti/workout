Given a string `` expression `` of numbers and operators, return _all possible results from computing all the different possible ways to group numbers and operators_. You may return the answer in __any order__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> expression = "2-1-1"
<strong>Output:</strong> [0,2]
<strong>Explanation:</strong>
((2-1)-1) = 0 
(2-(1-1)) = 2
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> expression = "2*3-4*5"
<strong>Output:</strong> [-34,-14,-10,-10,10]
<strong>Explanation:</strong>
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= expression.length &lt;= 20 ``
*   `` expression `` consists of digits and the operator `` '+' ``, `` '-' ``, and `` '*' ``.