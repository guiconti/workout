We have `` n `` buildings numbered from `` 0 `` to `` n - 1 ``. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.

You are given an array `` requests `` where <code>requests[i] = [from<sub>i</sub>, to<sub>i</sub>]</code> represents an employee's request to transfer from building <code>from<sub>i</sub></code> to building <code>to<sub>i</sub></code>.

__All buildings are full__, so a list of requests is achievable only if for each building, the __net change in employee transfers is zero__. This means the number of employees __leaving__ is __equal__ to the number of employees __moving in__. For example if `` n = 3 `` and two employees are leaving building `` 0 ``, one is leaving building `` 1 ``, and one is leaving building `` 2 ``, there should be two employees moving to building `` 0 ``, one employee moving to building `` 1 ``, and one employee moving to building `` 2 ``.

Return _the maximum number of achievable requests_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/10/move1.jpg" style="width: 600px; height: 406px;"/>

<pre>
<strong>Input:</strong> n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
<strong>Output:</strong> 5
<strong>Explantion:</strong> Let's see the requests:
From building 0 we have employees x and y and both want to move to building 1.
From building 1 we have employees a and b and they want to move to buildings 2 and 0 respectively.
From building 2 we have employee z and they want to move to building 0.
From building 3 we have employee c and they want to move to building 4.
From building 4 we don't have any requests.
We can achieve the requests of users x and b by swapping their places.
We can achieve the requests of users y, a and z by swapping the places in the 3 buildings.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/10/move2.jpg" style="width: 450px; height: 327px;"/>

<pre>
<strong>Input:</strong> n = 3, requests = [[0,0],[1,2],[2,1]]
<strong>Output:</strong> 3
<strong>Explantion:</strong> Let's see the requests:
From building 0 we have employee x and they want to stay in the same building 0.
From building 1 we have employee y and they want to move to building 2.
From building 2 we have employee z and they want to move to building 1.
We can achieve all the requests. </pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 20 ``
*   `` 1 &lt;= requests.length &lt;= 16 ``
*   `` requests[i].length == 2 ``
*   <code>0 &lt;= from<sub>i</sub>, to<sub>i</sub> &lt; n</code>