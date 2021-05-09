We are given `` n `` different types of `` stickers ``. Each sticker has a lowercase English word on it.

You would like to spell out the given string `` target `` by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

Return _the minimum number of stickers that you need to spell out _`` target ``. If the task is impossible, return `` -1 ``.

__Note:__ In all test cases, all words were chosen randomly from the `` 1000 `` most common US English words, and `` target `` was chosen as a concatenation of two random words.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> stickers = ["with","example","science"], target = "thehat"
<strong>Output:</strong> 3
<strong>Explanation:</strong>
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> stickers = ["notice","possible"], target = "basicbasic"
<strong>Output:</strong> -1
Explanation:
We cannot form the target "basicbasic" from cutting letters from the given stickers.
</pre>

&nbsp;

__Constraints:__

*   `` n == stickers.length ``
*   `` 1 &lt;= n &lt;= 50 ``
*   `` 1 &lt;= stickers[i].length &lt;= 10 ``
*   `` 1 &lt;= target &lt;= 15 ``
*   `` stickers[i] `` and `` target `` consist of lowercase English letters.