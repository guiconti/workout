Suppose LeetCode will start its __IPO__ soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the __IPO__. Since it has limited resources, it can only finish at most `` k `` distinct projects before the __IPO__. Help LeetCode design the best way to maximize its total capital after finishing at most `` k `` distinct projects.

You are given `` n `` projects where the <code>i<sup>th</sup></code> project has a pure profit `` profits[i] `` and a minimum capital of `` capital[i] `` is needed to start it.

Initially, you have `` w `` capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of __at most__ `` k `` distinct projects from given projects to __maximize your final capital__, and return _the final maximized capital_.

The answer is guaranteed to fit in a 32-bit signed integer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
<strong>Output:</strong> 6
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= k &lt;= 10<sup>5</sup></code>
*   <code>0 &lt;= w &lt;= 10<sup>9</sup></code>
*   `` n == profits.length ``
*   `` n == capital.length ``
*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>
*   <code>0 &lt;= profits[i] &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= capital[i] &lt;= 10<sup>9</sup></code>