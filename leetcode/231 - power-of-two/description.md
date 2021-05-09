Given an integer `` n ``, return _`` true `` if it is a power of two. Otherwise, return `` false ``_.

An integer `` n `` is a power of two, if there exists an integer `` x `` such that <code>n == 2<sup>x</sup></code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>0</sup> = 1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 16
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>4</sup> = 16
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> false
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> true
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code>

&nbsp;
__Follow up:__ Could you solve it without loops/recursion?