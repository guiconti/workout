We have a wooden&nbsp;plank of the length `` n `` __units__. Some ants are walking on the&nbsp;plank, each ant moves with speed __1 unit per second__. Some of the ants move to the __left__, the other move to the __right__.

When two ants moving in two __different__ directions meet at some point, they change their directions and continue moving again. Assume changing directions doesn't take any additional time.

When an ant reaches __one end__ of the plank at a time `` t ``, it falls out of the plank imediately.

Given an integer `` n `` and two integer arrays `` left `` and `` right ``, the positions of the ants moving to the left and the right.&nbsp;Return _the&nbsp;moment_ when the last ant(s) fall out of the plank.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/17/ants.jpg" style="width: 450px; height: 610px;"/>

<pre>
<strong>Input:</strong> n = 4, left = [4,3], right = [0,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> In the image above:
-The ant at index 0 is named A and going to the right.
-The ant at index 1 is named B and going to the right.
-The ant at index 3 is named C and going to the left.
-The ant at index 4 is named D and going to the left.
Note that the last moment when an ant was on the plank is t = 4 second, after that it falls imediately out of the plank. (i.e. We can say that at t = 4.0000000001, there is no ants on the plank).
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/17/ants2.jpg" style="width: 639px; height: 101px;"/>

<pre>
<strong>Input:</strong> n = 7, left = [], right = [0,1,2,3,4,5,6,7]
<strong>Output:</strong> 7
<strong>Explanation:</strong> All ants are going to the right, the ant at index 0 needs 7 seconds to fall.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/17/ants3.jpg" style="width: 639px; height: 100px;"/>

<pre>
<strong>Input:</strong> n = 7, left = [0,1,2,3,4,5,6,7], right = []
<strong>Output:</strong> 7
<strong>Explanation:</strong> All ants are going to the left, the ant at index 7 needs 7 seconds to fall.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 9, left = [5], right = [4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> At t = 1 second, both ants will be at the same intial position but with different direction.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 6, left = [6], right = [0]
<strong>Output:</strong> 6
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 10^4 ``
*   `` 0 &lt;= left.length &lt;= n + 1 ``
*   `` 0 &lt;= left[i] &lt;= n ``
*   `` 0 &lt;= right.length &lt;= n + 1 ``
*   `` 0 &lt;= right[i] &lt;= n ``
*   `` 1 &lt;= left.length + right.length &lt;= n + 1 ``
*   All values of `` left `` and `` right `` are unique, and each value can appear __only in one__ of the two arrays.