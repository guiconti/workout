An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

*   `` 'A' ``: Absent.
*   `` 'L' ``: Late.
*   `` 'P' ``: Present.

Any student is eligible for an attendance award if they meet __both__ of the following criteria:

*   The student was absent (`` 'A' ``) for __strictly__ fewer than 2 days __total__.
*   The student was __never__ late (`` 'L' ``) for 3 or more __consecutive__ days.

Given an integer `` n ``, return _the __number__ of possible attendance records of length_ `` n ``_ that make a student eligible for an attendance award. The answer may be very large, so return it __modulo__ _<code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 8
<strong>Explanation:</strong> There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 3
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 10101
<strong>Output:</strong> 183236316
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>