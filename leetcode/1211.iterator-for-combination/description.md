Design the `` CombinationIterator `` class:

*   `` CombinationIterator(string characters, int combinationLength) ``&nbsp;Initializes the object with&nbsp;a string&nbsp;`` characters ``&nbsp;of __sorted distinct__ lowercase English letters and a number&nbsp;`` combinationLength `` as arguments.
*   `` next() ``&nbsp;Returns the next combination of length `` combinationLength ``&nbsp;in __lexicographical order__.
*   `` hasNext() ``&nbsp;Returns `` true ``&nbsp;if and only if&nbsp;there exists a next combination.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
<strong>Output</strong>
[null, "ab", true, "ac", true, "bc", false]

<strong>Explanation</strong>
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= combinationLength &lt;=&nbsp;characters.length &lt;= 15 ``
*   All the characters of `` characters `` are __unique__.
*   At most <code>10<sup>4</sup></code>&nbsp;calls will be made to `` next `` and `` hasNext ``.
*   It's guaranteed that all&nbsp;calls&nbsp;of the function `` next ``&nbsp;are valid.