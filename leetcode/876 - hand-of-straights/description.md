Alice has a `` hand `` of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size `` W ``, and consists of `` W `` consecutive cards.

Return `` true `` if and only if she can.

__Note:__ This question is the same as&nbsp;1296:&nbsp;<https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/>

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> hand = [1,2,3,6,2,3,4,7,8], W = 3
<strong>Output:</strong> true
<strong>Explanation:</strong> Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> hand = [1,2,3,4,5], W = 4
<strong>Output:</strong> false
<strong>Explanation:</strong> Alice's hand can't be rearranged into groups of 4.

</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= hand.length &lt;= 10000 ``
*   `` 0 &lt;= hand[i]&nbsp;&lt;= 10^9 ``
*   `` 1 &lt;= W &lt;= hand.length ``