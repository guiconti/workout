Given an integer `` n ``, find a sequence that satisfies all of the following:

*   The integer `` 1 `` occurs once in the sequence.
*   Each integer between `` 2 `` and `` n `` occurs twice in the sequence.
*   For every integer `` i `` between `` 2 `` and `` n ``, the __distance__ between the two occurrences of `` i `` is exactly `` i ``.

The __distance__ between two numbers on the sequence, `` a[i] `` and `` a[j] ``, is the absolute difference of their indices, `` |j - i| ``.

Return _the __lexicographically largest__ sequence__. It is guaranteed that under the given constraints, there is always a solution. _

A sequence `` a `` is lexicographically larger than a sequence `` b `` (of the same length) if in the first position where `` a `` and `` b `` differ, sequence `` a `` has a number greater than the corresponding number in `` b ``. For example, `` [0,1,9,0] `` is lexicographically larger than `` [0,1,5,6] `` because the first position they differ is at the third number, and `` 9 `` is greater than `` 5 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> [3,1,2,3,2]
<strong>Explanation:</strong> [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> [5,3,1,4,3,5,2,4,2]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 20 ``