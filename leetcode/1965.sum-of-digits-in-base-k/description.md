Given an integer `` n `` (in base `` 10 ``) and a base `` k ``, return _the __sum__ of the digits of _`` n ``_ __after__ converting _`` n ``_ from base _`` 10 ``_ to base _`` k ``.

After converting, each digit should be interpreted as a base `` 10 `` number, and the sum should be returned in base `` 10 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 34, k = 6
<strong>Output:</strong> 9
<strong>Explanation: </strong>34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 10, k = 10
<strong>Output:</strong> 1
<strong>Explanation: </strong>n is already in base 10. 1 + 0 = 1.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 100 ``
*   `` 2 &lt;= k &lt;= 10 ``