__HTML entity parser__ is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

The special characters and their entities for HTML are:

*   __Quotation Mark:__&nbsp;the entity is `` &amp;quot; `` and&nbsp;symbol character is `` " ``.
*   __Single Quote&nbsp;Mark:__&nbsp;the entity is `` &amp;apos; `` and&nbsp;symbol character is `` ' ``.
*   __Ampersand:__&nbsp;the entity is `` &amp;amp; `` and symbol character is `` &amp; ``.
*   __Greater Than Sign:__&nbsp;the entity is `` &amp;gt; ``&nbsp;and symbol character is `` &gt; ``.
*   __Less Than Sign:__&nbsp;the entity is `` &amp;lt; ``&nbsp;and symbol character is `` &lt; ``.
*   __Slash:__&nbsp;the entity is `` &amp;frasl; `` and&nbsp;symbol character is `` / ``.

Given the input `` text `` string to the HTML parser, you have to implement the entity parser.

Return _the text_ after replacing the entities by the special characters.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> text = "&amp;amp; is an HTML entity but &amp;ambassador; is not."
<strong>Output:</strong> "&amp; is an HTML entity but &amp;ambassador; is not."
<strong>Explanation:</strong> The parser will replace the &amp;amp; entity by &amp;
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> text = "and I quote: &amp;quot;...&amp;quot;"
<strong>Output:</strong> "and I quote: \"...\""
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> text = "Stay home! Practice on Leetcode :)"
<strong>Output:</strong> "Stay home! Practice on Leetcode :)"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> text = "x &amp;gt; y &amp;amp;&amp;amp; x &amp;lt; y is always false"
<strong>Output:</strong> "x &gt; y &amp;&amp; x &lt; y is always false"
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> text = "leetcode.com&amp;frasl;problemset&amp;frasl;all"
<strong>Output:</strong> "leetcode.com/problemset/all"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= text.length &lt;= 10^5 ``
*   The string may contain any possible characters out of all the 256&nbsp;ASCII characters.