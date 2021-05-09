Given an array `` nums `` with `` n `` objects colored red, white, or blue, sort them __<a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> __so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `` 0 ``, `` 1 ``, and `` 2 `` to represent the color red, white, and blue, respectively.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [2,0,2,1,1,0]
<strong>Output:</strong> [0,0,1,1,2,2]
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [2,0,1]
<strong>Output:</strong> [0,1,2]
</pre>

__Example 3:__

<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>

__Example 4:__

<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> [1]
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   `` 1 &lt;= n &lt;= 300 ``
*   `` nums[i] `` is `` 0 ``, `` 1 ``, or `` 2 ``.

&nbsp;

__Follow up:__

*   Could you solve this problem without using the library's sort function?
*   Could you come up with a one-pass algorithm using only `` O(1) `` constant space?