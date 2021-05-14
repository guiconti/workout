There are several cards&nbsp;__arranged in a row__, and each card has an associated number of points&nbsp;The points are given in the integer array&nbsp;`` cardPoints ``.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly `` k `` cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array `` cardPoints `` and the integer `` k ``, return the _maximum score_ you can obtain.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> cardPoints = [1,2,3,4,5,6,1], k = 3
<strong>Output:</strong> 12
<strong>Explanation:</strong> After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> cardPoints = [2,2,2], k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> Regardless of which two cards you take, your score will always be 4.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> cardPoints = [9,7,7,9,7,7,9], k = 7
<strong>Output:</strong> 55
<strong>Explanation:</strong> You have to take all the cards. Your score is the sum of points of all cards.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> cardPoints = [1,1000,1], k = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> You cannot take the card in the middle. Your best score is 1. 
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> cardPoints = [1,79,80,1,1,1,200,1], k = 3
<strong>Output:</strong> 202
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= cardPoints.length &lt;= 10^5 ``
*   `` 1 &lt;= cardPoints[i] &lt;= 10^4 ``
*   `` 1 &lt;= k &lt;= cardPoints.length ``