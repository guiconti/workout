You are given an array of positive integers `` arr ``. Perform some operations (possibly none) on `` arr `` so that it satisfies these conditions:

*   The value of the __first__ element in `` arr `` must be `` 1 ``.
*   The absolute difference between any 2 adjacent elements must be __less than or equal to __`` 1 ``. In other words, `` abs(arr[i] - arr[i - 1]) &lt;= 1 `` for each `` i `` where `` 1 &lt;= i &lt; arr.length `` (__0-indexed__). `` abs(x) `` is the absolute value of `` x ``.

There are 2 types of operations that you can perform any number of times:

*   __Decrease__ the value of any element of `` arr `` to a __smaller positive integer__.
*   __Rearrange__ the elements of `` arr `` to be in any order.

Return _the __maximum__ possible value of an element in _`` arr ``_ after performing the operations to satisfy the conditions_.

&nbsp;

__Example 1:__

<strong>Input:</strong> arr = [2,2,1,2,1]
    <strong>Output:</strong> 2
    <strong>Explanation:</strong> 
    We can satisfy the conditions by rearranging arr so it becomes <code>[1,2,2,2,1]</code>.
    The largest element in <code>arr</code> is 2.

__Example 2:__

<strong>Input:</strong> arr = [100,1,1000]
    <strong>Output:</strong> 3
    <strong>Explanation:</strong> 
    One possible way to satisfy the conditions is by doing the following:
    1. Rearrange arr so it becomes <code>[1,100,1000]</code>.
    2. Decrease the value of the second element to 2.
    3. Decrease the value of the third element to 3.
    Now <code>arr = [1,2,3], which </code>satisfies the conditions.
    The largest element in <code>arr is 3.</code>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [1,2,3,4,5]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The array already satisfies the conditions, and the largest element is 5.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= arr[i] &lt;= 10<sup>9</sup></code>