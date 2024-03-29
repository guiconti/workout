Write a class `` StockSpanner `` which collects daily price quotes for some stock, and returns the _span_&nbsp;of that stock's price for the current day.

The span of the stock's price today&nbsp;is defined as the maximum number of consecutive days (starting from today and going backwards)&nbsp;for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were `` [100, 80, 60, 70, 60, 75, 85] ``, then the stock spans would be `` [1, 1, 1, 2, 1, 4, 6] ``.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-1-1">["StockSpanner","next","next","next","next","next","next","next"]</span>, <span id="example-input-1-2">[[],[100],[80],[60],[70],[60],[75],[85]]</span>
<strong>Output: </strong><span id="example-output-1">[null,1,1,1,2,1,4,6]</span>
<strong>Explanation: </strong>
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.
</pre>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ol>
<li>Calls to <code>StockSpanner.next(int price)</code> will have <code>1 &lt;= price &lt;= 10^5</code>.</li>
<li>There will be at most <code>10000</code> calls to <code>StockSpanner.next</code>&nbsp;per test case.</li>
<li>There will be at most <code>150000</code> calls to <code>StockSpanner.next</code> across all test cases.</li>
<li>The total&nbsp;time limit for this problem has been reduced by 75% for&nbsp;C++, and 50% for all other languages.</li>
</ol>
</div>