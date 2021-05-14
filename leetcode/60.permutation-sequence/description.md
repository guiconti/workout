The set `` [1, 2, 3, ...,&nbsp;n] `` contains a total of `` n! `` unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for `` n = 3 ``:

1.   `` "123" ``
2.   `` "132" ``
3.   `` "213" ``
4.   `` "231" ``
5.   `` "312" ``
6.   `` "321" ``

Given `` n `` and `` k ``, return the <code>k<sup>th</sup></code> permutation sequence.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> n = 3, k = 3
<strong>Output:</strong> "213"
</pre>

__Example 2:__

<pre><strong>Input:</strong> n = 4, k = 9
<strong>Output:</strong> "2314"
</pre>

__Example 3:__

<pre><strong>Input:</strong> n = 3, k = 1
<strong>Output:</strong> "123"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 9 ``
*   `` 1 &lt;= k &lt;= n! ``