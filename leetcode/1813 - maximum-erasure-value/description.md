You are given an array of positive integers `` nums `` and want to erase a subarray containing&nbsp;__unique elements__. The __score__ you get by erasing the subarray is equal to the __sum__ of its elements.

Return _the __maximum score__ you can get by erasing __exactly one__ subarray._

An array `` b `` is called to be a <span class="tex-font-style-it">subarray</span> of `` a `` if it forms a contiguous subsequence of `` a ``, that is, if it is equal to `` a[l],a[l+1],...,a[r] `` for some `` (l,r) ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [4,2,4,5,6]
<strong>Output:</strong> 17
<strong>Explanation:</strong> The optimal subarray here is [2,4,5,6].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [5,2,1,2,5,2,1,2,5]
<strong>Output:</strong> 8
<strong>Explanation:</strong> The optimal subarray here is [5,2,1] or [1,2,5].
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code>