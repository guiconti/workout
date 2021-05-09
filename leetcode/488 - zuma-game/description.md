Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> board = "WRRBBW", hand = "RB"
<strong>Output:</strong> -1
<strong>Explanation:</strong> WRRBBW -&gt; WRR[R]BBW -&gt; WBBW -&gt; WBB[B]W -&gt; WW
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> board = "WWRRBBWW", hand = "WRBRW"
<strong>Output:</strong> 2
<strong>Explanation:</strong> WWRRBBWW -&gt; WWRR[R]BBWW -&gt; WWBBWW -&gt; WWBB[B]WW -&gt; WWWW -&gt; empty
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> board = "G", hand = "GGGGG"
<strong>Output:</strong> 2
<strong>Explanation:</strong> G -&gt; G[G] -&gt; GG[G] -&gt; empty 
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> board = "RBYYBBRRB", hand = "YRBGB"
<strong>Output:</strong> 3
<strong>Explanation:</strong> RBYYBBRRB -&gt; RBYY[Y]BBRRB -&gt; RBBBRRB -&gt; RRRB -&gt; B -&gt; B[B] -&gt; BB[B] -&gt; empty 
</pre>

&nbsp;

__Constraints:__

*   You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
*   `` 1 &lt;= board.length &lt;= 16 ``
*   `` 1 &lt;= hand.length &lt;= 5 ``
*   Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.