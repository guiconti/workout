A sentence `` S `` is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "_Goat Latin"_&nbsp;(a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

*   If a word begins with a vowel (a, e, i, o, or u), append `` "ma" ``&nbsp;to the end of the word.  
    
    
*   If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add `` "ma" ``.  
    
    
*   Add one letter `` 'a' ``&nbsp;to the end of each word per its word index in the sentence, starting with 1.  
    

Return the&nbsp;final sentence representing the conversion from `` S ``&nbsp;to Goat&nbsp;Latin.&nbsp;

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>"I speak Goat Latin"
<strong>Output: </strong>"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
</pre>

__Example 2:__

<pre>
<strong>Input: </strong>"The quick brown fox jumped over the lazy dog"
<strong>Output: </strong>"heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
</pre>

&nbsp;

Notes:

*   `` S `` contains only uppercase, lowercase and spaces.&nbsp;Exactly one space between each word.
*   `` 1 &lt;= S.length &lt;= 150 ``.