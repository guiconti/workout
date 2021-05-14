Two strings `` X ``&nbsp;and `` Y ``&nbsp;are similar if we can swap two letters (in different positions) of `` X ``, so that&nbsp;it equals `` Y ``. Also two strings `` X `` and `` Y `` are similar if they are equal.

For example, `` "tars" ``&nbsp;and `` "rats" ``&nbsp;are similar (swapping at positions `` 0 `` and `` 2 ``), and `` "rats" `` and `` "arts" `` are similar, but `` "star" `` is not similar to `` "tars" ``, `` "rats" ``, or `` "arts" ``.

Together, these form two connected groups by similarity: `` {"tars", "rats", "arts"} `` and `` {"star"} ``.&nbsp; Notice that `` "tars" `` and `` "arts" `` are in the same group even though they are not similar.&nbsp; Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list `` strs `` of strings where every string in `` strs `` is an anagram of every other string in `` strs ``. How many groups are there?

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> strs = ["tars","rats","arts","star"]
<strong>Output:</strong> 2
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> strs = ["omv","ovm"]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= strs.length &lt;= 300 ``
*   `` 1 &lt;= strs[i].length &lt;= 300 ``
*   `` strs[i] `` consists of lowercase letters only.
*   All words in `` strs `` have the same length and are anagrams of each other.