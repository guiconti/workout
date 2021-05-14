We have a sequence of `` books ``: the `` i ``-th book has thickness `` books[i][0] `` and height `` books[i][1] ``.

We want to place these books __in order__&nbsp;onto bookcase shelves that have total width `` shelf_width ``.

We choose&nbsp;some of the books to place on this shelf (such that the sum of their thickness is `` &lt;= shelf_width ``), then build another level of shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down.&nbsp; We repeat this process until there are no more books to place.

Note again that at each step of the above&nbsp;process, <u>the order of the books we place is the same order as the given sequence of books</u>.&nbsp; For example, if we have an ordered list of 5&nbsp;books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/06/24/shelves.png" style="width: 250px; height: 370px;"/>

<pre>
<strong>Input:</strong> books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
<strong>Output:</strong> 6
<strong>Explanation:</strong>
The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= books.length &lt;= 1000 ``
*   `` 1 &lt;= books[i][0] &lt;= shelf_width &lt;= 1000 ``
*   `` 1 &lt;= books[i][1] &lt;= 1000 ``