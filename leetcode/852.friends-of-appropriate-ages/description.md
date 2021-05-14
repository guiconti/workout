Some people will make friend requests. The&nbsp;list of their ages is given and&nbsp;`` ages[i] ``&nbsp;is the age of the&nbsp;ith person.&nbsp;

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

*   `` age[B]&nbsp;&lt;= 0.5 * age[A]&nbsp;+ 7 ``
*   `` age[B]&nbsp;&gt; age[A] ``
*   `` age[B]&nbsp;&gt; 100 &amp;&amp;&nbsp;age[A]&nbsp;&lt; 100 ``

Otherwise, A will friend request B.

Note that if&nbsp;A requests B, B does not necessarily request A.&nbsp; Also, people will not friend request themselves.

How many total friend requests are made?

__Example 1:__

<pre>
<strong>Input: </strong>[16,16]
<strong>Output: </strong>2
<strong>Explanation: </strong>2 people friend request each other.
</pre>

__Example 2:__

<pre>
<strong>Input: </strong>[16,17,18]
<strong>Output: </strong>2
<strong>Explanation: </strong>Friend requests are made 17 -&gt; 16, 18 -&gt; 17.</pre>

__Example 3:__

<pre>
<strong>Input: </strong>[20,30,100,110,120]
<strong>Output: </strong>3
<strong>Explanation: </strong>Friend requests are made 110 -&gt; 100, 120 -&gt; 110, 120 -&gt; 100.
</pre>

&nbsp;

Notes:

*   `` 1 &lt;= ages.length&nbsp;&lt;= 20000 ``.
*   `` 1 &lt;= ages[i] &lt;= 120 ``.