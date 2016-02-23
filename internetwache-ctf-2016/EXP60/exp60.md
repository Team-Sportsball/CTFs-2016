# EXP60: EquationSolver

## Challenge
**Description:** I created a program for an unsolvable equation system. My friend somehow forced it to solve the equations. Can you tell me how he did it?

**Service:** 188.166.133.53:12049

## Solution

### Testing for Integer Overflow
We connect to the server with netcat and throw a large integer to test for integer overflow:

```
$ nc 188.166.133.53 12049
Solve the following equations:
X > 1337
X * 7 + 4 = 1337
Enter the solution X: 55555555555555555555555555555
You entered: 2147483647
2147483647 is bigger than 1337
2147483645 is not equal to 1337
WRONG!!!
Go to school and learn some math!
```

Looks like we've got a signed int32 and we know:

* Largest negative 32bit integer value: `-2147483648`
* Largest positive 32bit integer value: `2147483647`

We want X such that:

```
(X * 7) mod 4294967295 + 4 = 1337
```

Since our X can range from `-2147483648` to `2147483647` and we can't solve for a negative modulo value, we use the the entire range as a positive number (an unsigned int32): `4294967295`

`4294967295` is actually an estimate since integer overflows are not exact and may occur differently at each overflow. This means we'll probably have to test a couple of values before we find the exact solution.

### Solving for X
Now we need to solve for X.

We know from the Extended Euclidean Algorithm (`ax + by = gcd(a,b)`) that we can solve an inverse modulo such that `(x * e) mod k = 1 (where e and k are known values).`

In Python, we write this as:

```
# iterative Extended Euclidean Algorithm
def iterative_egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q # use x//y for floor "floor division"
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

# modulo inverse
def modinv(a, m):
    g, x, y = iterative_egcd(a, m) 
    if g != 1:
        return None
    else:
        return x % m
```

In our case, we set:

```
>>> e = 7
>>> k = 4294967295
```

and solve for X:

```
>>> X = modinv(e, k)
>>> X
1227133513
```

### Testing values close to X

We test our X value (`1227133513`):

```
$ nc 188.166.133.53 12049
Solve the following equations:
X > 1337
X * 7 + 4 = 1337
Enter the solution X: 1227133513
You entered: 1227133513
1227133513 is bigger than 1337
3 is not equal to 1337
WRONG!!!
Go to school and learn some math!
```

7 divides 1337 evenly, so this modulo didn't work, but we got close to 1 so we know the equation is solving correctly. We increase our modulo `k` by 1 and solve for X again:

```
>>> e = 7
>>> k = 4294967296
>>> X = modinv(e, k)
>>> X
3067833783
```

`3067833783` is larger than an int32, so this won't work. We increase modulo by 1 again:

```
>>> e = 7
>>> k = 4294967297
>>> X = modinv(e, k)
>>> X
2454267027
```

`2454267027` is also larger than an int32, so this won't work. We increase modulo by 1 yet again:

```
>>> e = 7
>>> k = 4294967298
>>> X = modinv(e, k)
>>> X
613566757
```

That value is valid so we test it out:

```
$ nc 188.166.133.53 12049
Solve the following equations:
X > 1337
X * 7 + 4 = 1337
Enter the solution X: 613566757
You entered: 613566757
613566757 is bigger than 1337
7 is not equal to 1337
WRONG!!!
Go to school and learn some math!
```

Awesome! Now we're only off from 1337 by 1330 which is divisible by 7. Since `7 * 190 = 1330`, we increase X by 190:

```
$ nc 188.166.133.53 12049
Solve the following equations:
X > 1337
X * 7 + 4 = 1337
Enter the solution X: 613566947
You entered: 613566947
613566947 is bigger than 1337
1337 is equal to 1337
Well done!
IW{Y4Y_0verfl0w}
```
