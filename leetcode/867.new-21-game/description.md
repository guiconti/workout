Alice plays the following game, loosely based on the card game "21".

Alice starts with `` 0 `` points, and draws numbers while she has less than `` K `` points.&nbsp; During each draw, she gains an integer number of points randomly from the range `` [1, W] ``, where `` W `` is an integer.&nbsp; Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets `` K `` or more points.&nbsp; What is the probability&nbsp;that she has `` N `` or less points?

__Example 1:__

<pre>
<strong>Input: </strong>N = 10, K = 1, W = 10
<strong>Output: </strong>1.00000
<strong>Explanation: </strong> Alice gets a single card, then stops.
</pre>

__Example 2:__

<pre>
<strong>Input: </strong>N = 6, K = 1, W = 10
<strong>Output: </strong>0.60000
<strong>Explanation: </strong> Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
</pre>

__Example 3:__

<pre>
<strong>Input: </strong>N = 21, K = 17, W = 10
<strong>Output: </strong>0.73278</pre>

__Note:__

1.   `` 0 &lt;= K &lt;= N &lt;= 10000 ``
2.   `` 1 &lt;= W &lt;= 10000 ``
3.   Answers will be accepted as correct if they are within `` 10^-5 `` of the correct answer.
4.   The judging time limit has been reduced for this question.