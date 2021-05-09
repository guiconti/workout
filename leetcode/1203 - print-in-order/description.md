Suppose we have a class:

<pre>
public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
</pre>

The same instance of `` Foo `` will be passed to three different threads. Thread A will call `` first() ``, thread B will call `` second() ``, and thread C will call `` third() ``. Design a mechanism and modify the program to ensure that `` second() `` is executed after `` first() ``, and `` third() `` is executed after `` second() ``.

__Note:__

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> "firstsecondthird"
<strong>Explanation:</strong> There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,3,2]
<strong>Output:</strong> "firstsecondthird"
<strong>Explanation:</strong> The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
</pre>