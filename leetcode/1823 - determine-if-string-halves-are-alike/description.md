You are given a string `` s `` of even length. Split this string into two halves of equal lengths, and let `` a `` be the first half and `` b `` be the second half.

Two strings are __alike__ if they have the same number of vowels (`` 'a' ``, `` 'e' ``, `` 'i' ``, `` 'o' ``, `` 'u' ``, `` 'A' ``, `` 'E' ``, `` 'I' ``, `` 'O' ``, `` 'U' ``). Notice that `` s `` contains uppercase and lowercase letters.

Return `` true ``_ if _`` a ``_ and _`` b ``_ are __alike___. Otherwise, return `` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "book"
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;a = "b<u>o</u>" and b = "<u>o</u>k". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "textbook"
<strong>Output:</strong> false
<strong>Explanation:</strong>&nbsp;a = "t<u>e</u>xt" and b = "b<u>oo</u>k". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "MerryChristmas"
<strong>Output:</strong> false
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "AbCdEfGh"
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= s.length &lt;= 1000 ``
*   `` s.length `` is even.
*   `` s `` consists of __uppercase and lowercase__ letters.