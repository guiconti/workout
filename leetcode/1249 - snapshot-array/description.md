Implement a SnapshotArray that supports the following interface:

*   `` SnapshotArray(int length) `` initializes an array-like data structure with the given length.&nbsp; __Initially, each element equals 0__.
*   `` void set(index, val) `` sets the element at the given `` index `` to be equal to `` val ``.
*   `` int snap() ``&nbsp;takes a snapshot of the array and returns the `` snap_id ``: the total number of times we called `` snap() `` minus `` 1 ``.
*   `` int get(index, snap_id) ``&nbsp;returns the value at the given `` index ``, at the time we took the snapshot with the given `` snap_id ``

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
<strong>Output:</strong> [null,null,0,null,5]
<strong>Explanation: </strong>
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= length&nbsp;&lt;= 50000 ``
*   At most `` 50000 ``&nbsp;calls will be made to `` set ``, `` snap ``, and `` get ``.
*   `` 0 &lt;= index&nbsp;&lt;&nbsp;length ``
*   `` 0 &lt;=&nbsp;snap_id &lt;&nbsp; ``(the total number of times we call `` snap() ``)
*   `` 0 &lt;=&nbsp;val &lt;= 10^9 ``