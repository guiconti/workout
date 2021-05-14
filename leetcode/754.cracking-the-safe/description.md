There is a box protected by a password. The password is a sequence of&nbsp;`` n `` digits&nbsp;where each digit can be one of the first `` k `` digits `` 0, 1, ..., k-1 ``.

While entering a password,&nbsp;the last `` n `` digits entered will automatically be matched against the correct password.

For example, assuming the correct password is `` "345" ``,&nbsp;if you type `` "012345" ``, the box will open because the correct password matches the suffix of the entered password.

Return any password of __minimum length__ that is guaranteed to open the box at some point of entering it.

&nbsp;

__Example 1:__

<pre>
<b>Input:</b> n = 1, k = 2
<b>Output:</b> "01"
<b>Note:</b> "10" will be accepted too.
</pre>

__Example 2:__

<pre>
<b>Input:</b> n = 2, k = 2
<b>Output:</b> "00110"
<b>Note:</b> "01100", "10011", "11001" will be accepted too.
</pre>

&nbsp;

__Note:__

1.   `` n `` will be in the range `` [1, 4] ``.
2.   `` k `` will be in the range `` [1, 10] ``.
3.   `` k^n `` will be at most `` 4096 ``.

&nbsp;