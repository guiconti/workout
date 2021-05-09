Given a string `` s ``&nbsp;and an integer array `` indices `` of the __same length__.

The string `` s `` will be shuffled such that the character at the <code>i<sup>th</sup></code> position moves to&nbsp;`` indices[i] `` in the shuffled string.

Return _the shuffled string_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/09/q1.jpg" style="width: 321px; height: 243px;"/>

<strong>Input:</strong> s = "codeleet", indices = [4,5,6,7,0,2,1,3]
    <strong>Output:</strong> "leetcode"
    <strong>Explanation:</strong> As shown, "codeleet" becomes "leetcode" after shuffling.

__Example 2:__

<strong>Input:</strong> s = "abc", indices = [0,1,2]
    <strong>Output:</strong> "abc"
    <strong>Explanation:</strong> After shuffling, each character remains in its position.

__Example 3:__

<strong>Input:</strong> s = "aiohn", indices = [3,1,4,2,0]
    <strong>Output:</strong> "nihao"

__Example 4:__

<strong>Input:</strong> s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
    <strong>Output:</strong> "arigatou"

__Example 5:__

<strong>Input:</strong> s = "art", indices = [1,0,2]
    <strong>Output:</strong> "rat"

&nbsp;

__Constraints:__

*   `` s.length == indices.length == n ``
*   `` 1 &lt;= n &lt;= 100 ``
*   `` s `` contains only lower-case English letters.
*   `` 0 &lt;= indices[i] &lt;&nbsp;n ``
*   All values of `` indices `` are unique (i.e. `` indices `` is a permutation of the integers from `` 0 `` to `` n - 1 ``).