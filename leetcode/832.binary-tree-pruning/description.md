We are given the head node `` root ``&nbsp;of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> [1,null,0,0,1]
<strong>Output: </strong>[1,null,0,null,1]
 
<strong>Explanation:</strong> 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png" style="width:450px"/>
</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> [1,0,1,0,0,0,1]
<strong>Output: </strong>[1,null,1,null,1]

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png" style="width:450px"/>
</pre>

<pre>
<strong>Example 3:</strong>
<strong>Input:</strong> [1,1,0,1,1,0,1,0]
<strong>Output: </strong>[1,1,0,1,1,null,1]

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png" style="width:450px"/>
</pre>

__Note: __

*   The binary tree&nbsp;will&nbsp;have&nbsp;at&nbsp;most `` 200 nodes ``.
*   The value of each node will only be `` 0 `` or `` 1 ``.