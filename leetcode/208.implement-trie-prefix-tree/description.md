A <a href="https://en.wikipedia.org/wiki/Trie" target="_blank">__trie__</a> (pronounced as "try") or __prefix tree__ is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

*   `` Trie() `` Initializes the trie object.
*   `` void insert(String word) `` Inserts the string `` word `` into the trie.
*   `` boolean search(String word) `` Returns `` true `` if the string `` word `` is in the trie (i.e., was inserted before), and `` false `` otherwise.
*   `` boolean startsWith(String prefix) `` Returns `` true `` if there is a previously inserted string `` word `` that has the prefix `` prefix ``, and `` false `` otherwise.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
<strong>Output</strong>
[null, null, true, false, true, null, true]

<strong>Explanation</strong>
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= word.length, prefix.length &lt;= 2000 ``
*   `` word `` and `` prefix `` consist only of lowercase English letters.
*   At most <code>3 * 10<sup>4</sup></code> calls __in total__ will be made to `` insert ``, `` search ``, and `` startsWith ``.