Given an integer array `` arr `` of __distinct__ integers and an integer `` k ``.

A game will be played between the first two elements of the array (i.e. `` arr[0] `` and `` arr[1] ``). In each round of the game, we compare `` arr[0] `` with `` arr[1] ``, the larger integer&nbsp;wins and remains at position `` 0 `` and the smaller integer moves to the end of the array. The game ends when an integer wins `` k `` consecutive rounds.

Return _the integer which will win the game_.

It is __guaranteed__ that there will be a winner of the game.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [2,1,3,5,4,6,7], k = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> Let's see the rounds of the game:
Round |       arr       | winner | win_count
  1   | [2,1,3,5,4,6,7] | 2      | 1
  2   | [2,3,5,4,6,7,1] | 3      | 1
  3   | [3,5,4,6,7,1,2] | 5      | 1
  4   | [5,4,6,7,1,2,3] | 5      | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [3,2,1], k = 10
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 will win the first 10 rounds consecutively.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [1,9,8,2,3,7,6,4,5], k = 7
<strong>Output:</strong> 9
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
<strong>Output:</strong> 99
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= arr.length &lt;= 10^5 ``
*   `` 1 &lt;= arr[i] &lt;= 10^6 ``
*   `` arr `` contains __distinct__&nbsp;integers.
*   `` 1 &lt;= k &lt;= 10^9 ``