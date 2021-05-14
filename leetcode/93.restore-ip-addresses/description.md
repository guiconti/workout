Given a string `` s `` containing only digits, return all possible valid IP addresses that can be obtained from `` s ``. You can return them in __any__ order.

A __valid IP address__ consists of exactly four integers, each integer is between `` 0 `` and `` 255 ``, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are __valid__ IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are __invalid__ IP addresses.&nbsp;

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> s = "25525511135"
<strong>Output:</strong> ["255.255.11.135","255.255.111.35"]
</pre>

__Example 2:__

<pre><strong>Input:</strong> s = "0000"
<strong>Output:</strong> ["0.0.0.0"]
</pre>

__Example 3:__

<pre><strong>Input:</strong> s = "1111"
<strong>Output:</strong> ["1.1.1.1"]
</pre>

__Example 4:__

<pre><strong>Input:</strong> s = "010010"
<strong>Output:</strong> ["0.10.0.10","0.100.1.0"]
</pre>

__Example 5:__

<pre><strong>Input:</strong> s = "101023"
<strong>Output:</strong> ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= s.length &lt;= 3000 ``
*   `` s `` consists of digits only.