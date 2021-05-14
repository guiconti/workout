Given a string `` IP ``, return `` "IPv4" `` if IP is a valid IPv4 address, `` "IPv6" `` if IP is a valid IPv6 address or `` "Neither" `` if IP is not a correct IP of any type.

__A valid IPv4__ address is an IP in the form <code>"x<sub>1</sub>.x<sub>2</sub>.x<sub>3</sub>.x<sub>4</sub>"</code> where <code>0 &lt;= x<sub>i</sub> &lt;= 255</code> and <code>x<sub>i</sub></code> __cannot contain__ leading zeros. For example, `` "192.168.1.1" `` and `` "192.168.1.0" `` are valid IPv4 addresses but `` "192.168.01.1" ``, while `` "192.168.1.00" `` and `` "192.168@1.1" `` are invalid IPv4 addresses.

__A valid IPv6__ address is an IP in the form <code>"x<sub>1</sub>:x<sub>2</sub>:x<sub>3</sub>:x<sub>4</sub>:x<sub>5</sub>:x<sub>6</sub>:x<sub>7</sub>:x<sub>8</sub>"</code> where:

*   <code>1 &lt;= x<sub>i</sub>.length &lt;= 4</code>
*   <code>x<sub>i</sub></code> is a __hexadecimal string__ which may contain digits, lower-case English letter (`` 'a' `` to `` 'f' ``) and upper-case English letters (`` 'A' `` to `` 'F' ``).
*   Leading zeros are allowed in <code>x<sub>i</sub></code>.

For example, "`` 2001:0db8:85a3:0000:0000:8a2e:0370:7334" `` and "`` 2001:db8:85a3:0:0:8A2E:0370:7334" `` are valid IPv6 addresses, while "`` 2001:0db8:85a3::8A2E:037j:7334" `` and "`` 02001:0db8:85a3:0000:0000:8a2e:0370:7334" `` are invalid IPv6 addresses.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> IP = "172.16.254.1"
<strong>Output:</strong> "IPv4"
<strong>Explanation:</strong> This is a valid IPv4 address, return "IPv4".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
<strong>Output:</strong> "IPv6"
<strong>Explanation:</strong> This is a valid IPv6 address, return "IPv6".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> IP = "256.256.256.256"
<strong>Output:</strong> "Neither"
<strong>Explanation:</strong> This is neither a IPv4 address nor a IPv6 address.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
<strong>Output:</strong> "Neither"
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> IP = "1e1.4.5.6"
<strong>Output:</strong> "Neither"
</pre>

&nbsp;

__Constraints:__

*   `` IP `` consists only of English letters, digits and the characters `` '.' `` and `` ':' ``.