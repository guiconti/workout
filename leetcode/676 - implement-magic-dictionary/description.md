Design a data structure that is initialized with a list of __different__ words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.

Implement the&nbsp;`` MagicDictionary ``&nbsp;class:

*   `` MagicDictionary() ``&nbsp;Initializes the object.
*   `` void buildDict(String[]&nbsp;dictionary) ``&nbsp;Sets the data structure&nbsp;with an array of distinct strings `` dictionary ``.
*   `` bool search(String searchWord) `` Returns `` true `` if you can change __exactly one character__ in `` searchWord `` to match any string in the data structure, otherwise returns `` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
<strong>Output</strong>
[null, null, false, true, false, false]

<strong>Explanation</strong>
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;=&nbsp;dictionary.length &lt;= 100 ``
*   `` 1 &lt;=&nbsp;dictionary[i].length &lt;= 100 ``
*   `` dictionary[i] `` consists of only lower-case English letters.
*   All the strings in&nbsp;`` dictionary ``&nbsp;are __distinct__.
*   `` 1 &lt;=&nbsp;searchWord.length &lt;= 100 ``
*   `` searchWord ``&nbsp;consists of only lower-case English letters.
*   `` buildDict ``&nbsp;will be called only once before `` search ``.
*   At most `` 100 `` calls will be made to `` search ``.