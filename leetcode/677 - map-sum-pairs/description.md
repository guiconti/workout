Implement the `` MapSum `` class:

*   `` MapSum() `` Initializes the&nbsp;`` MapSum `` object.
*   `` void insert(String key, int val) `` Inserts the `` key-val `` pair into the map. If the `` key `` already existed, the original `` key-value `` pair will be overridden to the new one.
*   `` int sum(string prefix) `` Returns&nbsp;the sum of all the pairs' value whose `` key `` starts with the `` prefix ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
<strong>Output</strong>
[null, null, 3, null, 5]

<strong>Explanation</strong>
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (<u>ap</u>ple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (<u>ap</u>ple + <u>ap</u>p = 3 + 2 = 5)
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= key.length, prefix.length &lt;= 50 ``
*   `` key `` and `` prefix `` consist of only lowercase English letters.
*   `` 1 &lt;= val &lt;= 1000 ``
*   At most `` 50 `` calls will be made to `` insert `` and `` sum ``.