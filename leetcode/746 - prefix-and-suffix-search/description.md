Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the `` WordFilter `` class:

*   `` WordFilter(string[] words) `` Initializes the object with the `` words `` in the dictionary.
*   `` f(string prefix, string suffix) `` Returns _the index of the word in the dictionary,_ which has the prefix `` prefix `` and the suffix `` suffix ``. If there is more than one valid index, return __the largest__ of them. If there is no such word in the dictionary, return `` -1 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
<strong>Output</strong>
[null, 0]

<strong>Explanation</strong>
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= words.length &lt;= 15000 ``
*   `` 1 &lt;= words[i].length &lt;= 10 ``
*   `` 1 &lt;= prefix.length, suffix.length &lt;= 10 ``
*   `` words[i] ``, `` prefix `` and `` suffix `` consist of lower-case English letters only.
*   At most `` 15000 `` calls will be made to the function `` f ``.