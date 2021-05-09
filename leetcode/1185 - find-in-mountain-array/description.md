_(This problem is an&nbsp;__interactive problem__.)_

You may recall that an array&nbsp;`` A `` is a _mountain array_ if and only if:

*   `` A.length &gt;= 3 ``
*   There exists some&nbsp;`` i ``&nbsp;with&nbsp;`` 0 &lt; i&nbsp;&lt; A.length - 1 ``&nbsp;such that:	
    
    *   `` A[0] &lt; A[1] &lt; ... A[i-1] &lt; A[i] ``
    *   `` A[i] &gt; A[i+1] &gt; ... &gt; A[A.length - 1] ``
    
    
    

Given a mountain&nbsp;array `` mountainArr ``, return the __minimum__&nbsp;`` index `` such that `` mountainArr.get(index) == target ``.&nbsp; If such an `` index ``&nbsp;doesn't exist, return `` -1 ``.

__You can't access the mountain array directly.__&nbsp; You may only access the array using a&nbsp;`` MountainArray ``&nbsp;interface:

*   `` MountainArray.get(k) `` returns the element of the array at index `` k ``&nbsp;(0-indexed).
*   `` MountainArray.length() ``&nbsp;returns the length of the array.

Submissions making more than `` 100 `` calls to&nbsp;`` MountainArray.get ``&nbsp;will be judged _Wrong Answer_.&nbsp; Also, any solutions that attempt to circumvent the judge&nbsp;will result in disqualification.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> array = [1,2,3,4,5,3,1], target = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.</pre>

__Example 2:__

<strong>Input:</strong> array = [0,1,2,4,2,1], target = 3
    <strong>Output:</strong> -1
    <strong>Explanation:</strong> 3 does not exist in the array, so we return -1.

&nbsp;

__Constraints:__

*   `` 3 &lt;= mountain_arr.length() &lt;= 10000 ``
*   `` 0 &lt;= target &lt;= 10^9 ``
*   `` 0 &lt;= mountain_arr.get(index) &lt;=&nbsp;10^9 ``