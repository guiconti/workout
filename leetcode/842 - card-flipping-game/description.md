On a table are `` N `` cards, with a positive integer printed on the front and back of each card (possibly different).

We flip any number of cards, and after we choose one&nbsp;card.&nbsp;

If the number `` X `` on the back of the chosen&nbsp;card is not on the front of any card, then this number X is good.

What is the smallest number that is good?&nbsp; If no number is good, output `` 0 ``.

Here, `` fronts[i] `` and `` backs[i] `` represent the number on the front and back of card `` i ``.&nbsp;

A&nbsp;flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.

__Example:__

<strong>Input:</strong> fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
    <strong>Output:</strong> 2
    <strong>Explanation:</strong> If we flip the second card, the fronts are <code>[1,3,4,4,7]</code> and the backs are <code>[1,2,4,1,3]</code>.
    We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so <code>2</code> is good.

&nbsp;

__Note:__

1.   `` 1 &lt;= fronts.length == backs.length&nbsp;&lt;=&nbsp;1000 ``.
2.   `` 1 &lt;=&nbsp;fronts[i]&nbsp;&lt;= 2000 ``.
3.   `` 1 &lt;= backs[i]&nbsp;&lt;= 2000 ``.