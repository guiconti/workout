The __median__ is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

*   For examples, if <code>arr = [2,<u>3</u>,4]</code>, the median is `` 3 ``.
*   For examples, if <code>arr = [1,<u>2,3</u>,4]</code>, the median is `` (2 + 3) / 2 = 2.5 ``.

You are given an integer array `` nums `` and an integer `` k ``. There is a sliding window of size `` k `` which is moving from the very left of the array to the very right. You can only see the `` k `` numbers in the window. Each time the sliding window moves right by one position.

Return _the median array for each window in the original array_. Answers within <code>10<sup>-5</sup></code> of the actual value will be accepted.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,3,-1,-3,5,3,6,7], k = 3
<strong>Output:</strong> [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
<strong>Explanation:</strong> 
Window position                Median
---------------                -----
[<strong>1  3  -1</strong>] -3  5  3  6  7        1
 1 [<strong>3  -1  -3</strong>] 5  3  6  7       -1
 1  3 [<strong>-1  -3  5</strong>] 3  6  7       -1
 1  3  -1 [<strong>-3  5  3</strong>] 6  7        3
 1  3  -1  -3 [<strong>5  3  6</strong>] 7        5
 1  3  -1  -3  5 [<strong>3  6  7</strong>]       6
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4,2,3,1,4,2], k = 3
<strong>Output:</strong> [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>