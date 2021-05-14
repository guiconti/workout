Given an array `` target `` and&nbsp;an integer `` n ``. In each iteration, you will read a number from &nbsp;`` list = {1,2,3..., n} ``.

Build the `` target ``&nbsp;array&nbsp;using the following operations:

*   __Push__: Read a new element from the beginning&nbsp;`` list ``, and push it in the array.
*   __Pop__: delete the last element of&nbsp;the array.
*   If the target array is already&nbsp;built, stop reading more elements.

Return the operations to build the target array. You are guaranteed that the answer is unique.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> target = [1,3], n = 3
<strong>Output:</strong> ["Push","Push","Pop","Push"]
<strong>Explanation: 
</strong>Read number 1 and automatically push in the array -&gt; [1]
Read number 2 and automatically push in the array then Pop it -&gt; [1]
Read number 3 and automatically push in the array -&gt; [1,3]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> target = [1,2,3], n = 3
<strong>Output:</strong> ["Push","Push","Push"]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> target = [1,2], n = 4
<strong>Output:</strong> ["Push","Push"]
<strong>Explanation: </strong>You only need to read the first 2 numbers and stop.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> target = [2,3,4], n = 4
<strong>Output:</strong> ["Push","Pop","Push","Push","Push"]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= target.length &lt;= 100 ``
*   `` 1 &lt;= target[i]&nbsp;&lt;= n ``
*   `` 1 &lt;= n &lt;= 100 ``
*   `` target `` is strictly&nbsp;increasing.