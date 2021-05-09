You are playing the __<a href="https://en.wikipedia.org/wiki/Bulls_and_Cows" target="_blank">Bulls and Cows</a>__ game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

*   The number of "bulls", which are digits in the guess that are in the correct position.
*   The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

Given the secret number `` secret `` and your friend's guess `` guess ``, return _the hint for your friend's guess_.

The hint should be formatted as `` "xAyB" ``, where `` x `` is the number of bulls and `` y `` is the number of cows. Note that both `` secret `` and `` guess `` may contain duplicate digits.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> secret = "1807", guess = "7810"
<strong>Output:</strong> "1A3B"
<strong>Explanation:</strong> Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"<u>7</u>8<u>10</u>"</pre>

__Example 2:__

<pre>
<strong>Input:</strong> secret = "1123", guess = "0111"
<strong>Output:</strong> "1A1B"
<strong>Explanation:</strong> Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"01<u>1</u>1"        "011<u>1</u>"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> secret = "1", guess = "0"
<strong>Output:</strong> "0A0B"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> secret = "1", guess = "1"
<strong>Output:</strong> "1A0B"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= secret.length, guess.length &lt;= 1000 ``
*   `` secret.length == guess.length ``
*   `` secret `` and `` guess `` consist of digits only.