Write a program that outputs the string representation of numbers from 1 to&nbsp;_n_, however:

*   If the number is divisible by 3, output "fizz".
*   If the number is divisible by 5, output&nbsp;"buzz".
*   If the number is divisible by both 3 and 5, output&nbsp;"fizzbuzz".

For example, for&nbsp;`` n = 15 ``, we output:&nbsp;`` 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz ``.

Suppose you are given the following code:

<pre>
class FizzBuzz {
&nbsp; public FizzBuzz(int n) { ... }&nbsp;              // constructor
  public void fizz(printFizz) { ... }          // only output "fizz"
  public void buzz(printBuzz) { ... }          // only output "buzz"
  public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
  public void number(printNumber) { ... }      // only output the numbers
}</pre>

Implement a multithreaded version of `` FizzBuzz `` with __four__ threads. The same instance of `` FizzBuzz `` will be passed to four different threads:

1.   Thread A will call&nbsp;`` fizz() ``&nbsp;to check for divisibility of 3 and outputs&nbsp;`` fizz ``.
2.   Thread B will call&nbsp;`` buzz() ``&nbsp;to check for divisibility of 5 and outputs&nbsp;`` buzz ``.
3.   Thread C will call `` fizzbuzz() ``&nbsp;to check for divisibility of 3 and 5 and outputs&nbsp;`` fizzbuzz ``.
4.   Thread D will call `` number() `` which should only output the numbers.