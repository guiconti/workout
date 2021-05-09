Given the string `` s ``, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "eleetminicoworoep"
<strong>Output:</strong> 13
<strong>Explanation: </strong>The longest substring is "leetminicowor" which contains two each of the vowels: <strong>e</strong>, <strong>i</strong> and <strong>o</strong> and zero of the vowels: <strong>a</strong> and <strong>u</strong>.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "leetcodeisgreat"
<strong>Output:</strong> 5
<strong>Explanation:</strong> The longest substring is "leetc" which contains two e's.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "bcbcbc"
<strong>Output:</strong> 6
<strong>Explanation:</strong> In this case, the given string "bcbcbc" is the longest because all vowels: <strong>a</strong>, <strong>e</strong>, <strong>i</strong>, <strong>o</strong> and <strong>u</strong> appear zero times.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 5 x 10^5 ``
*   `` s ``&nbsp;contains only lowercase English letters.