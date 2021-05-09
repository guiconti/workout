A company has `` n `` employees with a unique ID for each employee from `` 0 `` to `` n - 1 ``. The head of the company is the one with `` headID ``.

Each employee has one direct manager given in the `` manager `` array where `` manager[i] `` is the direct manager of the `` i-th `` employee, `` manager[headID] = -1 ``. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The `` i-th `` employee needs `` informTime[i] `` minutes to inform all of his direct subordinates (i.e., After informTime\[i\] minutes, all his direct subordinates can start spreading the news).

Return _the number of minutes_ needed to inform all the employees about the urgent news.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 1, headID = 0, manager = [-1], informTime = [0]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The head of the company is the only employee in the company.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/27/graph.png" style="width: 404px; height: 174px;"/>

<pre>
<strong>Input:</strong> n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/28/1730_example_3_5.PNG" style="width: 568px; height: 432px;"/>

<pre>
<strong>Input:</strong> n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
<strong>Output:</strong> 21
<strong>Explanation:</strong> The head has id = 6. He will inform employee with id = 5 in 1 minute.
The employee with id = 5 will inform the employee with id = 4 in 2 minutes.
The employee with id = 4 will inform the employee with id = 3 in 3 minutes.
The employee with id = 3 will inform the employee with id = 2 in 4 minutes.
The employee with id = 2 will inform the employee with id = 1 in 5 minutes.
The employee with id = 1 will inform the employee with id = 0 in 6 minutes.
Needed time = 1 + 2 + 3 + 4 + 5 + 6 = 21.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The first minute the head will inform employees 1 and 2.
The second minute they will inform employees 3, 4, 5 and 6.
The third minute they will inform the rest of employees.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]
<strong>Output:</strong> 1076
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>
*   `` 0 &lt;= headID &lt; n ``
*   `` manager.length == n ``
*   `` 0 &lt;= manager[i] &lt; n ``
*   `` manager[headID] == -1 ``
*   `` informTime.length == n ``
*   `` 0 &lt;= informTime[i] &lt;= 1000 ``
*   `` informTime[i] == 0 `` if employee `` i `` has no subordinates.
*   It is __guaranteed__ that all the employees can be informed.