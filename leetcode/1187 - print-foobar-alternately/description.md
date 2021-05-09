Suppose you are given the following code:

<pre>
class FooBar {
  public void foo() {
&nbsp; &nbsp; for (int i = 0; i &lt; n; i++) {
&nbsp; &nbsp; &nbsp; print("foo");
&nbsp;   }
  }

  public void bar() {
&nbsp; &nbsp; for (int i = 0; i &lt; n; i++) {
&nbsp; &nbsp; &nbsp; print("bar");
&nbsp; &nbsp; }
  }
}
</pre>

The same instance of `` FooBar `` will be passed to two different threads. Thread A will call&nbsp;`` foo() `` while thread B will call&nbsp;`` bar() ``.&nbsp;Modify the given program to output "foobar" _n_ times.

&nbsp;

__Example 1:__

<pre>
<b>Input:</b> n = 1
<b>Output:</b> "foobar"
<strong>Explanation:</strong> There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar(). "foobar" is being output 1 time.
</pre>

__Example 2:__

<pre>
<b>Input:</b> n = 2
<b>Output:</b> "foobarfoobar"
<strong>Explanation:</strong> "foobar" is being output 2 times.
</pre>