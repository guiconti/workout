Given two version numbers,&nbsp;`` version1 `` and `` version2 ``, compare them.

Version numbers consist of __one or more revisions__ joined by a dot&nbsp;`` '.' ``. Each revision&nbsp;consists of __digits__&nbsp;and may contain leading __zeros__. Every revision contains __at least one character__. Revisions are __0-indexed from left to right__, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example&nbsp;`` 2.5.33 ``&nbsp;and&nbsp;`` 0.1 ``&nbsp;are valid version numbers.

To compare version numbers, compare their revisions in __left-to-right order__. Revisions are compared using their&nbsp;__integer value ignoring any leading zeros__. This means that revisions&nbsp;`` 1 ``&nbsp;and&nbsp;`` 001 ``&nbsp;are considered&nbsp;__equal__. If a version number does not specify a revision at an index, then&nbsp;__treat the revision as&nbsp;`` 0 ``__. For example, version&nbsp;`` 1.0 `` is less than version&nbsp;`` 1.1 ``&nbsp;because their revision 0s are the same, but their revision 1s are&nbsp;`` 0 ``&nbsp;and&nbsp;`` 1 ``&nbsp;respectively, and&nbsp;`` 0 &lt; 1 ``.

_Return the following:_

*   If `` version1 &lt; version2 ``, return `` -1 ``.
*   If `` version1 &gt; version2 ``, return `` 1 ``.
*   Otherwise, return `` 0 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> version1 = "1.01", version2 = "1.001"
<strong>Output:</strong> 0
<strong>Explanation:</strong> Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> version1 = "1.0", version2 = "1.0.0"
<strong>Output:</strong> 0
<strong>Explanation:</strong> version1 does not specify revision 2, which means it is treated as "0".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> version1 = "0.1", version2 = "1.1"
<strong>Output:</strong> -1
<strong>Explanation:</strong>&nbsp;version1's revision 0 is "0", while version2's revision 0 is "1". 0 &lt; 1, so version1 &lt; version2.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> version1 = "1.0.1", version2 = "1"
<strong>Output:</strong> 1
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> version1 = "7.5.2.4", version2 = "7.5.3"
<strong>Output:</strong> -1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= version1.length, version2.length &lt;= 500 ``
*   `` version1 `` and `` version2 ``&nbsp;only contain digits and `` '.' ``.
*   `` version1 `` and `` version2 ``&nbsp;__are valid version numbers__.
*   All the given revisions in&nbsp;`` version1 `` and `` version2 ``&nbsp;can be stored in&nbsp;a&nbsp;__32-bit integer__.