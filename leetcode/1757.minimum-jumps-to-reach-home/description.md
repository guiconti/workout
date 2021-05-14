A certain bug's home is on the x-axis at position `` x ``. Help them get there from position `` 0 ``.

The bug jumps according to the following rules:

*   It can jump exactly `` a `` positions __forward__ (to the right).
*   It can jump exactly `` b `` positions __backward__ (to the left).
*   It cannot jump backward twice in a row.
*   It cannot jump to any `` forbidden `` positions.

The bug may jump forward __beyond__ its home, but it __cannot jump__ to positions numbered with __negative__ integers.

Given an array of integers `` forbidden ``, where `` forbidden[i] `` means that the bug cannot jump to the position `` forbidden[i] ``, and integers `` a ``, `` b ``, and `` x ``, return _the minimum number of jumps needed for the bug to reach its home_. If there is no possible sequence of jumps that lands the bug on position `` x ``, return `` -1. ``

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 jumps forward (0 -&gt; 3 -&gt; 6 -&gt; 9) will get the bug home.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
<strong>Output:</strong> -1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
<strong>Output:</strong> 2
<strong>Explanation:</strong> One jump forward (0 -&gt; 16) then one jump backward (16 -&gt; 7) will get the bug home.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= forbidden.length &lt;= 1000 ``
*   `` 1 &lt;= a, b, forbidden[i] &lt;= 2000 ``
*   `` 0 &lt;= x &lt;= 2000 ``
*   All the elements in `` forbidden `` are distinct.
*   Position `` x `` is not forbidden.