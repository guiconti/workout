You are given two strings&nbsp;`` s1 ``&nbsp;and&nbsp;`` s2 ``&nbsp;of equal length&nbsp;consisting of letters `` "x" `` and `` "y" `` __only__. Your task is to&nbsp;make these two strings equal to each other. You can swap any two characters that belong to __different__ strings,&nbsp;which means: swap `` s1[i] `` and `` s2[j] ``.

Return&nbsp;the minimum number of swaps required&nbsp;to make&nbsp;`` s1 ``&nbsp;and `` s2 `` equal, or return&nbsp;`` -1 ``&nbsp;if it is&nbsp;impossible to do so.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s1 = "xx", s2 = "yy"
<strong>Output:</strong> 1
<strong>Explanation: 
</strong>Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".</pre>

__Example 2:&nbsp;__

<pre>
<strong>Input:</strong> s1 = "xy", s2 = "yx"
<strong>Output:</strong> 2
<strong>Explanation: 
</strong>Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s1 = "xx", s2 = "xy"
<strong>Output:</strong> -1
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s1.length, s2.length &lt;= 1000 ``
*   `` s1, s2 ``&nbsp;only contain `` 'x' `` or `` 'y' ``.