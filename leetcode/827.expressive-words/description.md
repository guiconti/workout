Sometimes people repeat letters to represent extra feeling, such as "hello" -&gt; "heeellooo", "hi" -&gt; "hiiii".&nbsp; In these strings like "heeellooo", we have _groups_ of adjacent letters that are all the same:&nbsp; "h", "eee", "ll", "ooo".

For some given string `` S ``, a query word is _stretchy_ if it can be made to be equal to `` S `` by any&nbsp;number of&nbsp;applications of the following _extension_ operation: choose a group consisting of&nbsp;characters `` c ``, and add some number of characters `` c `` to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.&nbsp; Also, we could do another extension like "ll" -&gt; "lllll" to get "helllllooo".&nbsp; If `` S = "helllllooo" ``, then the query word "hello" would be stretchy because of these two extension operations:&nbsp;`` query = "hello" -&gt; "hellooo" -&gt;&nbsp;"helllllooo" = S ``.

Given a list of query words, return the number of words that are stretchy.&nbsp;

&nbsp;

<pre>
<strong>Example:</strong>
<strong>Input:</strong> 
S = "heeellooo"
words = ["hello", "hi", "helo"]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= len(S) &lt;= 100 ``.
*   `` 0 &lt;= len(words) &lt;= 100 ``.
*   `` 0 &lt;= len(words[i]) &lt;= 100 ``.
*   `` S `` and all words in `` words ``&nbsp;consist only of&nbsp;lowercase letters