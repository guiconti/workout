You have `` k `` servers numbered from `` 0 `` to `` k-1 `` that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but __cannot handle more than one request at a time__. The requests are assigned to servers according to a specific algorithm:

*   The <code>i<sup>th</sup></code> (0-indexed) request arrives.
*   If all servers are busy, the request is dropped (not handled at all).
*   If the <code>(i % k)<sup>th</sup></code> server is available, assign the request to that server.
*   Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the <code>i<sup>th</sup></code> server is busy, try to assign the request to the <code>(i+1)<sup>th</sup></code> server, then the <code>(i+2)<sup>th</sup></code> server, and so on.

You are given a __strictly increasing__ array `` arrival `` of positive integers, where `` arrival[i] `` represents the arrival time of the <code>i<sup>th</sup></code> request, and another array `` load ``, where `` load[i] `` represents the load of the <code>i<sup>th</sup></code> request (the time it takes to complete). Your goal is to find the __busiest server(s)__. A server is considered __busiest__ if it handled the most number of requests successfully among all the servers.

Return _a list containing the IDs (0-indexed) of the __busiest server(s)___. You may return the IDs in any order.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/08/load-1.png" style="width: 389px; height: 221px;"/>

<pre>
<strong>Input:</strong> k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
<strong>Output:</strong> [1] 
<strong>Explanation:</strong>
All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
<strong>Output:</strong> [0]
<strong>Explanation:</strong>
The first 3 requests are handled by first 3 servers.
Request 3 comes in. It is handled by server 0 since the server is available.
Server 0 handled two requests, while servers 1 and 2 handled one request each. Hence server 0 is the busiest server.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> k = 3, arrival = [1,2,3], load = [10,12,11]
<strong>Output:</strong> [0,1,2]
<strong>Explanation: </strong>Each server handles a single request, so they are all considered the busiest.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> k = 3, arrival = [1,2,3,4,8,9,10], load = [5,2,10,3,1,2,2]
<strong>Output:</strong> [1]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> k = 1, arrival = [1], load = [1]
<strong>Output:</strong> [0]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= k &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= arrival.length, load.length &lt;= 10<sup>5</sup></code>
*   `` arrival.length == load.length ``
*   <code>1 &lt;= arrival[i], load[i] &lt;= 10<sup>9</sup></code>
*   `` arrival `` is __strictly increasing__.