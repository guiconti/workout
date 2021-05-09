There are `` n `` cities connected by some number of flights. You are given an array `` flights `` where <code>flights[i] = [from<sub>i</sub>, to<sub>i</sub>, price<sub>i</sub>]</code> indicates that there is a flight from city <code>from<sub>i</sub></code> to city <code>to<sub>i</sub></code> with cost <code>price<sub>i</sub></code>.

You are also given three integers `` src ``, `` dst ``, and `` k ``, return ___the cheapest price__ from _`` src ``_ to _`` dst ``_ with at most _`` k ``_ stops. _If there is no such route, return_ _`` -1 ``.

&nbsp;

__Example 1:__

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height: 360px; width: 492px;"/>

<strong>Input:</strong> n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
    <strong>Output:</strong> 200
    <strong>Explanation:</strong> The graph is shown.
    The cheapest price from city 0 to city <code>2</code> with at most 1 stop costs 200, as marked red in the picture.

__Example 2:__

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height: 360px; width: 492px;"/>

<strong>Input:</strong> n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
    <strong>Output:</strong> 500
    <strong>Explanation:</strong> The graph is shown.
    The cheapest price from city 0 to city <code>2</code> with at most 0 stop costs 500, as marked blue in the picture.

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 100 ``
*   `` 0 &lt;= flights.length &lt;= (n * (n - 1) / 2) ``
*   `` flights[i].length == 3 ``
*   <code>0 &lt;= from<sub>i</sub>, to<sub>i</sub> &lt; n</code>
*   <code>from<sub>i</sub> != to<sub>i</sub></code>
*   <code>1 &lt;= price<sub>i</sub> &lt;= 10<sup>4</sup></code>
*   There will not be any multiple flights between two cities.
*   `` 0 &lt;= src, dst, k &lt; n ``
*   `` src != dst ``