You are given an integer array `` cards `` of length `` 4 ``. You have four cards, each containing a number in the range `` [1, 9] ``. You should arrange the numbers on these cards in a mathematical expression using the operators `` ['+', '-', '*', '/'] `` and the parentheses `` '(' `` and `` ')' `` to get the value 24.

You are restricted with the following rules:

*   The division operator `` '/' `` represents real division, not integer division.	
    
    *   For example, `` 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12 ``.
    
    
    
*   Every operation done is between two numbers. In particular, we cannot use `` '-' `` as a unary operator.	
    
    *   For example, if `` cards = [1, 1, 1, 1] ``, the expression `` "-1 - 1 - 1 - 1" `` is __not allowed__.
    
    
    
*   You cannot concatenate numbers together	
    
    *   For example, if `` cards = [1, 2, 1, 2] ``, the expression `` "12 + 12" `` is not valid.
    
    
    

Return `` true `` if you can get such expression that evaluates to `` 24 ``, and `` false `` otherwise.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> cards = [4,1,8,7]
<strong>Output:</strong> true
<strong>Explanation:</strong> (8-4) * (7-1) = 24
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> cards = [1,2,1,2]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` cards.length == 4 ``
*   `` 1 &lt;= cards[i] &lt;= 9 ``