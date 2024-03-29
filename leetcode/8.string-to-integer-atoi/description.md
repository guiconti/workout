Implement the `` myAtoi(string s) `` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `` atoi `` function).

The algorithm for `` myAtoi(string s) `` is as follows:

1.   Read in and ignore any leading whitespace.
2.   Check if the next character (if not already at the end of the string) is `` '-' `` or `` '+' ``. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3.   Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
4.   Convert these digits into an integer (i.e. `` "123" -&gt; 123 ``, `` "0032" -&gt; 32 ``). If no digits were read, then the integer is `` 0 ``. Change the sign as necessary (from step 2).
5.   If the integer is out of the 32-bit signed integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then clamp the integer so that it remains in the range. Specifically, integers less than <code>-2<sup>31</sup></code> should be clamped to <code>-2<sup>31</sup></code>, and integers greater than <code>2<sup>31</sup> - 1</code> should be clamped to <code>2<sup>31</sup> - 1</code>.
6.   Return the integer as the final result.

__Note:__

*   Only the space character `` ' ' `` is considered a whitespace character.
*   __Do not ignore__ any characters other than the leading whitespace or the rest of the string after the digits.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "42"
<strong>Output:</strong> 42
<strong>Explanation:</strong> The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "<u>42</u>" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is 42.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "   -42"
<strong>Output:</strong> -42
<strong>Explanation:</strong>
Step 1: "<u>   </u>-42" (leading whitespace is read and ignored)
            ^
Step 2: "   <u>-</u>42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -<u>42</u>" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is -42.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "4193 with words"
<strong>Output:</strong> 4193
<strong>Explanation:</strong>
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "<u>4193</u> with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is 4193.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "words and 987"
<strong>Output:</strong> 0
<strong>Explanation:
</strong>Step 1: "words and 987" (no characters read because there is no leading whitespace)
         ^
Step 2: "words and 987" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "words and 987" (reading stops immediately because there is a non-digit 'w')
         ^
The parsed integer is 0 because no digits were read.
Since 0 is in the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is 0.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "-91283472332"
<strong>Output:</strong> -2147483648
<strong>Explanation:
</strong>Step 1: "-91283472332" (no characters read because there is no leading whitespace)
         ^
Step 2: "<u>-</u>91283472332" ('-' is read, so the result should be negative)
          ^
Step 3: "-<u>91283472332</u>" ("91283472332" is read in)
                     ^
The parsed integer is -91283472332.
Since -91283472332 is less than the lower bound of the range [-2<sup>31</sup>, 2<sup>31</sup> - 1], the final result is clamped to -2<sup>31</sup> = -2147483648.<strong><span style="display: none;"> </span></strong>
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= s.length &lt;= 200 ``
*   `` s `` consists of English letters (lower-case and upper-case), digits (`` 0-9 ``), `` ' ' ``, `` '+' ``, `` '-' ``, and `` '.' ``.