Given an integer array `` nums `` and an integer `` k ``, return _the_ `` k `` _most frequent elements_. You may return the answer in __any order__.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [1,1,1,2,2,3], k = 2
<strong>Output:</strong> [1,2]
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   `` k `` is in the range `` [1, the number of unique elements in the array] ``.
*   It is __guaranteed__ that the answer is __unique__.

&nbsp;

__Follow up:__ Your algorithm's time complexity must be better than `` O(n log n) ``, where n is the array's size.