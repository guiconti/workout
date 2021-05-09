Given an input string `` s ``, reverse the order of the __words__.

A __word__ is defined as a sequence of non-space characters. The __words__ in `` s `` will be separated by at least one space.

Return _a string of the words in reverse order concatenated by a single space._

__Note__ that `` s `` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "the sky is blue"
<strong>Output:</strong> "blue is sky the"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "  hello world  "
<strong>Output:</strong> "world hello"
<strong>Explanation:</strong> Your reversed string should not contain leading or trailing spaces.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "a good   example"
<strong>Output:</strong> "example good a"
<strong>Explanation:</strong> You need to reduce multiple spaces between two words to a single space in the reversed string.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "  Bob    Loves  Alice   "
<strong>Output:</strong> "Alice Loves Bob"
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "Alice does not even like bob"
<strong>Output:</strong> "bob like even not does Alice"
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>4</sup></code>
*   `` s `` contains English letters (upper-case and lower-case), digits, and spaces `` ' ' ``.
*   There is __at least one__ word in `` s ``.

&nbsp;

__Follow up:__ Could you solve it __in-place__ with `` O(1) `` extra space?