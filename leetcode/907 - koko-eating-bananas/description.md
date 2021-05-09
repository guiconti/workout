Koko loves to eat bananas. There are `` n `` piles of bananas, the <code>i<sup>th</sup></code> pile has `` piles[i] `` bananas. The guards have gone and will come back in `` h `` hours.

Koko can decide her bananas-per-hour eating speed of `` k ``. Each hour, she chooses some pile of bananas and eats `` k `` bananas from that pile. If the pile has less than `` k `` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return _the minimum integer_ `` k `` _such that she can eat all the bananas within_ `` h `` _hours_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> piles = [3,6,7,11], h = 8
<strong>Output:</strong> 4
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> piles = [30,11,23,4,20], h = 5
<strong>Output:</strong> 30
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> piles = [30,11,23,4,20], h = 6
<strong>Output:</strong> 23
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= piles.length &lt;= 10<sup>4</sup></code>
*   <code>piles.length &lt;= h &lt;= 10<sup>9</sup></code>
*   <code>1 &lt;= piles[i] &lt;= 10<sup>9</sup></code>