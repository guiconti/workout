







__Example 1:__  

<pre>
<b>Input:</b> grid = 
[[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]
<b>Output:</b> 10
<b>Explanation:</b>
There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:

[[0,1,0,0,0,0,1,1],
 [0,1,0,0,0,0,1,1],
 [0,0,0,0,0,0,1,1],
 [0,0,0,0,0,0,0,1]]

On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.
</pre>

__Example 2:__  

<pre>
<b>Input:</b> grid = 
[[1,1,1],
 [1,0,1],
 [1,1,1]]
<b>Output:</b> 4
<b>Explanation:</b> Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.
</pre>

__Example 3:__  

<pre>
<b>Input:</b> grid = 
[[1,1,1,0,0,0,0,0,0],
 [1,0,1,0,1,1,1,1,1],
 [1,1,1,0,0,0,0,0,0]]
<b>Output:</b> 13
<b>Explanation:</b> The region on the left only builds two new walls.
</pre>

__Note:__  

1.   The number of rows and columns of `` grid `` will each be in the range `` [1, 50] ``.
2.   Each `` grid[i][j] `` will be either `` 0 `` or `` 1 ``.
3.   Throughout the described process, there is always a contiguous viral region that will infect __strictly more__ uncontaminated squares in the next round.