Write an algorithm to determine if a number `` n `` is happy.

A __happy number__ is a number defined by the following process:

*   Starting with any positive integer, replace the number by the sum of the squares of its digits.
*   Repeat the process until the number equals 1 (where it will stay), or it __loops endlessly in a cycle__ which does not include 1.
*   Those numbers for which this process __ends in 1__ are happy.

Return `` true `` _if_ `` n `` _is a happy number, and_ `` false `` _if not_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 19
<strong>Output:</strong> true
<strong>Explanation:</strong>
1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code>