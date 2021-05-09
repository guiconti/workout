Given a string `` s ``, we make queries on substrings of `` s ``.

For each query `` queries[i] = [left, right, k] ``, we may __rearrange__&nbsp;the substring `` s[left], ..., s[right] ``, and then choose __up to__ `` k `` of them to replace with any lowercase English letter.&nbsp;

If the substring&nbsp;is possible to be a&nbsp;palindrome string after the operations above, the result of the query is `` true ``.&nbsp;Otherwise, the result&nbsp;is `` false ``.

Return an array `` answer[] ``, where `` answer[i] `` is the result of the `` i ``-th query `` queries[i] ``.

Note that: Each letter is counted __individually__ for replacement so&nbsp;if for example&nbsp;`` s[left..right] = "aaa" ``, and `` k = 2 ``, we can only replace two of the letters.&nbsp; (Also, note that the initial string `` s ``&nbsp;is never modified by any query.)

&nbsp;

__Example :__

<pre>
<strong>Input:</strong> s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
<strong>Output:</strong> [true,false,false,true,true]
<strong>Explanation:</strong>
queries[0] : substring = "d", is palidrome.
queries[1] :&nbsp;substring = "bc", is not palidrome.
queries[2] :&nbsp;substring = "abcd", is not palidrome after replacing only 1 character.
queries[3] :&nbsp;substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
queries[4] :&nbsp;substring = "abcda",&nbsp;could be changed to "abcba" which is palidrome.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length,&nbsp;queries.length&nbsp;&lt;= 10^5 ``
*   `` 0 &lt;= queries[i][0] &lt;= queries[i][1] &lt;&nbsp;s.length ``
*   `` 0 &lt;= queries[i][2] &lt;= s.length ``
*   `` s `` only contains lowercase English letters.