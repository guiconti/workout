Hercy wants to save money for his first car. He puts money in the Leetcode&nbsp;bank __every day__.

He starts by putting in `` $1 `` on Monday, the first day. Every day from Tuesday to Sunday, he will put in `` $1 `` more than the day before. On every subsequent Monday, he will put in `` $1 `` more than the __previous Monday__.<span style="display: none;"> </span>

Given `` n ``, return _the total amount of money he will have in the Leetcode bank at the end of the _<code>n<sup>th</sup></code>_ day._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 10
<strong>Explanation:</strong>&nbsp;After the 4<sup>th</sup> day, the total is 1 + 2 + 3 + 4 = 10.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 37
<strong>Explanation:</strong>&nbsp;After the 10<sup>th</sup> day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2<sup>nd</sup> Monday, Hercy only puts in $2.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 20
<strong>Output:</strong> 96
<strong>Explanation:</strong>&nbsp;After the 20<sup>th</sup> day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 1000 ``