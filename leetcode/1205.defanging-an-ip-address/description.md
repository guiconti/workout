Given a valid (IPv4) IP `` address ``, return a defanged version of that IP address.

A _defanged&nbsp;IP address_&nbsp;replaces every period `` "." `` with `` "[.]" ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> address = "1.1.1.1"
<strong>Output:</strong> "1[.]1[.]1[.]1"
</pre>

__Example 2:__

<pre><strong>Input:</strong> address = "255.100.50.0"
<strong>Output:</strong> "255[.]100[.]50[.]0"
</pre>

&nbsp;

__Constraints:__

*   The given `` address `` is a valid IPv4 address.