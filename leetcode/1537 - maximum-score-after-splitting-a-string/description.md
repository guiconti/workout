Given a&nbsp;string `` s ``&nbsp;of zeros and ones, _return the maximum score after splitting the string into two __non-empty__ substrings_ (i.e. __left__ substring and __right__ substring).

The score after splitting a string is the number of __zeros__ in the __left__ substring plus the number of __ones__ in the __right__ substring.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "011101"
<strong>Output:</strong> 5 
<strong>Explanation:</strong> 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "00111"
<strong>Output:</strong> 5
<strong>Explanation:</strong> When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "1111"
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= s.length &lt;= 500 ``
*   The string `` s `` consists of characters '0' and '1' only.