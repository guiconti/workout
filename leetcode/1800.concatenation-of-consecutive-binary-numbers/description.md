Given an integer `` n ``, return _the __decimal value__ of the binary string formed by concatenating the binary representations of _`` 1 ``_ to _`` n ``_ in order, __modulo ___<code>10<sup>9 </sup>+ 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
<strong>Explanation: </strong>"1" in binary corresponds to the decimal value 1. 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 27
<strong>Explanation: </strong>In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 12
<strong>Output:</strong> 505379714
<strong>Explanation</strong>: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 10<sup>9</sup> + 7, the result is 505379714.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>