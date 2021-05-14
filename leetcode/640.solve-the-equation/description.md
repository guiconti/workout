Solve a given equation and return the value of `` 'x' `` in the form of a string `` "x=#value" ``. The equation contains only `` '+' ``, `` '-' `` operation, the variable `` 'x' `` and its coefficient. You should return `` "No solution" `` if there is no solution for the equation, or `` "Infinite solutions" `` if there are infinite solutions for the equation.

If there is exactly one solution for the equation, we ensure that the value of `` 'x' `` is an integer.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> equation = "x+5-3+x=6+x-2"
<strong>Output:</strong> "x=2"
</pre>

__Example 2:__

<pre><strong>Input:</strong> equation = "x=x"
<strong>Output:</strong> "Infinite solutions"
</pre>

__Example 3:__

<pre><strong>Input:</strong> equation = "2x=x"
<strong>Output:</strong> "x=0"
</pre>

__Example 4:__

<pre><strong>Input:</strong> equation = "2x+3x-6x=x+2"
<strong>Output:</strong> "x=-1"
</pre>

__Example 5:__

<pre><strong>Input:</strong> equation = "x=x+2"
<strong>Output:</strong> "No solution"
</pre>

&nbsp;

__Constraints:__

*   `` 3 &lt;= equation.length &lt;= 1000 ``
*   `` equation `` has exactly one `` '=' ``.
*   `` equation `` consists of integers with an absolute value in the range `` [0, 100] `` without any leading zeros, and the variable `` 'x' ``.