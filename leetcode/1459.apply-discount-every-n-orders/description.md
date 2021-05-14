There is&nbsp;a sale in a supermarket, there will be a `` discount `` every `` n `` customer.  




Implement the `` Cashier `` class:

*   `` Cashier(int n, int discount, int[] products, int[] prices) `` Initializes the object with `` n ``, the `` discount ``, the `` products ``&nbsp;and their `` prices ``.
*   `` double&nbsp;getBill(int[] product, int[] amount) ``&nbsp;returns the value of the bill and apply the discount if needed. Answers within `` 10^-5 `` of the actual value will be accepted as correct.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]
[[3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]
<strong>Output</strong>
[null,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]
<strong>Explanation</strong>
Cashier cashier = new Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
cashier.getBill([1,2],[1,2]);                        // return 500.0, bill = 1 * 100 + 2 * 200 = 500.
cashier.getBill([3,7],[10,10]);                      // return 4000.0
cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]);    // return 800.0, The bill was 1600.0 but as this is the third customer, he has a discount of 50% which means his bill is only 1600 - 1600 * (50 / 100) = 800.
cashier.getBill([4],[10]);                           // return 4000.0
cashier.getBill([7,3],[10,10]);                      // return 4000.0
cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]); // return 7350.0, Bill was 14700.0 but as the system counted three more customers, he will have a 50% discount and the bill becomes 7350.0
cashier.getBill([2,3,5],[5,3,2]);                    // return 2500.0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 10^4 ``
*   `` 0 &lt;= discount &lt;= 100 ``
*   `` 1 &lt;= products.length &lt;= 200 ``
*   `` 1 &lt;= products[i] &lt;= 200 ``
*   There are __not__ repeated elements in the array `` products ``.
*   `` prices.length == products.length ``
*   `` 1 &lt;= prices[i] &lt;= 1000 ``
*   `` 1 &lt;= product.length &lt;= products.length ``
*   `` product[i] `` exists in `` products ``.
*   `` amount.length == product.length ``
*   `` 1 &lt;= amount[i] &lt;= 1000 ``
*   At most `` 1000 `` calls will be made to `` getBill ``.
*   Answers within&nbsp;`` 10^-5 ``&nbsp;of the actual value will be accepted as correct.