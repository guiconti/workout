Implementing the class `` MajorityChecker ``, which has the following API:

*   `` MajorityChecker(int[] arr) `` constructs an instance of MajorityChecker with the given array `` arr ``;
*   `` int query(int left, int right, int threshold) ``&nbsp;has arguments&nbsp;such that:	
    
    *   `` 0 &lt;= left&nbsp;&lt;= right&nbsp;&lt; arr.length `` representing a subarray of `` arr ``;
    *   `` 2 * threshold &gt; right - left + 1 ``, ie. the threshold is always a strict majority of the length of&nbsp;the subarray
    
    
    

Each&nbsp;`` query(...) `` returns the element in `` arr[left], arr[left+1], ..., arr[right] `` that occurs at least `` threshold `` times, or `` -1 `` if no such element exists.

&nbsp;

__Example:__

<pre>
MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // returns 1
majorityChecker.query(0,3,3); // returns -1
majorityChecker.query(2,3,2); // returns 2
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;=&nbsp;20000 ``
*   `` 1 &lt;= arr[i]&nbsp;&lt;=&nbsp;20000 ``
*   For each query, `` 0 &lt;= left &lt;= right &lt; len(arr) ``
*   For each query, `` 2 * threshold &gt; right - left + 1 ``
*   The number of queries is at most `` 10000 ``