Your task is to calculate <code>a<sup>b</sup></code> mod `` 1337 `` where `` a `` is a positive integer and `` b `` is an extremely large positive integer given in the form of an array.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> a = 2, b = [3]
<strong>Output:</strong> 8
</pre>

__Example 2:__

<pre><strong>Input:</strong> a = 2, b = [1,0]
<strong>Output:</strong> 1024
</pre>

__Example 3:__

<pre><strong>Input:</strong> a = 1, b = [4,3,3,8,5,2]
<strong>Output:</strong> 1
</pre>

__Example 4:__

<pre><strong>Input:</strong> a = 2147483647, b = [2,0,0]
<strong>Output:</strong> 1198
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= a &lt;= 2<sup>31</sup> - 1</code>
*   `` 1 &lt;= b.length &lt;= 2000 ``
*   `` 0 &lt;= b[i] &lt;= 9 ``
*   `` b `` doesn't contain leading zeros.