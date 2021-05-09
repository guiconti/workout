There is an authentication system that works with authentication tokens. For each session, the user will receive a new authentication token that will expire `` timeToLive `` seconds after the `` currentTime ``. If the token is renewed, the expiry time will be __extended__ to expire `` timeToLive `` seconds after the (potentially different) `` currentTime ``.

Implement the `` AuthenticationManager `` class:

*   `` AuthenticationManager(int timeToLive) `` constructs the `` AuthenticationManager `` and sets the `` timeToLive ``.
*   `` generate(string tokenId, int currentTime) `` generates a new token with the given `` tokenId `` at the given `` currentTime `` in seconds.
*   `` renew(string tokenId, int currentTime) `` renews the __unexpired__ token with the given `` tokenId `` at the given `` currentTime `` in seconds. If there are no unexpired tokens with the given `` tokenId ``, the request is ignored, and nothing happens.
*   `` countUnexpiredTokens(int currentTime) `` returns the number of __unexpired__ tokens at the given currentTime.

Note that if a token expires at time `` t ``, and another action happens on time `` t `` (`` renew `` or `` countUnexpiredTokens ``), the expiration takes place __before__ the other actions.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/copy-of-pc68_q2.png" style="width: 500px; height: 287px;"/>

<strong>Input</strong>
    ["AuthenticationManager", "renew", "generate", "<code>countUnexpiredTokens</code>", "generate", "<code>renew</code>", "<code>renew</code>", "<code>countUnexpiredTokens</code>"]
    [[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
    <strong>Output</strong>
    [null, null, null, 1, null, null, null, 0]
    
    <strong>Explanation</strong>
    AuthenticationManager authenticationManager = new AuthenticationManager(5); // Constructs the AuthenticationManager with <code>timeToLive</code> = 5 seconds.
    authenticationManager.<code>renew</code>("aaa", 1); // No token exists with tokenId "aaa" at time 1, so nothing happens.
    authenticationManager.generate("aaa", 2); // Generates a new token with tokenId "aaa" at time 2.
    authenticationManager.<code>countUnexpiredTokens</code>(6); // The token with tokenId "aaa" is the only unexpired one at time 6, so return 1.
    authenticationManager.generate("bbb", 7); // Generates a new token with tokenId "bbb" at time 7.
    authenticationManager.<code>renew</code>("aaa", 8); // The token with tokenId "aaa" expired at time 7, and 8 &gt;= 7, so at time 8 the <code>renew</code> request is ignored, and nothing happens.
    authenticationManager.<code>renew</code>("bbb", 10); // The token with tokenId "bbb" is unexpired at time 10, so the <code>renew</code> request is fulfilled and now the token will expire at time 15.
    authenticationManager.<code>countUnexpiredTokens</code>(15); // The token with tokenId "bbb" expires at time 15, and the token with tokenId "aaa" expired at time 7, so currently no token is unexpired, so return 0.

&nbsp;

__Constraints:__

*   <code>1 &lt;= timeToLive &lt;= 10<sup>8</sup></code>
*   <code>1 &lt;= currentTime &lt;= 10<sup>8</sup></code>
*   `` 1 &lt;= tokenId.length &lt;= 5 ``
*   `` tokenId `` consists only of lowercase letters.
*   All calls to `` generate `` will contain unique values of `` tokenId ``.
*   The values of `` currentTime `` across all the function calls will be __strictly increasing__.
*   At most `` 2000 `` calls will be made to all functions combined.