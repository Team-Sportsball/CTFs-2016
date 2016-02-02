# HackIM RE 1 ZorroPub - 100pts

>ZorroPub

## Write-up

This was an interesting challenge and took a bit longer than I expected, mostly because I couldn't find a decent implementation of the glibc `rand()/srand()` functions anywhere, so I ended up just firing up a Linux VM (the lazy is strong with me). Firing up the program we are asked to get a number of drinks, and a drinkID for each drink specified. After decompiling the binary with IDA I checked out one run of the codepath, noting that my input for drink IDs had to be between `0x10` `0xFFFF`, the weird encryption key that was being read (`encryption_key` down below), as well as the final MD5 check that happened before the answer was "accepted".

After extracting all this information (and using ctypes to interact with the glibc random number generator) I put together a brute force harness that essentially did all the stuff that mattered in our program without any of the stuff that didn't. After a while it found that `1` drink with the ID `59306` had the right md5. Piping that back into our program spits out the flag `nullcon{nu11c0n_s4yz_x0r1n6_1s_4m4z1ng}`

Flag:
> nullcon{nu11c0n_s4yz_x0r1n6_1s_4m4z1ng}

```python
# mmmm ctypes
libsystem = ctypes.CDLL('libc.so.6')

# Extracted by hand
encryption_key = [
    0x03C8, 0x0032, 0x02CE, 0x0302, 0x007F,
    0x01B8, 0x037E, 0x0188, 0x0349, 0x027F,
    0x005E, 0x0234, 0x0354, 0x01A3, 0x0096,
    0x0340, 0x0128, 0x02FC, 0x0300, 0x028E,
    0x0126, 0x001B, 0x032A, 0x02F5, 0x015F,
    0x0368, 0x01EB, 0x0079, 0x011D, 0x024E
]

need_md5 = '5eba99aff105c9ff6a1a913e343fec67'
mc = 0
while True:
    for drink_id_count in range(17, 0xFFFE):
        mc += 1
        if mc % 1000 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()
        for counter in range(5):
            input_1 = counter
            seed = 0
            drink_ids = []

            for x in range(input_1):
                drink_id = drink_id_count
                drink_ids.append(drink_id)
                if drink_id <= 16 or drink_id > 0xFFFF:
                    continue
                else:
                    seed ^= drink_id

            count = seed
            some_num = 0
            while count > 1:
                some_num += 1
                count &= (count - 1)

            if some_num != 10:
                continue
            else:
                pass

            libsystem.srand(seed)

            flag = ""
            h = hashlib.md5()

            for x in range(30):
                ran = libsystem.rand()
                rand_number = ran % 1000

                h.update("%d" % rand_number)
                flag += chr((rand_number ^ encryption_key[x])&0xFF)

            if h.hexdigest() == need_md5:
                print "\nHash -> %s" % h.hexdigest()
                print "Found it! Drinks:%d, Drink IDs:%s" % (counter, drink_ids)
                raw_input()
```
