On a __single-threaded__ CPU, we execute a program containing `` n `` functions. Each function has a unique ID between `` 0 `` and `` n-1 ``.

Function calls are __stored in a [call stack](https://en.wikipedia.org/wiki/Call_stack)__: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is __the current function being executed__. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list `` logs ``, where `` logs[i] `` represents the <code>i<sup>th</sup></code> log message formatted as a string `` "{function_id}:{"start" | "end"}:{timestamp}" ``. For example, `` "0:start:3" `` means a function call with function ID `` 0 `` __started at the beginning__ of timestamp `` 3 ``, and `` "1:end:2" `` means a function call with function ID `` 1 `` __ended at the end__ of timestamp `` 2 ``. Note that a function can be called __multiple times, possibly recursively__.

A function's __exclusive time__ is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for `` 2 `` time units and another call executing for `` 1 `` time unit, the __exclusive time__ is `` 2 + 1 = 3 ``.

Return _the __exclusive time__ of each function in an array, where the value at the _<code>i<sup>th</sup></code>_ index represents the exclusive time for the function with ID _`` i ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/04/05/diag1b.png" style="width: 550px; height: 239px;"/>

<pre>
<strong>Input:</strong> n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
<strong>Output:</strong> [3,4]
<strong>Explanation:</strong>
Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
<strong>Output:</strong> [8]
<strong>Explanation:</strong>
Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls itself again.
Function 0 (2nd recursive call) starts at the beginning of time 6 and executes for 1 unit of time.
Function 0 (initial call) resumes execution at the beginning of time 7 and executes for 1 unit of time.
So function 0 spends 2 + 4 + 1 + 1 = 8 units of total time executing.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
<strong>Output:</strong> [7,1]
<strong>Explanation:</strong>
Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls function 1.
Function 1 starts at the beginning of time 6, executes 1 units of time, and ends at the end of time 6.
Function 0 resumes execution at the beginning of time 6 and executes for 2 units of time.
So function 0 spends 2 + 4 + 1 = 7 units of total time executing, and function 1 spends 1 unit of total time executing.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]
<strong>Output:</strong> [8,1]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 1, logs = ["0:start:0","0:end:0"]
<strong>Output:</strong> [1]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 100 ``
*   `` 1 &lt;= logs.length &lt;= 500 ``
*   `` 0 &lt;= function_id &lt; n ``
*   <code>0 &lt;= timestamp &lt;= 10<sup>9</sup></code>
*   No two start events will happen at the same timestamp.
*   No two end events will happen at the same timestamp.
*   Each function has an `` "end" `` log for each `` "start" `` log.