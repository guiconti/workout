The __Fibonacci numbers__, commonly denoted `` F(n) `` form a sequence, called the __Fibonacci sequence__, such that each number is the sum of the two preceding ones, starting from `` 0 `` and `` 1 ``. That is,

<pre>
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n &gt; 1.
</pre>

Given `` n ``, calculate `` F(n) ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= n &lt;= 30 ``