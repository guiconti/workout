You are given two strings `` a `` and `` b `` of the same length. Choose an index and split both strings __at the same index__, splitting `` a `` into two strings: <code>a<sub>prefix</sub></code> and <code>a<sub>suffix</sub></code> where <code>a = a<sub>prefix</sub> + a<sub>suffix</sub></code>, and splitting `` b `` into two strings: <code>b<sub>prefix</sub></code> and <code>b<sub>suffix</sub></code> where <code>b = b<sub>prefix</sub> + b<sub>suffix</sub></code>. Check if <code>a<sub>prefix</sub> + b<sub>suffix</sub></code> or <code>b<sub>prefix</sub> + a<sub>suffix</sub></code> forms a palindrome.

When you split a string `` s `` into <code>s<sub>prefix</sub></code> and <code>s<sub>suffix</sub></code>, either <code>s<sub>suffix</sub></code> or <code>s<sub>prefix</sub></code> is allowed to be empty. For example, if `` s = "abc" ``, then `` "" + "abc" ``, `` "a" + "bc" ``, `` "ab" + "c" `` , and `` "abc" + "" `` are valid splits.

Return `` true ``_ if it is possible to form__ a palindrome string, otherwise return _`` false ``.

__Notice__ that&nbsp;`` x + y `` denotes the concatenation of strings `` x `` and `` y ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> a = "x", b = "y"
<strong>Output:</strong> true
<strong>Explaination:</strong> If either a or b are palindromes the answer is true since you can split in the following way:
a<sub>prefix</sub> = "", a<sub>suffix</sub> = "x"
b<sub>prefix</sub> = "", b<sub>suffix</sub> = "y"
Then, a<sub>prefix</sub> + b<sub>suffix</sub> = "" + "y" = "y", which is a palindrome.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> a = "abdef", b = "fecab"
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> a = "ulacfd", b = "jizalu"
<strong>Output:</strong> true
<strong>Explaination:</strong> Split them at index 3:
a<sub>prefix</sub> = "ula", a<sub>suffix</sub> = "cfd"
b<sub>prefix</sub> = "jiz", b<sub>suffix</sub> = "alu"
Then, a<sub>prefix</sub> + b<sub>suffix</sub> = "ula" + "alu" = "ulaalu", which is a palindrome.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> a = "xbdef", b = "xecab"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= a.length, b.length &lt;= 10<sup>5</sup></code>
*   `` a.length == b.length ``
*   `` a `` and `` b `` consist of lowercase English letters