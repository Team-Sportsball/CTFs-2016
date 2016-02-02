# HackIM RE 2 Pseudorandom - 300pts

>Random as F*!@

## Write-up

This challenge sucked, mostly because I'm rusty at reverse-engineering (not too much of it at $DAYJOB), and I ended up doing a lot of this manually, which I'm sure was way harder than it needed to be.

The first thing I noticed was that it lived up to the challenge name `psudorandom`. They actually mean it, as their RNG is actually never seeded, so it produces the same output over and over. That definitely helps! The only real hurdle was the fact that there was a `sleep(random())` at start-up. Easily fixed with an `LD_PRELOAD` hack (see `sleepy.c` below).

The only real challenge was figuring out which function was doing the deciding work, but thankfully the program would return immediately when it hit a bad number in the sequence, so backtracking it and looking at the comparison leading down the failure state let me fiddle around with the numbers until I figured out a pattern. Essentially the inputs are powers of 2, starting at `2^15`. Eventually it would cycle, shift, and repeat. Half-way through it started to half. Through guessing + checking I was able to figure out the correct sequence, and it eventually crapped out the flag `nullcon{50_5tup1d_ch4113ng3_f0r_e1i73er_71k3-y0u}`. Good times at 6AM :).

Flag:
> nullcon{50_5tup1d_ch4113ng3_f0r_e1i73er_71k3-y0u}

```c
// sleepy.c
// compile with `gcc -fPIC -shared sleepy.c -o sleepy.so`
int sleep(int seconds){
    return 0; // So sleepy
}
```

```bash
# What that glorious moment looked like
hacker@lubuntu-64:~/Downloads$ LD_PRELOAD=/home/hacker/Downloads/sleepy.so ./pseudorandom_bin
I will generate some random numbers.
If you can give me those numbers, you will be $rewarded$
hmm..thinking...OK. I am Ready. Enter Numbers.
32768
65536
131072
262144
524288
1048576
2097152
4194304
8388608
---SNIP---
64
128
8
16
32
64
4
8
16
32
2
1
Good Job!!
Wait till I fetch your reward...OK. Here it is
The flag is:nullcon{50_5tup1d_ch4113ng3_f0r_e1i73er_71k3-y0u}
```
```python
# The solution in base64 as there are a lot of newlines in the answer
import base64
solution = """
MzI3NjgKNjU1MzYKMTMxMDcyCjI2MjE0NAo1MjQyODgKMTA0ODU3NgoyMDk3MTUyCjQxOTQzMDQK
ODM4ODYwOAoxNjc3NzIxNgozMzU1NDQzMgo2NzEwODg2NAoxMzQyMTc3MjgKMjY4NDM1NDU2CjE2
Mzg0CjMyNzY4CjY1NTM2CjEzMTA3MgoyNjIxNDQKNTI0Mjg4CjEwNDg1NzYKMjA5NzE1Mgo0MTk0
MzA0CjgzODg2MDgKMTY3NzcyMTYKMzM1NTQ0MzIKNjcxMDg4NjQKMTM0MjE3NzI4CjgxOTIKMTYz
ODQKMzI3NjgKNjU1MzYKMTMxMDcyCjI2MjE0NAo1MjQyODgKMTA0ODU3NgoyMDk3MTUyCjQxOTQz
MDQKODM4ODYwOAoxNjc3NzIxNgo0MDk2CjgxOTIKMTYzODQKMzI3NjgKNjU1MzYKMTMxMDcyCjI2
MjE0NAo1MjQyODgKMTA0ODU3NgoyMDk3MTUyCjIwNDgKNDA5Ngo4MTkyCjE2Mzg0CjMyNzY4CjY1
NTM2CjEzMTA3MgoyNjIxNDQKNTI0Mjg4CjEwNDg1NzYKMTAyNAoyMDQ4CjQwOTYKODE5MgoxNjM4
NAozMjc2OAo2NTUzNgoxMzEwNzIKMjYyMTQ0CjUyNDI4OAo1MTIKMTAyNAoyMDQ4CjQwOTYKODE5
MgoxNjM4NAozMjc2OAo2NTUzNgoxMzEwNzIKMjYyMTQ0CjI1Ngo1MTIKMTAyNAoyMDQ4CjQwOTYK
ODE5MgoxNjM4NAozMjc2OAo2NTUzNgoxMjgKMjU2CjUxMgoxMDI0CjIwNDgKNDA5Ngo4MTkyCjE2
Mzg0CjMyNzY4CjY0CjEyOAoyNTYKNTEyCjEwMjQKMjA0OAo0MDk2CjMyCjY0CjEyOAoyNTYKMTYK
MzIKNjQKMTI4CjgKMTYKMzIKNjQKNAo4CjE2CjMyCjIK"""
print base64.b64decode(solution)
```
