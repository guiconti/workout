Given an integer `` n ``, return `` true `` _if it is possible to represent _`` n ``_ as the sum of distinct powers of three._ Otherwise, return `` false ``.

An integer `` y `` is a power of three if there exists an integer `` x `` such that <code>y == 3<sup>x</sup></code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 12
<strong>Output:</strong> true
<strong>Explanation:</strong> 12 = 3<sup>1</sup> + 3<sup>2</sup>
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 91
<strong>Output:</strong> true
<strong>Explanation:</strong> 91 = 3<sup>0</sup> + 3<sup>2</sup> + 3<sup>4</sup>
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 21
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 10<sup>7</sup></code>