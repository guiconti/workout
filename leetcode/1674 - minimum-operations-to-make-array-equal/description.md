You have an array `` arr `` of length `` n `` where `` arr[i] = (2 * i) + 1 `` for all valid values of `` i `` (i.e. `` 0 &lt;= i &lt; n ``).

In one operation, you can select two indices `` x ``&nbsp;and `` y `` where `` 0 &lt;= x, y &lt; n `` and subtract `` 1 `` from `` arr[x] `` and add `` 1 `` to `` arr[y] ``&nbsp;(i.e. perform `` arr[x] -=1&nbsp; ``and `` arr[y] += 1 ``).&nbsp;The goal is to make all the elements of the array __equal__. It is __guaranteed__ that all the elements of the array can be made equal using some operations.

Given an integer `` n ``, the length of the array. Return _the minimum number of operations_ needed to make&nbsp;all the elements of arr equal.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> 9
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 10^4 ``