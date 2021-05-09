Given an array of strings `` names `` of size `` n ``. You will create `` n `` folders in your file system __such that__, at the `` ith `` minute, you will create a folder with the name `` names[i] ``.

Since two files __cannot__ have the same name, if you enter a folder name which is previously used,&nbsp;the system&nbsp;will have a suffix&nbsp;addition to its name in the form of `` (k) ``,&nbsp;where,&nbsp;`` k `` is the __smallest positive integer__ such that the obtained name remains unique.

Return _an array of strings of length `` n ``_ where `` ans[i] `` is the actual name the system will assign to the `` ith `` folder when you create it.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> names = ["pes","fifa","gta","pes(2019)"]
<strong>Output:</strong> ["pes","fifa","gta","pes(2019)"]
<strong>Explanation:</strong> Let's see how the file system creates folder names:
"pes" --&gt; not assigned before, remains "pes"
"fifa" --&gt; not assigned before, remains "fifa"
"gta" --&gt; not assigned before, remains "gta"
"pes(2019)" --&gt; not assigned before, remains "pes(2019)"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> names = ["gta","gta(1)","gta","avalon"]
<strong>Output:</strong> ["gta","gta(1)","gta(2)","avalon"]
<strong>Explanation:</strong> Let's see how the file system creates folder names:
"gta" --&gt; not assigned before, remains "gta"
"gta(1)" --&gt; not assigned before, remains "gta(1)"
"gta" --&gt; the name is reserved, system adds (k), since "gta(1)" is also reserved, systems put k = 2. it becomes "gta(2)"
"avalon" --&gt; not assigned before, remains "avalon"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
<strong>Output:</strong> ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
<strong>Explanation:</strong> When the last folder is created, the smallest positive valid k is 4, and it becomes "onepiece(4)".
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> names = ["wano","wano","wano","wano"]
<strong>Output:</strong> ["wano","wano(1)","wano(2)","wano(3)"]
<strong>Explanation:</strong> Just increase the value of k each time you create folder "wano".
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> names = ["kaido","kaido(1)","kaido","kaido(1)"]
<strong>Output:</strong> ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
<strong>Explanation:</strong> Please note that system adds the suffix (k) to current name even it contained the same suffix before.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= names.length &lt;= 5 * 10^4 ``
*   `` 1 &lt;= names[i].length &lt;= 20 ``
*   `` names[i] `` consists of lower case English letters, digits and/or round brackets.