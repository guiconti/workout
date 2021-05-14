A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in __non-decreasing order__ by height. Let this ordering be represented by the integer array `` expected `` where `` expected[i] `` is the expected height of the <code>i<sup>th</sup></code> student in line.

You are given an integer array `` heights `` representing the __current order__ that the students are standing in. Each `` heights[i] `` is the height of the <code>i<sup>th</sup></code> student in line (__0-indexed__).

Return _the __number of indices__ where _`` heights[i] != expected[i] ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> heights = [1,1,4,2,1,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
heights:  [1,1,<u>4</u>,2,<u>1</u>,<u>3</u>]
expected: [1,1,<u>1</u>,2,<u>3</u>,<u>4</u>]
Indices 2, 4, and 5 do not match.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> heights = [5,1,2,3,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong>
heights:  [<u>5</u>,<u>1</u>,<u>2</u>,<u>3</u>,<u>4</u>]
expected: [<u>1</u>,<u>2</u>,<u>3</u>,<u>4</u>,<u>5</u>]
All indices do not match.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> heights = [1,2,3,4,5]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= heights.length &lt;= 100 ``
*   `` 1 &lt;= heights[i] &lt;= 100 ``