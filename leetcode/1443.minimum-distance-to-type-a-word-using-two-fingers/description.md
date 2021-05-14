<img alt="" src="https://assets.leetcode.com/uploads/2020/01/02/leetcode_keyboard.png" style="width: 417px; height: 250px;"/>

You have a keyboard layout as shown above in the XY plane, where each English uppercase letter is located at some coordinate, for example, the letter __A__ is located at coordinate __(0,0)__, the letter __B__ is located at coordinate __(0,1)__, the letter __P__ is located at coordinate __(2,3)__ and the letter __Z__ is located at coordinate __(4,1)__.

Given the string `` word ``, return the minimum total distance to type such string using only two&nbsp;fingers. The distance between coordinates __(x<sub>1</sub>,y<sub>1</sub>)__ and __(x<sub>2</sub>,y<sub>2</sub>)__ is __|x<sub>1</sub> - x<sub>2</sub>| + |y<sub>1</sub> - y<sub>2</sub>|__.&nbsp;

Note that the initial positions of your two&nbsp;fingers are considered free so don't count towards your total distance, also your two&nbsp;fingers do not have to start at the first letter or the first two&nbsp;letters.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> word = "CAKE"
<strong>Output:</strong> 3
<strong>Explanation: 
</strong>Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on letter 'C' -&gt; cost = 0 
Finger 1 on letter 'A' -&gt; cost = Distance from letter 'C' to letter 'A' = 2 
Finger 2 on letter 'K' -&gt; cost = 0 
Finger 2 on letter 'E' -&gt; cost = Distance from letter 'K' to letter 'E' = 1 
Total distance = 3
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> word = "HAPPY"
<strong>Output:</strong> 6
<strong>Explanation: </strong>
Using two fingers, one optimal way to type "HAPPY" is:
Finger 1 on letter 'H' -&gt; cost = 0
Finger 1 on letter 'A' -&gt; cost = Distance from letter 'H' to letter 'A' = 2
Finger 2 on letter 'P' -&gt; cost = 0
Finger 2 on letter 'P' -&gt; cost = Distance from letter 'P' to letter 'P' = 0
Finger 1 on letter 'Y' -&gt; cost = Distance from letter 'A' to letter 'Y' = 4
Total distance = 6
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> word = "NEW"
<strong>Output:</strong> 3
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> word = "YEAR"
<strong>Output:</strong> 7
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= word.length &lt;= 300 ``
*   Each <code data-stringify-type="code">word\[i\]</code>&nbsp;is an English uppercase letter.