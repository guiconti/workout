You are given two strings `` word1 `` and `` word2 ``. You want to construct a string `` merge `` in the following way: while either `` word1 `` or `` word2 `` are non-empty, choose __one__ of the following options:

*   If `` word1 `` is non-empty, append the __first__ character in `` word1 `` to `` merge `` and delete it from `` word1 ``.	
    
    *   For example, if `` word1 = "abc"  ``and `` merge = "dv" ``, then after choosing this operation, `` word1 = "bc" `` and `` merge = "dva" ``.
    
    
    
*   If `` word2 `` is non-empty, append the __first__ character in `` word2 `` to `` merge `` and delete it from `` word2 ``.	
    
    *   For example, if `` word2 = "abc"  ``and `` merge = "" ``, then after choosing this operation, `` word2 = "bc" `` and `` merge = "a" ``.
    
    
    

Return _the lexicographically __largest__ _`` merge ``_ you can construct_.

A string `` a `` is lexicographically larger than a string `` b `` (of the same length) if in the first position where `` a `` and `` b `` differ, `` a `` has a character strictly larger than the corresponding character in `` b ``. For example, `` "abcd" `` is lexicographically larger than `` "abcc" `` because the first position they differ is at the fourth character, and `` d `` is greater than `` c ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> word1 = "cabaa", word2 = "bcaaa"
<strong>Output:</strong> "cbcabaaaaa"
<strong>Explanation:</strong> One way to get the lexicographically largest merge is:
- Take from word1: merge = "c", word1 = "abaa", word2 = "bcaaa"
- Take from word2: merge = "cb", word1 = "abaa", word2 = "caaa"
- Take from word2: merge = "cbc", word1 = "abaa", word2 = "aaa"
- Take from word1: merge = "cbca", word1 = "baa", word2 = "aaa"
- Take from word1: merge = "cbcab", word1 = "aa", word2 = "aaa"
- Append the remaining 5 a's from word1 and word2 at the end of merge.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> word1 = "abcabc", word2 = "abdcaba"
<strong>Output:</strong> "abdcabcabcaba"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= word1.length, word2.length &lt;= 3000 ``
*   `` word1 `` and `` word2 `` consist only of lowercase English letters.