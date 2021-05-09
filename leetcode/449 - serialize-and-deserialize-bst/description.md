Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a __binary search tree__. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

__The encoded string should be as compact as possible.__

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> [2,1,3]
</pre>

__Example 2:__

<pre><strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.
*   <code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code>
*   The input tree is __guaranteed__ to be a binary search tree.