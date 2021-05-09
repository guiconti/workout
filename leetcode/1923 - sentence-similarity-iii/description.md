A sentence is a list of words that are separated by a single space with no leading or trailing spaces. For example, `` "Hello World" ``, `` "HELLO" ``, `` "hello world hello world" `` are all sentences. Words consist of __only__ uppercase and lowercase English letters.

Two sentences `` sentence1 `` and `` sentence2 `` are __similar__ if it is possible to insert an arbitrary sentence __(possibly empty)__ inside one of these sentences such that the two sentences become equal. For example, `` sentence1 = "Hello my name is Jane" `` and `` sentence2 = "Hello Jane" `` can be made equal by inserting `` "my name is" `` between `` "Hello" `` and `` "Jane" `` in `` sentence2 ``.

Given two sentences `` sentence1 `` and `` sentence2 ``, return `` true `` _if _`` sentence1 `` _and _`` sentence2 `` _are similar._ Otherwise, return `` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> sentence1 = "My name is Haley", sentence2 = "My Haley"
<strong>Output:</strong> true
<strong>Explanation:</strong> sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> sentence1 = "of", sentence2 = "A lot of words"
<strong>Output:</strong> false
<strong>Explanation: </strong>No single sentence can be inserted inside one of the sentences to make it equal to the other.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> sentence1 = "Eating right now", sentence2 = "Eating"
<strong>Output:</strong> true
<strong>Explanation:</strong> sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> sentence1 = "Luky", sentence2 = "Lucccky"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= sentence1.length, sentence2.length &lt;= 100 ``
*   `` sentence1 `` and `` sentence2 `` consist of lowercase and uppercase English letters and spaces.
*   The words in `` sentence1 `` and `` sentence2 `` are separated by a single space.