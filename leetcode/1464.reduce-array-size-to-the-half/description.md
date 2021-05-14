Given an array `` arr ``.&nbsp; You can choose a set of integers and remove all the occurrences of these integers in the array.

Return _the minimum size of the set_ so that __at least__ half of the integers of the array are removed.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [3,3,3,3,5,5,5,2,2,7]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [7,7,7,7,7,7]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only possible set you can choose is {7}. This will make the new array empty.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [1,9]
<strong>Output:</strong> 1
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [1000,1000,3,7]
<strong>Output:</strong> 1
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> arr = [1,2,3,4,5,6,7,8,9,10]
<strong>Output:</strong> 5
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 10^5 ``
*   `` arr.length `` is even.
*   `` 1 &lt;= arr[i] &lt;= 10^5 ``