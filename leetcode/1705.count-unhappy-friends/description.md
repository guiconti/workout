You are given a list of&nbsp;`` preferences ``&nbsp;for&nbsp;`` n ``&nbsp;friends, where `` n `` is always __even__.

For each person `` i ``,&nbsp;`` preferences[i] ``&nbsp;contains&nbsp;a list of friends&nbsp;__sorted__ in the __order of preference__. In other words, a friend earlier in the list is more preferred than a friend later in the list.&nbsp;Friends in&nbsp;each list are&nbsp;denoted by integers from `` 0 `` to `` n-1 ``.

All the friends are divided into pairs.&nbsp;The pairings are&nbsp;given in a list&nbsp;`` pairs ``,&nbsp;where <code>pairs[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> denotes <code>x<sub>i</sub></code>&nbsp;is paired with <code>y<sub>i</sub></code> and <code>y<sub>i</sub></code> is paired with <code>x<sub>i</sub></code>.

However, this pairing may cause some of the friends to be unhappy.&nbsp;A friend `` x ``&nbsp;is unhappy if `` x ``&nbsp;is paired with `` y ``&nbsp;and there exists a friend `` u ``&nbsp;who&nbsp;is paired with `` v ``&nbsp;but:

*   `` x ``&nbsp;prefers `` u ``&nbsp;over `` y ``,&nbsp;and
*   `` u ``&nbsp;prefers `` x ``&nbsp;over `` v ``.

Return _the number of unhappy friends_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Friend 1 is unhappy because:
- 1 is paired with 0 but prefers 3 over 0, and
- 3 prefers 1 over 2.
Friend 3 is unhappy because:
- 3 is paired with 2 but prefers 1 over 2, and
- 1 prefers 3 over 0.
Friends 0 and 2 are happy.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Both friends 0 and 1 are happy.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 500 ``
*   `` n ``&nbsp;is even.
*   `` preferences.length&nbsp;== n ``
*   `` preferences[i].length&nbsp;== n - 1 ``
*   `` 0 &lt;= preferences[i][j] &lt;= n - 1 ``
*   `` preferences[i] ``&nbsp;does not contain `` i ``.
*   All values in&nbsp;`` preferences[i] ``&nbsp;are unique.
*   `` pairs.length&nbsp;== n/2 ``
*   `` pairs[i].length&nbsp;== 2 ``
*   <code>x<sub>i</sub> != y<sub>i</sub></code>
*   <code>0 &lt;= x<sub>i</sub>, y<sub>i</sub>&nbsp;&lt;= n - 1</code>
*   Each person is contained in __exactly one__ pair.