You are given an array of positive integers `` w `` where `` w[i] `` describes the weight of `` i ``<sup>`` th ``&nbsp;</sup>index (0-indexed).

We need to call the function&nbsp;`` pickIndex() `` which __randomly__ returns an integer in the range `` [0, w.length - 1] ``.&nbsp;`` pickIndex() ``&nbsp;should return the integer&nbsp;proportional to its weight in the `` w `` array. For example, for `` w = [1, 3] ``, the probability of picking the index `` 0 `` is `` 1 / (1 + 3)&nbsp;= 0.25 `` (i.e 25%)&nbsp;while the probability of picking the index `` 1 `` is `` 3 / (1 + 3)&nbsp;= 0.75 `` (i.e 75%).

More formally, the probability of picking index `` i `` is `` w[i] / sum(w) ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["Solution","pickIndex"]
[[[1]],[]]
<strong>Output</strong>
[null,0]

<strong>Explanation</strong>
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.
</pre>

__Example 2:__

<pre>
<strong>Input</strong>
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
<strong>Output</strong>
[null,1,1,1,1,0]

<strong>Explanation</strong>
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.

Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= w.length &lt;= 10000 ``
*   `` 1 &lt;= w[i] &lt;= 10^5 ``
*   `` pickIndex ``&nbsp;will be called at most `` 10000 `` times.