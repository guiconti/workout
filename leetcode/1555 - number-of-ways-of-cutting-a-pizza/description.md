Given a rectangular pizza represented as a `` rows x cols ``&nbsp;matrix containing the following characters: `` 'A' `` (an apple) and `` '.' `` (empty cell) and given the integer `` k ``. You have to cut the pizza into `` k `` pieces using `` k-1 `` cuts.&nbsp;

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

_Return the number of ways of cutting the pizza such that each piece contains __at least__ one apple.&nbsp;_Since the answer can be a huge number, return this modulo 10^9 + 7.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/04/23/ways_to_cut_apple_1.png" style="width: 500px; height: 378px;"/></strong>

<pre>
<strong>Input:</strong> pizza = ["A..","AAA","..."], k = 3
<strong>Output:</strong> 3 
<strong>Explanation:</strong> The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> pizza = ["A..","AA.","..."], k = 3
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> pizza = ["A..","A..","..."], k = 1
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= rows, cols &lt;= 50 ``
*   `` rows ==&nbsp;pizza.length ``
*   `` cols ==&nbsp;pizza[i].length ``
*   `` 1 &lt;= k &lt;= 10 ``
*   `` pizza `` consists of characters `` 'A' ``&nbsp;and `` '.' `` only.