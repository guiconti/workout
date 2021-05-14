A valid parentheses string is either empty `` ("") ``, `` "(" + A + ")" ``, or `` A + B ``, where `` A `` and `` B `` are valid parentheses strings, and `` + `` represents string concatenation.&nbsp; For example, `` "" ``, `` "()" ``, `` "(())()" ``, and `` "(()(()))" `` are all valid parentheses strings.

A valid parentheses string `` S `` is __primitive__ if it is nonempty, and there does not exist a way to split it into `` S = A+B ``, with `` A `` and `` B `` nonempty valid parentheses strings.

Given a valid parentheses string `` S ``, consider its primitive decomposition: `` S = P_1 + P_2 + ... + P_k ``, where `` P_i `` are primitive valid parentheses strings.

Return `` S `` after removing the outermost parentheses of every primitive string in the primitive decomposition of `` S ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">"(()())(())"</span>
<strong>Output: </strong><span id="example-output-1">"()()()"</span>
<strong>Explanation: </strong>
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">"(()())(())(()(()))"</span>
<strong>Output: </strong><span id="example-output-2">"()()()()(())"</span>
<strong>Explanation: </strong>
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-3-1">"()()"</span>
<strong>Output: </strong><span id="example-output-3">""</span>
<strong>Explanation: </strong>
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
</pre>
<p>&nbsp;</p>
</div>
</div>

__Note:__

1.   `` S.length &lt;= 10000 ``
2.   `` S[i] `` is `` "(" `` or `` ")" ``
3.   `` S `` is a valid parentheses string

<div>
<div>
<div>&nbsp;</div>
</div>
</div>