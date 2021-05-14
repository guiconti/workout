The string `` "PAYPALISHIRING" `` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

<pre>
P   A   H   N
A P L S I I G
Y   I   R
</pre>

And then read line by line: `` "PAHNAPLSIIGYIR" ``

Write the code that will take a string and make this conversion given a number of rows:

<pre>
string convert(string s, int numRows);
</pre>

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "PAYPALISHIRING", numRows = 3
<strong>Output:</strong> "PAHNAPLSIIGYIR"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "PAYPALISHIRING", numRows = 4
<strong>Output:</strong> "PINALSIGYAHRPI"
<strong>Explanation:</strong>
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "A", numRows = 1
<strong>Output:</strong> "A"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 1000 ``
*   `` s `` consists of English letters (lower-case and upper-case), `` ',' `` and `` '.' ``.
*   `` 1 &lt;= numRows &lt;= 1000 ``