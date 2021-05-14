Given a string `` path ``, where `` path[i] = 'N' ``, `` 'S' ``, `` 'E' `` or `` 'W' ``, each representing moving one unit north, south, east, or west, respectively. You start at the origin `` (0, 0) `` on a 2D plane and walk on the path specified by `` path ``.

Return `` true `` _if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited_. Return `` false `` otherwise.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123929-pm.png" style="width: 400px; height: 358px;"/>

<pre>
<strong>Input:</strong> path = "NES"
<strong>Output:</strong> false 
<strong>Explanation:</strong> Notice that the path doesn't cross any point more than once.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123843-pm.png" style="width: 400px; height: 339px;"/>

<pre>
<strong>Input:</strong> path = "NESWW"
<strong>Output:</strong> true
<strong>Explanation:</strong> Notice that the path visits the origin twice.</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= path.length &lt;= 10<sup>4</sup></code>
*   `` path[i] `` is either `` 'N' ``, `` 'S' ``, `` 'E' ``, or `` 'W' ``.