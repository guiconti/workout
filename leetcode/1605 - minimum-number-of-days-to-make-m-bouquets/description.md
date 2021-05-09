Given an integer array `` bloomDay ``, an integer `` m `` and an integer `` k ``.

We need to make `` m ``&nbsp;bouquets. To make a bouquet,&nbsp;you need to use `` k `` __adjacent flowers__ from the garden.

The garden consists of `` n `` flowers, the `` ith `` flower will bloom in the `` bloomDay[i] ``&nbsp;and then can be used in&nbsp;__exactly one__ bouquet.

Return _the minimum number of days_ you need to wait to be able to make `` m `` bouquets from the garden. If it is impossible to make `` m `` bouquets return __-1__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> bloomDay = [1,10,3,10,2], m = 3, k = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> bloomDay = [1,10,3,10,2], m = 3, k = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
<strong>Output:</strong> 12
<strong>Explanation:</strong> We need 2 bouquets each should have 3 flowers.
Here's the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> bloomDay = [1000000000,1000000000], m = 1, k = 1
<strong>Output:</strong> 1000000000
<strong>Explanation:</strong> You need to wait 1000000000 days to have a flower ready for a bouquet.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
<strong>Output:</strong> 9
</pre>

&nbsp;

__Constraints:__

*   `` bloomDay.length == n ``
*   `` 1 &lt;= n &lt;= 10^5 ``
*   `` 1 &lt;= bloomDay[i] &lt;= 10^9 ``
*   `` 1 &lt;= m &lt;= 10^6 ``
*   `` 1 &lt;= k &lt;= n ``