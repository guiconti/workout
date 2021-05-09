A game is played by a cat and a mouse named Cat and Mouse.

The environment is represented by a `` grid `` of size `` rows x cols ``, where each element is a wall, floor, player (Cat, Mouse), or food.

*   Players are represented by the characters `` 'C' ``(Cat)`` ,'M' ``(Mouse).
*   Floors are represented by the character `` '.' `` and can be walked on.
*   Walls are represented by the character `` '#' `` and cannot be walked on.
*   Food is represented by the character `` 'F' `` and can be walked on.
*   There is only one of each character `` 'C' ``, `` 'M' ``, and `` 'F' `` in `` grid ``.

Mouse and Cat play according to the following rules:

*   Mouse __moves first__, then they take turns to move.
*   During each turn, Cat and Mouse can jump in one of the four directions (left, right, up, down). They cannot jump over the wall nor outside of the `` grid ``.
*   `` catJump, mouseJump `` are the maximum lengths Cat and Mouse can jump at a time, respectively. Cat and Mouse can jump less than the maximum length.
*   Staying in the same position is allowed.
*   Mouse can jump over Cat.

The game can end in 4 ways:

*   If Cat occupies the same position as Mouse, Cat wins.
*   If Cat reaches the food first, Cat wins.
*   If Mouse reaches the food first, Mouse wins.
*   If Mouse cannot get to the food within 1000 turns, Cat wins.

Given a `` rows x cols `` matrix `` grid `` and two integers `` catJump `` and `` mouseJump ``, return `` true ``_ if Mouse can win the game if both Cat and Mouse play optimally, otherwise return _`` false ``.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/09/12/sample_111_1955.png" style="width: 580px; height: 239px;"/></strong>

<pre>
<strong>Input:</strong> grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> Cat cannot catch Mouse on its turn nor can it get the food before Mouse.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/12/sample_2_1955.png" style="width: 580px; height: 175px;"/>

<pre>
<strong>Input:</strong> grid = ["M.C...F"], catJump = 1, mouseJump = 4
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> grid = ["M.C...F"], catJump = 1, mouseJump = 3
<strong>Output:</strong> false
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
<strong>Output:</strong> false
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 1
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` rows == grid.length ``
*   `` cols = grid[i].length ``
*   `` 1 &lt;= rows, cols &lt;= 8 ``
*   `` grid[i][j] `` consist only of characters `` 'C' ``, `` 'M' ``, `` 'F' ``, `` '.' ``, and `` '#' ``.
*   There is only one of each character `` 'C' ``, `` 'M' ``, and `` 'F' `` in `` grid ``.
*   `` 1 &lt;= catJump, mouseJump &lt;= 8 ``