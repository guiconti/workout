Given an array _nums_ and a value `` val ``, remove all instances of that value <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">__in-place__</a> and return the new length.

Do not allocate extra space for another array, you must do this by __modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a>__ with `` O(1) `` extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

__Clarification:__

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by __reference__, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

<pre>
// <strong>nums</strong> is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to <strong>nums</strong> in your function would be known by the caller.
// using the length returned by your function, it prints the first <strong>len</strong> elements.
for (int i = 0; i &lt; len; i++) {
&nbsp; &nbsp; print(nums[i]);
}</pre>

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,2,2,3], val = 3
<strong>Output:</strong> 2, nums = [2,2]
<strong>Explanation:</strong> Your function should return length = <strong>2</strong>, with the first two elements of <em>nums</em> being <strong>2</strong>.
It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.
</pre>

__Example 2:__

<strong>Input:</strong> nums = [0,1,2,2,3,0,4,2], val = 2
    <strong>Output:</strong> 5, nums = [0,1,4,0,3]
    <strong>Explanation:</strong> Your function should return length = <strong>5</strong>, with the first five elements of <em><code>nums</code></em> containing <strong><code>0</code></strong>, <strong><code>1</code></strong>, <strong><code>3</code></strong>, <strong><code>0</code></strong>, and <strong>4</strong>. Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.

&nbsp;

__Constraints:__

*   `` 0 &lt;= nums.length &lt;= 100 ``
*   `` 0 &lt;= nums[i] &lt;= 50 ``
*   `` 0 &lt;= val &lt;= 100 ``