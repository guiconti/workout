A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

1.   The area of the rectangular web page you designed must equal to the given target area.
2.   The width `` W `` should not be larger than the length `` L ``, which means `` L &gt;= W ``.
3.   The difference between length `` L `` and width `` W `` should be as small as possible.

Return _an array `` [L, W] `` where `` L `` and `` W `` are the length and width of the&nbsp;web page you designed in sequence._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> area = 4
<strong>Output:</strong> [2,2]
<strong>Explanation:</strong> The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> area = 37
<strong>Output:</strong> [37,1]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> area = 122122
<strong>Output:</strong> [427,286]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= area &lt;= 10<sup>7</sup></code>