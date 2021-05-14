You are given a list of strings of the __same length__ `` words `` and a string `` target ``.

Your task is to form `` target `` using the given `` words `` under the following rules:

*   `` target `` should be formed from left to right.
*   To form the <code>i<sup>th</sup></code> character (__0-indexed__) of `` target ``, you can choose the <code>k<sup>th</sup></code> character of the <code>j<sup>th</sup></code> string in `` words `` if `` target[i] = words[j][k] ``.
*   Once you use the <code>k<sup>th</sup></code> character of the <code>j<sup>th</sup></code> string of `` words ``, you __can no longer__ use the <code>x<sup>th</sup></code> character of any string in `` words `` where `` x &lt;= k ``. In other words, all characters to the left of or at index `` k `` become unusuable for every string.
*   Repeat the process until you form the string `` target ``.

__Notice__&nbsp;that you can use __multiple characters__ from the __same string__ in `` words `` provided the conditions above are met.

Return _the number of ways to form `` target `` from `` words ``_. Since the answer may be too large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> words = ["acca","bbbb","caca"], target = "aba"
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are 6 ways to form target.
"aba" -&gt; index 0 ("<u>a</u>cca"), index 1 ("b<u>b</u>bb"), index 3 ("cac<u>a</u>")
"aba" -&gt; index 0 ("<u>a</u>cca"), index 2 ("bb<u>b</u>b"), index 3 ("cac<u>a</u>")
"aba" -&gt; index 0 ("<u>a</u>cca"), index 1 ("b<u>b</u>bb"), index 3 ("acc<u>a</u>")
"aba" -&gt; index 0 ("<u>a</u>cca"), index 2 ("bb<u>b</u>b"), index 3 ("acc<u>a</u>")
"aba" -&gt; index 1 ("c<u>a</u>ca"), index 2 ("bb<u>b</u>b"), index 3 ("acc<u>a</u>")
"aba" -&gt; index 1 ("c<u>a</u>ca"), index 2 ("bb<u>b</u>b"), index 3 ("cac<u>a</u>")
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> words = ["abba","baab"], target = "bab"
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 ways to form target.
"bab" -&gt; index 0 ("<u>b</u>aab"), index 1 ("b<u>a</u>ab"), index 2 ("ab<u>b</u>a")
"bab" -&gt; index 0 ("<u>b</u>aab"), index 1 ("b<u>a</u>ab"), index 3 ("baa<u>b</u>")
"bab" -&gt; index 0 ("<u>b</u>aab"), index 2 ("ba<u>a</u>b"), index 3 ("baa<u>b</u>")
"bab" -&gt; index 1 ("a<u>b</u>ba"), index 2 ("ba<u>a</u>b"), index 3 ("baa<u>b</u>")
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> words = ["abcd"], target = "abcd"
<strong>Output:</strong> 1
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> words = ["abab","baba","abba","baab"], target = "abba"
<strong>Output:</strong> 16
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= words.length &lt;= 1000 ``
*   `` 1 &lt;= words[i].length &lt;= 1000 ``
*   All strings in `` words `` have the same length.
*   `` 1 &lt;= target.length &lt;= 1000 ``
*   `` words[i] `` and `` target `` contain only lowercase English letters.