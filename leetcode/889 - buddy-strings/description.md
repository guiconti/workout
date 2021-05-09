Given two strings `` a `` and `` b ``, return `` true ``_ if you can swap two letters in _`` a ``_ so the result is equal to _`` b ``_, otherwise, return _`` false ``_._

Swapping letters is defined as taking two indices `` i `` and `` j `` (0-indexed) such that `` i != j `` and swapping the characters at `` a[i] `` and `` a[j] ``.

*   For example, swapping at indices `` 0 `` and `` 2 `` in `` "abcd" `` results in `` "cbad" ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> a = "ab", b = "ba"
<strong>Output:</strong> true
<strong>Explanation:</strong> You can swap a[0] = 'a' and a[1] = 'b' to get "ba", which is equal to b.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> a = "ab", b = "ab"
<strong>Output:</strong> false
<strong>Explanation:</strong> The only letters you can swap are a[0] = 'a' and a[1] = 'b', which results in "ba" != b.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> a = "aa", b = "aa"
<strong>Output:</strong> true
<strong>Explanation:</strong> You can swap a[0] = 'a' and a[1] = 'a' to get "aa", which is equal to b.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> a = "aaaaaaabc", b = "aaaaaaacb"
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= a.length, b.length &lt;= 2 * 10<sup>4</sup></code>
*   `` a `` and `` b `` consist of lowercase letters.