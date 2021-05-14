Given a sorted array _nums_, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">__in-place__</a> such that duplicates appeared at most&nbsp;_twice_ and return the new length.

Do not allocate extra space for another array; you must do this by __modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a>__ with O(1) extra memory.

__Clarification:__

Confused why the returned value is an integer, but your answer is an array?

Note that the input array is passed in by __reference__, which means a modification to the input array will be known to the caller.

Internally you can think of this:

<pre>
// <strong>nums</strong> is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to <strong>nums</strong> in your function would be known by the caller.
// using the length returned by your function, it prints the first <strong>len</strong> elements.
for (int i = 0; i &lt; len; i++) {
&nbsp; &nbsp; print(nums[i]);
}
</pre>

&nbsp;

__Example 1:__

<strong>Input:</strong> nums = [1,1,1,2,2,3]
    <strong>Output:</strong> 5, nums = [1,1,2,2,3]
    <strong>Explanation:</strong> Your function should return length = <strong>5</strong>, with the first five elements of <em><code>nums</code></em> being <strong><code>1, 1, 2, 2</code></strong> and <strong>3</strong> respectively. It doesn't matter what you leave beyond the returned length.

__Example 2:__

<strong>Input:</strong> nums = [0,0,1,1,1,1,2,3,3]
    <strong>Output:</strong> 7, nums = [0,0,1,1,2,3,3]
    <strong>Explanation:</strong> Your function should return length = <strong>7</strong>, with the first seven elements of <em><code>nums</code></em> being modified to <strong><code>0</code></strong>, <strong>0</strong>, <strong>1</strong>, <strong>1</strong>, <strong>2</strong>, <strong>3</strong> and <strong>3</strong> respectively. It doesn't matter what values are set beyond the returned length.

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>
*   `` nums ``&nbsp;is sorted in ascending order.