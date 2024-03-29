You are given a data structure of employee information, which includes the employee's __unique id__, their&nbsp;__importance value__ and their&nbsp;__direct__ subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like \[1, 15, \[2\]\], and employee 2 has \[2, 10, \[3\]\], and employee 3 has \[3, 5, \[\]\]. Note that although employee 3 is also a subordinate of employee 1, the relationship is __not direct__.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all their&nbsp;subordinates.

__Example 1:__

<pre>
<b>Input:</b> [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
<b>Output:</b> 11
<b>Explanation:</b>
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
</pre>

&nbsp;

__Note:__

1.   One employee has at most one __direct__ leader and may have several subordinates.
2.   The maximum number of employees won't exceed 2000.