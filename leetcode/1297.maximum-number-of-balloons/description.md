Given a string `` text ``, you want to use the characters of `` text `` to form as many instances of the word __"balloon"__ as possible.

You can use each character in `` text `` __at most once__. Return the maximum number of instances that can be formed.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG" style="width: 132px; height: 35px;"/></strong>

<pre>
<strong>Input:</strong> text = "nlaebolko"
<strong>Output:</strong> 1
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG" style="width: 267px; height: 35px;"/></strong>

<pre>
<strong>Input:</strong> text = "loonbalxballpoon"
<strong>Output:</strong> 2
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> text = "leetcode"
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= text.length &lt;= 10<sup>4</sup></code>
*   `` text `` consists of lower case English letters only.