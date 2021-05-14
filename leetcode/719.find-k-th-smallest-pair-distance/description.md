Given an integer array, return the k-th smallest __distance__ among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B. 

__Example 1:__  

<pre>
<b>Input:</b>
nums = [1,3,1]
k = 1
<b>Output: 0</b> 
<b>Explanation:</b>
Here are all the pairs:
(1,3) -&gt; 2
(1,1) -&gt; 0
(3,1) -&gt; 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
</pre>

__Note:__  

1.   `` 2 &lt;= len(nums) &lt;= 10000 ``.
2.   `` 0 &lt;= nums[i] &lt; 1000000 ``.
3.   `` 1 &lt;= k &lt;= len(nums) * (len(nums) - 1) / 2 ``.