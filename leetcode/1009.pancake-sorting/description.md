Given an array of integers `` arr ``, sort the array by performing a series of __pancake flips__.

In one pancake flip we do the following steps:

*   Choose an integer `` k `` where `` 1 &lt;= k &lt;= arr.length ``.
*   Reverse the sub-array `` arr[0...k-1] `` (__0-indexed__).

For example, if `` arr = [3,2,1,4] `` and we performed a pancake flip choosing `` k = 3 ``, we reverse the sub-array `` [3,2,1] ``, so <code>arr = [<u>1</u>,<u>2</u>,<u>3</u>,4]</code> after the pancake flip at `` k = 3 ``.

Return _an array of the _`` k ``_-values corresponding to a sequence of pancake flips that sort _`` arr ``. Any valid answer that sorts the array within `` 10 * arr.length `` flips will be judged as correct.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [3,2,4,1]
<strong>Output:</strong> [4,2,4,3]
<strong>Explanation: </strong>
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: arr = [3, 2, 4, 1]
After 1st flip (k = 4): arr = [<u>1</u>, <u>4</u>, <u>2</u>, <u>3</u>]
After 2nd flip (k = 2): arr = [<u>4</u>, <u>1</u>, 2, 3]
After 3rd flip (k = 4): arr = [<u>3</u>, <u>2</u>, <u>1</u>, <u>4</u>]
After 4th flip (k = 3): arr = [<u>1</u>, <u>2</u>, <u>3</u>, 4], which is sorted.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,2,3]
<strong>Output:</strong> []
<strong>Explanation: </strong>The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 100 ``
*   `` 1 &lt;= arr[i] &lt;= arr.length ``
*   All integers in `` arr `` are unique (i.e. `` arr `` is a permutation of the integers from `` 1 `` to `` arr.length ``).