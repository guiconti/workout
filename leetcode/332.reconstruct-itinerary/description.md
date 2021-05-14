You are given a list of airline `` tickets `` where <code>tickets[i] = [from<sub>i</sub>, to<sub>i</sub>]</code> represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from `` "JFK" ``, thus, the itinerary must begin with `` "JFK" ``. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

*   For example, the itinerary `` ["JFK", "LGA"] `` has a smaller lexical order than `` ["JFK", "LGB"] ``.

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg" style="width: 382px; height: 222px;"/>

<pre>
<strong>Input:</strong> tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
<strong>Output:</strong> ["JFK","MUC","LHR","SFO","SJC"]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg" style="width: 222px; height: 230px;"/>

<pre>
<strong>Input:</strong> tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
<strong>Output:</strong> ["JFK","ATL","JFK","SFO","ATL","SFO"]
<strong>Explanation:</strong> Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= tickets.length &lt;= 300 ``
*   `` tickets[i].length == 2 ``
*   <code>from<sub>i</sub>.length == 3</code>
*   <code>to<sub>i</sub>.length == 3</code>
*   <code>from<sub>i</sub></code> and <code>to<sub>i</sub></code> consist of uppercase English letters.
*   <code>from<sub>i</sub> != to<sub>i</sub></code>