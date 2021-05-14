







__Example 1:__  

<pre>
<b>Input:</b> 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
<b>Output:</b> [[2,2,2],[2,2,0],[2,0,1]]
<b>Explanation:</b> 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
</pre>

__Note:__<li>The length of <code>image</code> and <code>image[0]</code> will be in the range <code>[1, 50]</code>.</li><li>The given starting pixel will satisfy <code>0 &lt;= sr &lt; image.length</code> and <code>0 &lt;= sc &lt; image[0].length</code>.</li><li>The value of each color in <code>image[i][j]</code> and <code>newColor</code> will be an integer in <code>[0, 65535]</code>.</li>