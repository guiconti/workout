We are given&nbsp;`` head ``,&nbsp;the head node of a linked list containing&nbsp;__unique integer values__.

We are also given the list&nbsp;`` G ``, a subset of the values in the linked list.

Return the number of connected components in `` G ``, where two values are connected if they appear consecutively in the linked list.

__Example 1:__

<pre>
<strong>Input:</strong> 
head: 0-&gt;1-&gt;2-&gt;3
G = [0, 1, 3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> 
head: 0-&gt;1-&gt;2-&gt;3-&gt;4
G = [0, 3, 1, 4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
</pre>

__Note: __

*   If&nbsp;`` N ``&nbsp;is the&nbsp;length of the linked list given by&nbsp;`` head ``,&nbsp;`` 1 &lt;= N &lt;= 10000 ``.
*   The value of each node in the linked list will be in the range``  [0, N - 1] ``.
*   `` 1 &lt;= G.length &lt;= 10000 ``.
*   `` G `` is a subset of all values in the linked list.