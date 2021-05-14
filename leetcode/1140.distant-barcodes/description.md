In a warehouse, there is a row of barcodes, where the <code>i<sup>th</sup></code> barcode is `` barcodes[i] ``.

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> barcodes = [1,1,1,2,2,2]
<strong>Output:</strong> [2,1,2,1,2,1]
</pre>

__Example 2:__

<pre><strong>Input:</strong> barcodes = [1,1,1,1,2,2,3,3]
<strong>Output:</strong> [1,3,1,3,1,2,1,2]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= barcodes.length &lt;= 10000 ``
*   `` 1 &lt;= barcodes[i] &lt;= 10000 ``