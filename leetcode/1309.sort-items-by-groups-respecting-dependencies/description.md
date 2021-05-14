There are&nbsp;`` n ``&nbsp;items each&nbsp;belonging to zero or one of&nbsp;`` m ``&nbsp;groups where `` group[i] ``&nbsp;is the group that the `` i ``-th item belongs to and it's equal to `` -1 ``&nbsp;if the `` i ``-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

*   The items that belong to the same group are next to each other in the sorted list.
*   There are some&nbsp;relations&nbsp;between these items where&nbsp;`` beforeItems[i] ``&nbsp;is a list containing all the items that should come before the&nbsp;`` i ``-th item in the sorted array (to the left of the&nbsp;`` i ``-th item).

Return any solution if there is more than one solution and return an __empty list__&nbsp;if there is no solution.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/11/1359_ex1.png" style="width: 191px; height: 181px;"/></strong>

<pre>
<strong>Input:</strong> n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
<strong>Output:</strong> [6,3,4,1,5,2,0,7]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
<strong>Output:</strong> []
<strong>Explanation:</strong>&nbsp;This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= m &lt;= n &lt;= 3 * 10<sup>4</sup></code>
*   `` group.length == beforeItems.length == n ``
*   `` -1 &lt;= group[i] &lt;= m - 1 ``
*   `` 0 &lt;= beforeItems[i].length &lt;= n - 1 ``
*   `` 0 &lt;= beforeItems[i][j] &lt;= n - 1 ``
*   `` i != beforeItems[i][j] ``
*   `` beforeItems[i]&nbsp; ``does not contain&nbsp;duplicates elements.