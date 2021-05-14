You are given a string `` s `` of lowercase English letters and an array `` widths `` denoting __how many pixels wide__ each lowercase English letter is. Specifically, `` widths[0] `` is the width of `` 'a' ``, `` widths[1] `` is the width of `` 'b' ``, and so on.

You are trying to write `` s `` across several lines, where __each line is no longer than __`` 100 ``__ pixels__. Starting at the beginning of `` s ``, write as many letters on the first line such that the total width does not exceed `` 100 `` pixels. Then, from where you stopped in `` s ``, continue writing as many letters as you can on the second line. Continue this process until you have written all of `` s ``.

Return _an array _`` result ``_ of length 2 where:_

*   `` result[0] ``_ is the total number of lines._
*   `` result[1] ``_ is the width of the last line in pixels._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
<strong>Output:</strong> [3,60]
<strong>Explanation:</strong> You can write s as follows:
abcdefghij  // 100 pixels wide
klmnopqrst  // 100 pixels wide
uvwxyz      // 60 pixels wide
There are a total of 3 lines, and the last line is 60 pixels wide.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
<strong>Output:</strong> [2,4]
<strong>Explanation:</strong> You can write s as follows:
bbbcccdddaa  // 98 pixels wide
a            // 4 pixels wide
There are a total of 2 lines, and the last line is 4 pixels wide.</pre>

&nbsp;

__Constraints:__

*   `` widths.length == 26 ``
*   `` 2 &lt;= widths[i] &lt;= 10 ``
*   `` 1 &lt;= s.length &lt;= 1000 ``
*   `` s `` contains only lowercase English letters.