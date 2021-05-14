Alice and Bob continue their&nbsp;games with piles of stones.&nbsp; There are a number of&nbsp;piles&nbsp;__arranged in a row__, and each pile has a positive integer number of stones&nbsp;`` piles[i] ``.&nbsp; The objective of the game is to end with the most&nbsp;stones.&nbsp;

Alice&nbsp;and Bob take turns, with Alice starting first.&nbsp; Initially, `` M = 1 ``.

On each player's turn, that player&nbsp;can take __all the stones__ in the __first__ `` X `` remaining piles, where `` 1 &lt;= X &lt;= 2M ``.&nbsp; Then, we set&nbsp;`` M = max(M, X) ``.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice&nbsp;can get.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> piles = [2,7,9,4,4]
<strong>Output:</strong> 10
<strong>Explanation:</strong>  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> piles = [1,2,3,4,5,100]
<strong>Output:</strong> 104
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= piles.length &lt;= 100 ``
*   <code>1 &lt;= piles[i]&nbsp;&lt;= 10<sup>4</sup></code>