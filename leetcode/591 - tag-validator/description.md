Given a string representing a code snippet, implement a tag validator to parse the code and return whether it is valid.

A code snippet is valid if all the following rules hold:

1.   The code must be wrapped in a __valid closed tag__. Otherwise, the code is invalid.
2.   A __closed tag__ (not necessarily valid) has exactly the following format : `` &lt;TAG_NAME&gt;TAG_CONTENT&lt;/TAG_NAME&gt; ``. Among them, `` &lt;TAG_NAME&gt; `` is the start tag, and `` &lt;/TAG_NAME&gt; `` is the end tag. The TAG\_NAME in start and end tags should be the same. A closed tag is __valid__ if and only if the TAG\_NAME and TAG\_CONTENT are valid.
3.   A __valid__ `` TAG_NAME `` only contain __upper-case letters__, and has length in range \[1,9\]. Otherwise, the `` TAG_NAME `` is __invalid__.
4.   A __valid__ `` TAG_CONTENT `` may contain other __valid closed tags__, __cdata__ and any characters (see note1) __EXCEPT__ unmatched `` &lt; ``, unmatched start and end tag, and unmatched or closed tags with invalid TAG\_NAME. Otherwise, the `` TAG_CONTENT `` is __invalid__.
5.   A start tag is unmatched if no end tag exists with the same TAG\_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
6.   A `` &lt; `` is unmatched if you cannot find a subsequent `` &gt; ``. And when you find a `` &lt; `` or `` &lt;/ ``, all the subsequent characters until the next `` &gt; `` should be parsed as TAG\_NAME (not necessarily valid).
7.   The cdata has the following format : `` &lt;![CDATA[CDATA_CONTENT]]&gt; ``. The range of `` CDATA_CONTENT `` is defined as the characters between `` &lt;![CDATA[ `` and the __first subsequent__ `` ]]&gt; ``.
8.   `` CDATA_CONTENT `` may contain __any characters__. The function of cdata is to forbid the validator to parse `` CDATA_CONTENT ``, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as __regular characters__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> code = "&lt;DIV&gt;This is the first line &lt;![CDATA[&lt;div&gt;]]&gt;&lt;/DIV&gt;"
<strong>Output:</strong> true
<strong>Explanation:</strong> 
The code is wrapped in a closed tag : &lt;DIV&gt; and &lt;/DIV&gt;. 
The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata. 
Although CDATA_CONTENT has an unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as a tag.
So TAG_CONTENT is valid, and then the code is valid. Thus return true.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> code = "&lt;DIV&gt;&gt;&gt;  ![cdata[]] &lt;![CDATA[&lt;div&gt;]&gt;]]&gt;]]&gt;&gt;]&lt;/DIV&gt;"
<strong>Output:</strong> true
<strong>Explanation:</strong>
We first separate the code into : start_tag|tag_content|end_tag.
start_tag -&gt; <b>"&lt;DIV&gt;"</b>
end_tag -&gt; <b>"&lt;/DIV&gt;"</b>
tag_content could also be separated into : text1|cdata|text2.
text1 -&gt; <b>"&gt;&gt;  ![cdata[]] "</b>
cdata -&gt; <b>"&lt;![CDATA[&lt;div&gt;]&gt;]]&gt;"</b>, where the CDATA_CONTENT is <b>"&lt;div&gt;]&gt;"</b>
text2 -&gt; <b>"]]&gt;&gt;]"</b>
The reason why start_tag is NOT <b>"&lt;DIV&gt;&gt;&gt;"</b> is because of the rule 6.
The reason why cdata is NOT <b>"&lt;![CDATA[&lt;div&gt;]&gt;]]&gt;]]&gt;"</b> is because of the rule 7.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> code = "&lt;A&gt;  &lt;B&gt; &lt;/A&gt;   &lt;/B&gt;"
<strong>Output:</strong> false
<strong>Explanation:</strong> Unbalanced. If "&lt;A&gt;" is closed, then "&lt;B&gt;" must be unmatched, and vice versa.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> code = "&lt;DIV&gt;  div tag is not closed  &lt;DIV&gt;"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= code.length &lt;= 500 ``
*   `` code `` consists of English letters, digits, `` '&lt;' ``, `` '&gt;' ``, `` '/' ``, `` '!' ``, `` '[' ``, `` ']' ``, `` '.' ``, and `` ' ' ``.