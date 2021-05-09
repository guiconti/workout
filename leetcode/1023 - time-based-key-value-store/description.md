Create a timebased key-value store class&nbsp;`` TimeMap ``, that supports two operations.

1. `` set(string key, string value, int timestamp) ``

*   Stores the `` key `` and `` value ``, along with the given `` timestamp ``.

2. `` get(string key, int timestamp) ``

*   Returns a value such that `` set(key, value, timestamp_prev) `` was called previously, with `` timestamp_prev &lt;= timestamp ``.
*   If there are multiple such values, it returns the one with the largest `` timestamp_prev ``.
*   If there are no values, it returns the empty string (`` "" ``).

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong>inputs = <span id="example-input-1-1">["TimeMap","set","get","get","set","get","get"]</span>, inputs = <span id="example-input-1-2">[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]</span>
<strong>Output: </strong><span id="example-output-1">[null,null,"bar","bar",null,"bar2","bar2"]</span>
<strong>Explanation: </strong><span id="example-output-1">&nbsp; 
TimeMap kv; &nbsp; 
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1 &nbsp; 
kv.get("foo", 1);  // output "bar" &nbsp; 
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar" &nbsp; 
kv.set("foo", "bar2", 4); &nbsp; 
kv.get("foo", 4); // output "bar2" &nbsp; 
kv.get("foo", 5); //output "bar2" &nbsp; 
</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>inputs = <span id="example-input-2-1">["TimeMap","set","set","get","get","get","get","get"]</span>, inputs = <span id="example-input-2-2">[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]</span>
<strong>Output: </strong><span id="example-output-2">[null,null,null,"","high","high","low","low"]</span>
</pre>
</div>
</div>

&nbsp;

__Note:__

1.   All key/value strings are lowercase.
2.   All key/value strings have&nbsp;length in the range&nbsp;`` [1, 100] ``
3.   The `` timestamps `` for all `` TimeMap.set `` operations are strictly increasing.
4.   `` 1 &lt;= timestamp &lt;= 10^7 ``
5.   `` TimeMap.set `` and `` TimeMap.get ``&nbsp;functions will be called a total of `` 120000 `` times (combined) per test case.