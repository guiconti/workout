A delivery company wants to build a new service centre in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new centre in a position such that __the sum of the euclidean distances to all customers is minimum__.

Given an array `` positions `` where <code>positions[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> is the position of the `` ith `` customer on the map, return _the minimum sum of the euclidean distances_ to all customers.

In other words, you need to choose the position of the service centre <code>[x<sub>centre</sub>, y<sub>centre</sub>]</code> such that the following formula is minimized:

![](https://assets.leetcode.com/uploads/2020/06/25/q4_edited.jpg)

Answers within&nbsp;`` 10^-5 ``&nbsp;of the actual value will be accepted.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/25/q4_e1.jpg" style="width: 377px; height: 362px;"/>

<pre>
<strong>Input:</strong> positions = [[0,1],[1,0],[1,2],[2,1]]
<strong>Output:</strong> 4.00000
<strong>Explanation:</strong> As shown, you can see that choosing [x<sub>centre</sub>, y<sub>centre</sub>] = [1, 1] will make the distance to each customer = 1, the sum of all distances is 4 which is the minimum possible we can achieve.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/25/q4_e3.jpg" style="width: 419px; height: 419px;"/>

<pre>
<strong>Input:</strong> positions = [[1,1],[3,3]]
<strong>Output:</strong> 2.82843
<strong>Explanation:</strong> The minimum possible sum of distances = sqrt(2) + sqrt(2) = 2.82843
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> positions = [[1,1]]
<strong>Output:</strong> 0.00000
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> positions = [[1,1],[0,0],[2,0]]
<strong>Output:</strong> 2.73205
<strong>Explanation:</strong> At the first glance, you may think that locating the centre at [1, 0] will achieve the minimum sum, but locating it at [1, 0] will make the sum of distances = 3.
Try to locate the centre at [1.0, 0.5773502711] you will see that the sum of distances is 2.73205.
Be careful with the precision!
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
<strong>Output:</strong> 32.94036
<strong>Explanation:</strong> You can use [4.3460852395, 4.9813795505] as the position of the centre.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;=&nbsp;positions.length &lt;= 50 ``
*   `` positions[i].length == 2 ``
*   `` 0 &lt;=&nbsp;positions[i][0],&nbsp;positions[i][1] &lt;= 100 ``