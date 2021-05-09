Given an integer `` n ``. No-Zero integer is a positive integer which __doesn't contain any 0__ in its decimal representation.

Return _a list of two integers_ `` [A, B] `` where:

*   `` A `` and `` B `` are No-Zero integers.
*   `` A + B = n ``

It's guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> [1,1]
<strong>Explanation:</strong> A = 1, B = 1. A + B = n and both A and B don't contain any 0 in their decimal representation.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 11
<strong>Output:</strong> [2,9]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 10000
<strong>Output:</strong> [1,9999]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 69
<strong>Output:</strong> [1,68]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 1010
<strong>Output:</strong> [11,999]
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 10^4 ``