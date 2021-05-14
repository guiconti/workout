With respect to a given `` puzzle `` string, a `` word `` is _valid_&nbsp;if both the following conditions are satisfied:

*   `` word `` contains the first letter of `` puzzle ``.
*   For each letter in `` word ``, that letter is in `` puzzle ``.  
    	For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage"; while invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).

Return an array `` answer ``, where `` answer[i] `` is the number of words in the given word list&nbsp;`` words `` that are valid with respect to the puzzle `` puzzles[i] ``.
&nbsp;

__Example :__

<pre>
<strong>Input:</strong> 
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
<strong>Output:</strong> [1,1,3,2,4,0]
<strong>Explanation:</strong>
1 valid word&nbsp;for "aboveyz" : "aaaa" 
1 valid word&nbsp;for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for&nbsp;"absoryz" : "aaaa", "asas"
4 valid words for&nbsp;"actresz" : "aaaa", "asas", "actt", "access"
There're&nbsp;no valid words for&nbsp;"gaswxyz" cause none of the words in the list contains letter 'g'.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= words.length &lt;= 10^5 ``
*   `` 4 &lt;= words[i].length &lt;= 50 ``
*   `` 1 &lt;= puzzles.length &lt;= 10^4 ``
*   `` puzzles[i].length == 7 ``
*   `` words[i][j] ``, `` puzzles[i][j] `` are English lowercase letters.
*   Each `` puzzles[i]  ``doesn't contain repeated characters.