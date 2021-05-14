The chess knight has a __unique movement__,&nbsp;it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an __L__). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/18/chess.jpg" style="width: 402px; height: 402px;"/>

We have a chess knight and a phone pad as shown below, the knight __can only stand on a numeric cell__&nbsp;(i.e. blue cell).

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/18/phone.jpg" style="width: 242px; height: 322px;"/>

Given an integer `` n ``, return how many distinct phone numbers of length `` n `` we can dial.

You are allowed to place the knight __on any numeric cell__ initially and then you should perform `` n - 1 `` jumps to dial a number of length `` n ``. All jumps should be __valid__ knight jumps.

As the answer may be very large, __return the answer modulo__ <code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 10
<strong>Explanation:</strong> We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 20
<strong>Explanation:</strong> All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 46
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 104
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 3131
<strong>Output:</strong> 136006598
<strong>Explanation:</strong> Please take care of the mod.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 5000 ``