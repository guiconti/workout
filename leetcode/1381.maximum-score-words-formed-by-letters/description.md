Given a list of `` words ``, list of&nbsp; single&nbsp;`` letters `` (might be repeating)&nbsp;and `` score ``&nbsp;of every character.

Return the maximum score of __any__ valid set of words formed by using the given letters (`` words[i] `` cannot be used two&nbsp;or more times).

It is not necessary to use all characters in `` letters `` and each letter can only be used once. Score of letters&nbsp;`` 'a' ``, `` 'b' ``, `` 'c' ``, ... ,`` 'z' `` is given by&nbsp;`` score[0] ``, `` score[1] ``, ... , `` score[25] `` respectively.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
<strong>Output:</strong> 23
<strong>Explanation:</strong>
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
<strong>Output:</strong> 27
<strong>Explanation:</strong>
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
Letter "e" can only be used once.</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= words.length &lt;= 14 ``
*   `` 1 &lt;= words[i].length &lt;= 15 ``
*   `` 1 &lt;= letters.length &lt;= 100 ``
*   `` letters[i].length == 1 ``
*   `` score.length ==&nbsp;26 ``
*   `` 0 &lt;= score[i] &lt;= 10 ``
*   `` words[i] ``, `` letters[i] ``&nbsp;contains only lower case English letters.