Today, the bookstore owner has a store open for `` customers.length `` minutes.&nbsp; Every minute, some number of customers (`` customers[i] ``) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.&nbsp; If the bookstore owner is grumpy on the i-th minute, `` grumpy[i] = 1 ``, otherwise `` grumpy[i] = 0 ``.&nbsp; When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves&nbsp;not grumpy for `` X ``&nbsp;minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
<strong>Output: </strong>16
<strong>Explanation:</strong>&nbsp;The bookstore owner keeps themselves&nbsp;not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
</pre>

&nbsp;

__Note:__

*   `` 1 &lt;= X &lt;=&nbsp;customers.length ==&nbsp;grumpy.length &lt;= 20000 ``
*   `` 0 &lt;=&nbsp;customers[i] &lt;= 1000 ``
*   `` 0 &lt;=&nbsp;grumpy[i] &lt;= 1 ``