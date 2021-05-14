You are given an integer array `` nums `` and you have to return a new `` counts `` array. The `` counts `` array has the property where `` counts[i] `` is the number of smaller elements to the right of `` nums[i] ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [5,2,6,1]
<strong>Output:</strong> [2,1,1,0]
<strong>Explanation:</strong>
To the right of 5 there are <b>2</b> smaller elements (2 and 1).
To the right of 2 there is only <b>1</b> smaller element (1).
To the right of 6 there is <b>1</b> smaller element (1).
To the right of 1 there is <b>0</b> smaller element.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [-1]
<strong>Output:</strong> [0]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [-1,-1]
<strong>Output:</strong> [0,0]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>