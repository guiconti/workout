Given an integer&nbsp;`` k ``, _return the minimum number of Fibonacci numbers whose sum is equal to _`` k ``. The same Fibonacci number can be used multiple times.

The Fibonacci numbers are defined as:

*   <code>F<sub>1</sub> = 1</code>
*   <code>F<sub>2</sub> = 1</code>
*   <code>F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub></code> for `` n &gt; 2. ``

It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to `` k ``.
&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> k = 7
<strong>Output:</strong> 2 
<strong>Explanation:</strong> The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> k = 10
<strong>Output:</strong> 2 
<strong>Explanation:</strong> For k = 10 we can use 2 + 8 = 10.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> k = 19
<strong>Output:</strong> 3 
<strong>Explanation:</strong> For k = 19 we can use 1 + 5 + 13 = 19.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= k &lt;= 10^9 ``