Given an integer `` n ``, return _a string array_ `` answer `` (__1-indexed__) _where_:

*   `` answer[i] == "FizzBuzz" `` if `` i `` is divisible by `` 3 `` and `` 5 ``.
*   `` answer[i] == "Fizz" `` if `` i `` is divisible by `` 3 ``.
*   `` answer[i] == "Buzz" `` if `` i `` is divisible by `` 5 ``.
*   `` answer[i] == i `` if non of the above conditions are true.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["1","2","Fizz"]
</pre>

__Example 2:__

<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> ["1","2","Fizz","4","Buzz"]
</pre>

__Example 3:__

<pre><strong>Input:</strong> n = 15
<strong>Output:</strong> ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 10<sup>4</sup></code>