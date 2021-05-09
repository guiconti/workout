Given an array of characters `` chars ``, compress it using the following algorithm:

Begin with an empty string `` s ``. For each group of __consecutive repeating characters__ in `` chars ``:

*   If the group's length is 1, append the character to&nbsp;`` s ``.
*   Otherwise, append the character followed by the group's length.

The compressed string&nbsp;`` s `` __should not be returned separately__, but instead be stored&nbsp;__in the input character array&nbsp;`` chars ``__. Note that group lengths that are 10 or longer will be split into multiple characters in&nbsp;`` chars ``.

After you are done __modifying the input array__, return _the new length of the array_.

&nbsp;

__Follow up:__  
Could you solve it using only `` O(1) `` extra space?

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> chars = ["a","a","b","b","c","c","c"]
<strong>Output:</strong> Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
<strong>Explanation:</strong>&nbsp;The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> chars = ["a"]
<strong>Output:</strong> Return 1, and the first character of the input array should be: ["a"]
<strong>Explanation:</strong>&nbsp;The only group is "a", which remains uncompressed since it's a single character.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
<strong>Output:</strong> Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
<strong>Explanation:</strong>&nbsp;The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".</pre>

__Example 4:__

<pre>
<strong>Input:</strong> chars = ["a","a","a","b","b","a","a"]
<strong>Output:</strong> Return 6, and the first 6 characters of the input array should be: ["a","3","b","2","a","2"].
<strong>Explanation:</strong>&nbsp;The groups are "aaa", "bb", and "aa". This compresses to "a3b2a2". Note that each group is independent even if two groups have the same character.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= chars.length &lt;= 2000 ``
*   `` chars[i] `` is a lower-case English letter, upper-case English letter, digit, or symbol.