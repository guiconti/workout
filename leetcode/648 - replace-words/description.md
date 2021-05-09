In English, we have a concept called __root__, which can be followed by some other word&nbsp;to form another longer word - let's call this word __successor__. For example, when the __root__ `` "an" `` is&nbsp;followed by the __successor__&nbsp;word&nbsp;`` "other" ``, we&nbsp;can form a new word `` "another" ``.

Given a `` dictionary `` consisting of many __roots__ and a `` sentence ``&nbsp;consisting of words separated by spaces, replace all the __successors__ in the sentence with the __root__ forming it. If a __successor__ can be replaced by more than one __root__,&nbsp;replace it with the __root__ that has&nbsp;__the shortest length__.

Return _the `` sentence ``_ after the replacement.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
<strong>Output:</strong> "the cat was rat by the bat"
</pre>

__Example 2:__

<pre><strong>Input:</strong> dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
<strong>Output:</strong> "a a b c"
</pre>

__Example 3:__

<pre><strong>Input:</strong> dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
<strong>Output:</strong> "a a a a a a a a bbb baba a"
</pre>

__Example 4:__

<pre><strong>Input:</strong> dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
<strong>Output:</strong> "the cat was rat by the bat"
</pre>

__Example 5:__

<pre><strong>Input:</strong> dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
<strong>Output:</strong> "it is ab that this solution is ac"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= dictionary.length&nbsp;&lt;= 1000 ``
*   `` 1 &lt;= dictionary[i].length &lt;= 100 ``
*   `` dictionary[i] ``&nbsp;consists of only lower-case letters.
*   `` 1 &lt;= sentence.length &lt;= 10^6 ``
*   `` sentence ``&nbsp;consists of only lower-case letters and spaces.
*   The number of words in&nbsp;`` sentence ``&nbsp;is in the range `` [1, 1000] ``
*   The length of each word in&nbsp;`` sentence ``&nbsp;is in the range `` [1, 1000] ``
*   Each two consecutive words in&nbsp;`` sentence ``&nbsp;will be separated by exactly one space.
*   `` sentence ``&nbsp;does not have leading or trailing spaces.