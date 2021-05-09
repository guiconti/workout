Given two numbers, `` hour `` and `` minutes ``. Return the smaller angle (in degrees) formed between the `` hour `` and the `` minute `` hand.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/12/26/sample_1_1673.png" style="width: 230px; height: 225px;"/>

<pre>
<strong>Input:</strong> hour = 12, minutes = 30
<strong>Output:</strong> 165
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/12/26/sample_2_1673.png" style="width: 230px; height: 225px;"/>

<pre>
<strong>Input:</strong> hour = 3, minutes = 30
<strong>Output:</strong> 75
</pre>

__Example 3:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/12/26/sample_3_1673.png" style="width: 230px; height: 225px;"/></strong>

<pre>
<strong>Input:</strong> hour = 3, minutes = 15
<strong>Output:</strong> 7.5
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> hour = 4, minutes = 50
<strong>Output:</strong> 155
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> hour = 12, minutes = 0
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= hour &lt;= 12 ``
*   `` 0 &lt;= minutes &lt;= 59 ``
*   Answers within&nbsp;`` 10^-5 ``&nbsp;of the actual value will be accepted as correct.