There are `` n `` bulbs that are initially off. You first turn on all the bulbs, then&nbsp;you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the <code>i<sup>th</sup></code> round, you toggle every `` i `` bulb. For the <code>n<sup>th</sup></code> round, you only toggle the last bulb.

Return _the number of bulbs that are on after `` n `` rounds_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bulb.jpg" style="width: 421px; height: 321px;"/>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   <code>0 &lt;= n &lt;= 10<sup>9</sup></code>