



__Examples of Axis-Aligned Plus Signs of Order k:__  

<pre>
Order 1:
000
0<b>1</b>0
000

Order 2:
00000
00<b>1</b>00
0<b>111</b>0
00<b>1</b>00
00000

Order 3:
0000000
000<b>1</b>000
000<b>1</b>000
0<b>11111</b>0
000<b>1</b>000
000<b>1</b>000
0000000
</pre>

__Example 1:__  

<pre>
<b>Input:</b> N = 5, mines = [[4, 2]]
<b>Output:</b> 2
<b>Explanation:</b>
11111
11111
1<b>1</b>111
<b>111</b>11
1<b>1</b>011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
</pre>

__Example 2:__  

<pre>
<b>Input:</b> N = 2, mines = []
<b>Output:</b> 1
<b>Explanation:</b>
There is no plus sign of order 2, but there is of order 1.
</pre>

__Example 3:__  

<pre>
<b>Input:</b> N = 1, mines = [[0, 0]]
<b>Output:</b> 0
<b>Explanation:</b>
There is no plus sign, so return 0.
</pre>

__Note:__  

1.   `` N `` will be an integer in the range `` [1, 500] ``.
2.   `` mines `` will have length at most `` 5000 ``.
3.   `` mines[i] `` will be length 2 and consist of integers in the range `` [0, N-1] ``.
4.   _(Additionally, programs submitted in C, C++, or C\# will be judged with a slightly smaller time limit.)_