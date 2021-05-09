We are playing the Guessing Game. The game will work as follows:

1.   I pick a number between&nbsp;`` 1 ``&nbsp;and&nbsp;`` n ``.
2.   You guess a number.
3.   If you guess the right number, __you win the game__.
4.   If you guess the wrong number, then I will tell you whether the number I picked is __higher or lower__, and you will continue guessing.
5.   Every time you guess a wrong number&nbsp;`` x ``, you will pay&nbsp;`` x ``&nbsp;dollars. If you run out of money, __you lose the game__.

Given a particular&nbsp;`` n ``, return&nbsp;_the minimum amount of money you need to&nbsp;__guarantee a win regardless of what number I pick___.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/10/graph.png" style="width: 505px; height: 388px;"/>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 16
<strong>Explanation:</strong> The winning strategy is as follows:
- The range is [1,10]. Guess 7.
&nbsp;   - If this is my number, your total is $0. Otherwise, you pay $7.
&nbsp;   - If my number is higher, the range is [8,10]. Guess 9.
&nbsp;       - If this is my number, your total is $7. Otherwise, you pay $9.
&nbsp;       - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
&nbsp;       - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
&nbsp;   - If my number is lower, the range is [1,6]. Guess 3.
&nbsp;       - If this is my number, your total is $7. Otherwise, you pay $3.
&nbsp;       - If my number is higher, the range is [4,6]. Guess 5.
&nbsp;           - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
&nbsp;           - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
&nbsp;           - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
&nbsp;       - If my number is lower, the range is [1,2]. Guess 1.
&nbsp;           - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
&nbsp;           - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong>&nbsp;There is only one possible number, so you can guess 1 and not have to pay anything.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong>&nbsp;There are two possible numbers, 1 and 2.
- Guess 1.
&nbsp;   - If this is my number, your total is $0. Otherwise, you pay $1.
&nbsp;   - If my number is higher, it must be 2. Guess 2. Your total is $1.
The worst case is that you pay $1.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 200 ``