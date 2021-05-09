Given two stings `` ransomNote `` and `` magazine ``, return `` true `` if `` ransomNote `` can be constructed from `` magazine `` and `` false `` otherwise.

Each letter in `` magazine `` can only be used once in `` ransomNote ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> ransomNote = "a", magazine = "b"
<strong>Output:</strong> false
</pre>

__Example 2:__

<pre><strong>Input:</strong> ransomNote = "aa", magazine = "ab"
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre><strong>Input:</strong> ransomNote = "aa", magazine = "aab"
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= ransomNote.length, magazine.length &lt;= 10<sup>5</sup></code>
*   `` ransomNote `` and `` magazine `` consist of lowercase English letters.