Given `` 2n `` balls of `` k `` distinct colors. You will be given an integer array `` balls `` of size `` k `` where `` balls[i] `` is the number of balls of color `` i ``.&nbsp;

All the balls will be __shuffled uniformly at random__,&nbsp;then we will distribute the first `` n `` balls to the first box and the remaining `` n `` balls to the other box (Please read the explanation of the second example carefully).

Please note that the two boxes are considered different. For example, if we have two balls of colors `` a `` and `` b ``, and two boxes `` [] `` and `` () ``, then the distribution `` [a] (b) `` is considered different than the distribution `` [b] (a)&nbsp; ``(Please read the explanation of the first&nbsp;example carefully).

We want to _calculate the probability_ that the two boxes have the same number of distinct balls.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> balls = [1,1]
<strong>Output:</strong> 1.00000
<strong>Explanation:</strong> Only 2 ways to divide the balls equally:
- A ball of color 1 to box 1 and a ball of color 2 to box 2
- A ball of color 2 to box 1 and a ball of color 1 to box 2
In both ways, the number of distinct colors in each box is equal. The probability is 2/2 = 1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> balls = [2,1,1]
<strong>Output:</strong> 0.66667
<strong>Explanation:</strong> We have the set of balls [1, 1, 2, 3]
This set of balls will be shuffled randomly and we may have one of the 12 distinct shuffles with equale probability (i.e. 1/12):
[1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1], [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
After that we add the first two balls to the first box and the second two balls to the second box.
We can see that 8 of these 12 possible random distributions have the same number of distinct colors of balls in each box.
Probability is 8/12 = 0.66667
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> balls = [1,2,1,2]
<strong>Output:</strong> 0.60000
<strong>Explanation:</strong> The set of balls is [1, 2, 2, 3, 4, 4]. It is hard to display all the 180 possible random shuffles of this set but it is easy to check that 108 of them will have the same number of distinct colors in each box.
Probability = 108 / 180 = 0.6
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> balls = [3,2,1]
<strong>Output:</strong> 0.30000
<strong>Explanation:</strong> The set of balls is [1, 1, 1, 2, 2, 3]. It is hard to display all the 60 possible random shuffles of this set but it is easy to check that 18 of them will have the same number of distinct colors in each box.
Probability = 18 / 60 = 0.3
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> balls = [6,6,6,6,6,6]
<strong>Output:</strong> 0.90327
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= balls.length &lt;= 8 ``
*   `` 1 &lt;= balls[i] &lt;= 6 ``
*   `` sum(balls) `` is even.
*   Answers within `` 10^-5 `` of the actual value will be accepted as correct.