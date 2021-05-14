You are given an array `` nums `` of `` n `` positive integers.

You can perform two types of operations on any element of the array any number of times:

*   If the element is __even__, __divide__ it by `` 2 ``.	
    
    *   For example, if the array is `` [1,2,3,4] ``, then you can do this operation on the last element, and the array will be <code>[1,2,3,<u>2</u>].</code>
    
    
    
*   If the element is __odd__, __multiply__ it by `` 2 ``.	
    
    *   For example, if the array is `` [1,2,3,4] ``, then you can do this operation on the first element, and the array will be <code>[<u>2</u>,2,3,4].</code>
    
    
    

The __deviation__ of the array is the __maximum difference__ between any two elements in the array.

Return _the __minimum deviation__ the array can have after performing some number of operations._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 1
<strong>Explanation:</strong> You can transform the array to [1,2,3,<u>2</u>], then to [<u>2</u>,2,3,2], then the deviation will be 3 - 2 = 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [4,1,5,20,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You can transform the array after two operations to [4,<u>2</u>,5,<u>5</u>,3], then the deviation will be 5 - 2 = 3.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [2,10,8]
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   <code>2 &lt;= n &lt;= 10<sup><span style="font-size: 10.8333px;">5</span></sup></code>
*   <code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code>