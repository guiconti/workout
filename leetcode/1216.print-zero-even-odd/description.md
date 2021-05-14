Suppose you are given the following code:

<pre>
class ZeroEvenOdd {
&nbsp; public ZeroEvenOdd(int n) { ... }&nbsp;     // constructor
  public void zero(printNumber) { ... }  // only output 0's
  public void even(printNumber) { ... }  // only output even numbers
  public void odd(printNumber) { ... }   // only output odd numbers
}
</pre>

The same instance of `` ZeroEvenOdd `` will be passed to three different threads:

1.   Thread A will call&nbsp;`` zero() ``&nbsp;which should only output 0's.
2.   Thread B will call&nbsp;`` even() ``&nbsp;which should only ouput even numbers.
3.   Thread C will call `` odd() ``&nbsp;which should only output odd numbers.

Each of the threads is given a&nbsp;`` printNumber `` method to output&nbsp;an integer. Modify the given program to output the series&nbsp;`` 010203040506 ``... where the length of the series must be 2_n_.

&nbsp;

__Example 1:__

<pre>
<b>Input:</b> n = 2
<b>Output:</b> "0102"
<strong>Explanation:</strong> There are three threads being fired asynchronously. One of them calls zero(), the other calls even(), and the last one calls odd(). "0102" is the correct output.
</pre>

__Example 2:__

<pre>
<b>Input:</b> n = 5
<b>Output:</b> "0102030405"
</pre>