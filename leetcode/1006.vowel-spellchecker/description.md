Given a `` wordlist ``, we want to implement a spellchecker that converts a query word into a correct word.

For a given `` query `` word, the spell checker handles two categories of spelling mistakes:

*   Capitalization: If the query matches a word in the wordlist (__case-insensitive__), then the query word is returned with the same case as the case in the wordlist.	
    
    *   Example: `` wordlist = ["yellow"] ``, `` query = "YellOw" ``: `` correct = "yellow" ``
    *   Example: `` wordlist = ["Yellow"] ``, `` query = "yellow" ``: `` correct = "Yellow" ``
    *   Example: `` wordlist = ["yellow"] ``, `` query = "yellow" ``: `` correct = "yellow" ``
    
    
    
*   Vowel Errors: If after replacing the vowels `` ('a', 'e', 'i', 'o', 'u') `` of the query word with any vowel individually, it matches a word in the wordlist (__case-insensitive__), then the query word is returned with the same case as the match in the wordlist.	
    
    *   Example: `` wordlist = ["YellOw"] ``, `` query = "yollow" ``: `` correct = "YellOw" ``
    *   Example: `` wordlist = ["YellOw"] ``, `` query = "yeellow" ``: `` correct = "" `` (no match)
    *   Example: `` wordlist = ["YellOw"] ``, `` query = "yllw" ``: `` correct = "" `` (no match)
    
    
    

In addition, the spell checker operates under the following precedence rules:

*   When the query exactly matches a word in the wordlist (__case-sensitive__), you should return the same word back.
*   When the query matches a word up to capitlization, you should return the first such match in the wordlist.
*   When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
*   If the query has no matches in the wordlist, you should return the empty string.

Given some `` queries ``, return a list of words `` answer ``, where `` answer[i] `` is the correct word for `` query = queries[i] ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
<strong>Output:</strong> ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
</pre>

__Example 2:__

<pre><strong>Input:</strong> wordlist = ["yellow"], queries = ["YellOw"]
<strong>Output:</strong> ["yellow"]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= wordlist.length, queries.length &lt;= 5000 ``
*   `` 1 &lt;= wordlist[i].length, queries[i].length &lt;= 7 ``
*   `` wordlist[i] `` and `` queries[i] `` consist only of only English letters.