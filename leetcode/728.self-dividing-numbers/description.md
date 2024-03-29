A _self-dividing number_ is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because `` 128 % 1 == 0 ``, `` 128 % 2 == 0 ``, and `` 128 % 8 == 0 ``.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

__Example 1:__  

<pre>
<b>Input:</b> 
left = 1, right = 22
<b>Output:</b> [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
</pre>

__Note:__<li>The boundaries of each input argument are <code>1 &lt;= left &lt;= right &lt;= 10000</code>.</li>