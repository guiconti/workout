Given a list of folders, remove all sub-folders in those folders and return in __any order__ the folders after removing.

If a `` folder[i] `` is located within&nbsp;another `` folder[j] ``, it is called a&nbsp;sub-folder&nbsp;of it.

The format of a path is&nbsp;one or more concatenated strings of the form:&nbsp;`` / ``&nbsp;followed by one or more lowercase English letters. For example,&nbsp;`` /leetcode ``&nbsp;and&nbsp;`` /leetcode/problems ``&nbsp;are valid paths while an empty string and&nbsp;`` / ``&nbsp;are not.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
<strong>Output:</strong> ["/a","/c/d","/c/f"]
<strong>Explanation:</strong> Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> folder = ["/a","/a/b/c","/a/b/d"]
<strong>Output:</strong> ["/a"]
<strong>Explanation:</strong> Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> folder = ["/a/b/c","/a/b/ca","/a/b/d"]
<strong>Output:</strong> ["/a/b/c","/a/b/ca","/a/b/d"]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= folder.length&nbsp;&lt;= 4 * 10^4 ``
*   `` 2 &lt;= folder[i].length &lt;= 100 ``
*   `` folder[i] `` contains only&nbsp;lowercase letters and '/'
*   `` folder[i] `` always starts with character '/'
*   Each folder name is unique.