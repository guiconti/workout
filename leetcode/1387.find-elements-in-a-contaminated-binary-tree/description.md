Given a&nbsp;binary tree with the following rules:

1.   `` root.val == 0 ``
2.   If `` treeNode.val == x `` and `` treeNode.left != null ``, then `` treeNode.left.val == 2 * x + 1 ``
3.   If `` treeNode.val == x `` and `` treeNode.right != null ``, then `` treeNode.right.val == 2 * x + 2 ``

Now the binary tree is contaminated, which means all&nbsp;`` treeNode.val ``&nbsp;have&nbsp;been changed to `` -1 ``.

You need to first recover the binary tree and then implement the `` FindElements `` class:

*   `` FindElements(TreeNode* root) ``&nbsp;Initializes the object with a&nbsp;contamined binary tree, you need to recover it first.
*   `` bool find(int target) ``&nbsp;Return if the `` target `` value exists in the recovered binary tree.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/11/06/untitled-diagram-4-1.jpg" style="width: 320px; height: 119px;"/></strong>

<pre>
<strong>Input</strong>
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
<strong>Output</strong>
[null,false,true]
<strong>Explanation</strong>
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True </pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/11/06/untitled-diagram-4.jpg" style="width: 400px; height: 198px;"/></strong>

<pre>
<strong>Input</strong>
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
<strong>Output</strong>
[null,true,true,false]
<strong>Explanation</strong>
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False</pre>

__Example 3:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/11/07/untitled-diagram-4-1-1.jpg" style="width: 306px; height: 274px;"/></strong>

<pre>
<strong>Input</strong>
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
<strong>Output</strong>
[null,true,false,false,true]
<strong>Explanation</strong>
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
</pre>

&nbsp;

__Constraints:__

*   `` TreeNode.val == -1 ``
*   The height of the binary tree is less than or equal to `` 20 ``
*   The total number of nodes is between `` [1,&nbsp;10^4] ``
*   Total calls of `` find() `` is between `` [1,&nbsp;10^4] ``
*   `` 0 &lt;= target &lt;= 10^6 ``