In the video game Fallout 4, the quest __"Road to Freedom"__ requires players to reach a metal dial called the __"Freedom Trail Ring"__ and use the dial to spell a specific keyword to open the door.

Given a string `` ring `` that represents the code engraved on the outer ring and another string `` key `` that represents the keyword that needs to be spelled, return _the minimum number of steps to spell all the characters in the keyword_.

Initially, the first character of the ring is aligned at the `` "12:00" `` direction. You should spell all the characters in `` key `` one by one by rotating `` ring `` clockwise or anticlockwise to make each character of the string key aligned at the `` "12:00" `` direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character `` key[i] ``:

1.   You can rotate the ring clockwise or anticlockwise by one place, which counts as __one step__. The final purpose of the rotation is to align one of `` ring ``'s characters at the `` "12:00" `` direction, where this character must equal `` key[i] ``.
2.   If the character `` key[i] `` has been aligned at the `` "12:00" `` direction, press the center button to spell, which also counts as __one step__. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.

&nbsp;

__Example 1:__

<img src="https://assets.leetcode.com/uploads/2018/10/22/ring.jpg" style="width: 450px; height: 450px;"/>

<pre>
<strong>Input:</strong> ring = "godding", key = "gd"
<strong>Output:</strong> 4
<strong>Explanation:</strong>
For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> ring = "godding", key = "godding"
<strong>Output:</strong> 13
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= ring.length, key.length &lt;= 100 ``
*   `` ring `` and `` key `` consist of only lower case English letters.
*   It is guaranteed that `` key `` could always be spelled by rotating `` ring ``.