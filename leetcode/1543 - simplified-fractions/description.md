Given an integer `` n ``, return a list of all __simplified__ fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to `` n ``. The fractions can be in __any__ order.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> ["1/2"]
<strong>Explanation: </strong>"1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> ["1/2","1/3","2/3"]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> ["1/2","1/3","1/4","2/3","3/4"]
<strong>Explanation: </strong>"2/4" is not a simplified fraction because it can be simplified to "1/2".</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 100 ``