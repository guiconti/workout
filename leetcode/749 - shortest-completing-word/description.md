Given a string `` licensePlate `` and an array of strings `` words ``, find the __shortest completing__ word in `` words ``.

A __completing__ word is a word that __contains all the letters__ in `` licensePlate ``. __Ignore numbers and spaces__ in `` licensePlate ``, and treat letters as __case insensitive__. If a letter appears more than once in `` licensePlate ``, then it must appear in the word the same number of times or more.

For example, if `` licensePlate ````  = "aBc 12c" ``, then it contains letters `` 'a' ``, `` 'b' `` (ignoring case), and `` 'c' `` twice. Possible __completing__ words are `` "abccdef" ``, `` "caaacab" ``, and `` "cbca" ``.

Return _the shortest __completing__ word in _`` words ``_._ It is guaranteed an answer exists. If there are multiple shortest __completing__ words, return the __first__ one that occurs in `` words ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
<strong>Output:</strong> "steps"
<strong>Explanation:</strong> licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
<strong>Output:</strong> "pest"
<strong>Explanation:</strong> licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> licensePlate = "Ah71752", words = ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]
<strong>Output:</strong> "husband"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> licensePlate = "OgEu755", words = ["enough","these","play","wide","wonder","box","arrive","money","tax","thus"]
<strong>Output:</strong> "enough"
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> licensePlate = "iMSlpe4", words = ["claim","consumer","student","camera","public","never","wonder","simple","thought","use"]
<strong>Output:</strong> "simple"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= licensePlate.length &lt;= 7 ``
*   `` licensePlate `` contains digits, letters (uppercase or lowercase), or space `` ' ' ``.
*   `` 1 &lt;= words.length &lt;= 1000 ``
*   `` 1 &lt;= words[i].length &lt;= 15 ``
*   `` words[i] `` consists of lower case English letters.