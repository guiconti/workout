Given two strings&nbsp;`` s `` and `` t ``, you want to transform string&nbsp;`` s `` into string&nbsp;`` t `` using the following&nbsp;operation any number of times:

*   Choose a __non-empty__ substring in&nbsp;`` s ``&nbsp;and sort it in-place&nbsp;so the characters are in&nbsp;__ascending order__.

For example, applying the operation on the underlined substring in&nbsp;<code>"1<u>4234</u>"</code>&nbsp;results in <code>"1<u>2344</u>"</code>.

Return `` true `` if _it is possible to transform string `` s ``&nbsp;into string `` t ``_. Otherwise,&nbsp;return `` false ``.

A __substring__&nbsp;is a contiguous sequence of characters within a string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "84532", t = "34852"
<strong>Output:</strong> true
<strong>Explanation:</strong> You can transform s into t using the following sort operations:
"84<u>53</u>2" (from index 2 to 3) -&gt; "84<u>35</u>2"
"<u>843</u>52" (from index 0 to 2) -&gt; "<u>348</u>52"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "34521", t = "23415"
<strong>Output:</strong> true
<strong>Explanation:</strong> You can transform s into t using the following sort operations:
"<u>3452</u>1" -&gt; "<u>2345</u>1"
"234<u>51</u>" -&gt; "234<u>15</u>"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "12345", t = "12435"
<strong>Output:</strong> false
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "1", t = "2"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` s.length == t.length ``
*   <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
*   `` s `` and `` t ``&nbsp;only contain digits from `` '0' `` to `` '9' ``.