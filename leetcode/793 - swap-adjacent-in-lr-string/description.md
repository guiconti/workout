In a string composed of `` 'L' ``, `` 'R' ``, and `` 'X' `` characters, like `` "RXXLRXRXL" ``, a move consists of either replacing one occurrence of `` "XL" `` with `` "LX" ``, or replacing one occurrence of `` "RX" `` with `` "XR" ``. Given the starting string `` start `` and the ending string `` end ``, return `` True `` if and only if there exists a sequence of moves to transform one string to the other.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> start = "RXXLRXRXL", end = "XRLXXRRLX"
<strong>Output:</strong> true
<strong>Explanation:</strong> We can transform start to end following these steps:
RXXLRXRXL -&gt;
XRXLRXRXL -&gt;
XRLXRXRXL -&gt;
XRLXXRRXL -&gt;
XRLXXRRLX
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> start = "X", end = "L"
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> start = "LLR", end = "RRL"
<strong>Output:</strong> false
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> start = "XL", end = "LX"
<strong>Output:</strong> true
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> start = "XLLR", end = "LXLX"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= start.length&nbsp;&lt;= 10<sup>4</sup></code>
*   `` start.length == end.length ``
*   Both `` start `` and `` end `` will only consist of characters in `` 'L' ``, `` 'R' ``, and&nbsp;`` 'X' ``.