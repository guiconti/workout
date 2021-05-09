You are given an array `` target `` that consists of __distinct__ integers and another integer array `` arr `` that __can__ have duplicates.

In one operation, you can insert any integer at any position in `` arr ``. For example, if `` arr = [1,4,1,2] ``, you can add `` 3 `` in the middle and make it <code>[1,4,<u>3</u>,1,2]</code>. Note that you can insert the integer at the very beginning or end of the array.

Return _the __minimum__ number of operations needed to make _`` target ``_ a __subsequence__ of _`` arr ``_._

A __subsequence__ of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, `` [2,7,4] `` is a subsequence of <code>[4,<u>2</u>,3,<u>7</u>,2,1,<u>4</u>]</code> (the underlined elements), while `` [2,4,2] `` is not.

&nbsp;

__Example 1:__

<strong>Input:</strong> target = [5,1,3], arr = [9,4,2,3,4]
    <strong>Output:</strong> 2
    <strong>Explanation:</strong> You can add 5 and 1 in such a way that makes <code>arr</code> = [<u>5</u>,9,4,<u>1</u>,2,3,4], then target will be a subsequence of <code>arr</code>.

__Example 2:__

<strong>Input:</strong> target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
    <strong>Output:</strong> 3

&nbsp;

__Constraints:__

*   <code>1 &lt;= target.length, arr.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= target[i], arr[i] &lt;= 10<sup>9</sup></code>
*   `` target `` contains no duplicates.