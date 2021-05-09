Given two integers `` tomatoSlices ``&nbsp;and `` cheeseSlices ``. The ingredients of different burgers are as follows:

*   __Jumbo Burger:__ 4 tomato slices&nbsp;and 1 cheese slice.
*   __Small Burger:__ 2 Tomato slices&nbsp;and 1 cheese slice.

Return `` [total_jumbo, total_small] `` so that the number of remaining `` tomatoSlices ``&nbsp;equal to 0 and the number of remaining `` cheeseSlices `` equal to 0. If it is not possible to make the remaining `` tomatoSlices ``&nbsp;and `` cheeseSlices `` equal to 0 return `` [] ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> tomatoSlices = 16, cheeseSlices = 7
<strong>Output:</strong> [1,6]
<strong>Explantion:</strong> To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese. There will be no remaining ingredients.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> tomatoSlices = 17, cheeseSlices = 4
<strong>Output:</strong> []
<strong>Explantion:</strong> There will be no way to use all ingredients to make small and jumbo burgers.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> tomatoSlices = 4, cheeseSlices = 17
<strong>Output:</strong> []
<strong>Explantion:</strong> Making 1 jumbo burger there will be 16 cheese remaining and making 2 small burgers there will be 15 cheese remaining.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> tomatoSlices = 0, cheeseSlices = 0
<strong>Output:</strong> [0,0]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> tomatoSlices = 2, cheeseSlices = 1
<strong>Output:</strong> [0,1]
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= tomatoSlices &lt;= 10^7 ``
*   `` 0 &lt;= cheeseSlices &lt;= 10^7 ``