There are `` N `` rooms and you start in room `` 0 ``.&nbsp; Each room has a distinct number in `` 0, 1, 2, ..., N-1 ``, and each room may have&nbsp;some keys to access the next room.&nbsp;

Formally, each room `` i ``&nbsp;has a list of keys `` rooms[i] ``, and each key `` rooms[i][j] `` is an integer in `` [0, 1, ..., N-1] `` where `` N = rooms.length ``.&nbsp; A key `` rooms[i][j] = v ``&nbsp;opens the room with number `` v ``.

Initially, all the rooms start locked (except for room `` 0 ``).&nbsp;

You can walk back and forth between rooms freely.

Return `` true ``&nbsp;if and only if you can enter&nbsp;every room.

__Example 1:__

<pre>
<strong>Input: </strong>[[1],[2],[3],[]]
<strong>Output: </strong>true
<strong>Explanation:  </strong>
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
</pre>

__Example 2:__

<pre>
<strong>Input: </strong>[[1,3],[3,0,1],[2],[0]]
<strong>Output: </strong>false
<strong>Explanation: </strong>We can't enter the room with number 2.
</pre>

__Note:__

1.   `` 1 &lt;= rooms.length &lt;=&nbsp;1000 ``
2.   `` 0 &lt;= rooms[i].length &lt;= 1000 ``
3.   The number of keys in all rooms combined is at most&nbsp;`` 3000 ``.