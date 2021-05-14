There are `` n `` people&nbsp;that are split into some unknown number of groups. Each person is labeled with a&nbsp;__unique ID__&nbsp;from&nbsp;`` 0 ``&nbsp;to&nbsp;`` n - 1 ``.

You are given an integer array&nbsp;`` groupSizes ``, where `` groupSizes[i] ``&nbsp;is the size of the group that person&nbsp;`` i ``&nbsp;is in. For example, if&nbsp;`` groupSizes[1] = 3 ``, then&nbsp;person&nbsp;`` 1 ``&nbsp;must be in a&nbsp;group of size&nbsp;`` 3 ``.

Return&nbsp;_a list of groups&nbsp;such that&nbsp;each person&nbsp;`` i ``&nbsp;is in a group of size&nbsp;`` groupSizes[i] ``_.

Each person should&nbsp;appear in&nbsp;__exactly one group__,&nbsp;and every person must be in a group. If there are&nbsp;multiple answers, __return any of them__. It is __guaranteed__ that there will be __at least one__ valid solution for the given input.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> groupSizes = [3,3,3,3,3,1,3]
<strong>Output:</strong> [[5],[0,1,2],[3,4,6]]
<b>Explanation:</b> 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> groupSizes = [2,1,3,3,3,2]
<strong>Output:</strong> [[1],[0,5],[2,3,4]]
</pre>

&nbsp;

__Constraints:__

*   `` groupSizes.length == n ``
*   `` 1 &lt;= n&nbsp;&lt;= 500 ``
*   `` 1 &lt;=&nbsp;groupSizes[i] &lt;= n ``