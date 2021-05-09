Given a rectangular cake with height `` h `` and width `` w ``, and two arrays of integers `` horizontalCuts `` and `` verticalCuts `` where `` horizontalCuts[i] `` is the distance from the top of the rectangular cake to the `` ith `` horizontal cut&nbsp;and similarly, `` verticalCuts[j] `` is the distance from the&nbsp;left of the rectangular cake to the `` jth ``&nbsp;vertical cut.

_Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays `` horizontalCuts `` and `` verticalCuts ``.&nbsp;_Since the answer can be a huge number, return this modulo 10^9 + 7.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/05/14/leetcode_max_area_2.png" style="width: 300px; height: 320px;"/>

<pre>
<strong>Input:</strong> h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
<strong>Output:</strong> 4 
<strong>Explanation:</strong> The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/05/14/leetcode_max_area_3.png" style="width: 300px; height: 320px;"/></strong>

<pre>
<strong>Input:</strong> h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
<strong>Output:</strong> 9
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= h,&nbsp;w &lt;= 10^9 ``
*   `` 1 &lt;=&nbsp;horizontalCuts.length &lt;&nbsp;min(h, 10^5) ``
*   `` 1 &lt;=&nbsp;verticalCuts.length &lt; min(w, 10^5) ``
*   `` 1 &lt;=&nbsp;horizontalCuts[i] &lt; h ``
*   `` 1 &lt;=&nbsp;verticalCuts[i] &lt; w ``
*   It is guaranteed that all elements in&nbsp;`` horizontalCuts ``&nbsp;are distinct.
*   It is guaranteed that all elements in `` verticalCuts ``&nbsp;are distinct.