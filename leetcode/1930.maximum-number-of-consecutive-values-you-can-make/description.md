You are given an integer array `` coins `` of length `` n `` which represents the `` n `` coins that you own. The value of the <code>i<sup>th</sup></code> coin is `` coins[i] ``. You can __make__ some value `` x `` if you can choose some of your `` n `` coins such that their values sum up to `` x ``.

Return the _maximum number of consecutive integer values that you __can__ __make__ with your coins __starting__ from and __including__ _`` 0 ``.

Note that you may have multiple coins of the same value.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> coins = [1,3]
<strong>Output:</strong> 2
<strong>Explanation: </strong>You can make the following values:
- 0: take []
- 1: take [1]
You can make 2 consecutive integer values starting from 0.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> coins = [1,1,1,4]
<strong>Output:</strong> 8
<strong>Explanation: </strong>You can make the following values:
- 0: take []
- 1: take [1]
- 2: take [1,1]
- 3: take [1,1,1]
- 4: take [4]
- 5: take [4,1]
- 6: take [4,1,1]
- 7: take [4,1,1,1]
You can make 8 consecutive integer values starting from 0.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,4,10,3,1]
<strong>Output:</strong> 20</pre>

&nbsp;

__Constraints:__

*   `` coins.length == n ``
*   <code>1 &lt;= n &lt;= 4 * 10<sup>4</sup></code>
*   <code>1 &lt;= coins[i] &lt;= 4 * 10<sup>4</sup></code>