Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `` WordDictionary `` class:

*   `` WordDictionary() ``&nbsp;Initializes the object.
*   `` void addWord(word) `` Adds `` word `` to the data structure, it can be matched later.
*   `` bool search(word) ``&nbsp;Returns `` true `` if there is any string in the data structure that matches `` word ``&nbsp;or `` false `` otherwise. `` word `` may contain dots `` '.' `` where dots can be matched with any letter.

&nbsp;

__Example:__

<pre>
<strong>Input</strong>
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
<strong>Output</strong>
[null,null,null,null,false,true,true,true]

<strong>Explanation</strong>
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= word.length &lt;= 500 ``
*   `` word `` in `` addWord `` consists lower-case English letters.
*   `` word `` in `` search `` consist of&nbsp; `` '.' `` or lower-case English letters.
*   At most `` 50000 ``&nbsp;calls will be made to `` addWord ``&nbsp;and `` search ``.