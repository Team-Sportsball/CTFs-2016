# HackIM Crypto 1

>You are in this GAME. A critical mission, and you are surrounded by the beauties, ready to shed their slik gowns on your beck. On onside your feelings are pulling you apart and another side you are called by the duty. The biggiest question is seX OR success? The signals of subconcious mind are not clear, cryptic. You also have the message of heart which is clear and cryptic. You just need to use three of them and find whats the clear message of your Mind... What you must do?

## Write-up

This challenge was pretty simple, they gave us 3 files - `Heart_clear.txt`, `Heart_crypt.txt`, and `Mind_crypt.txt`. Since have the hint of "`seX OR success`", I knew it'd be an XOR key, so I took `Heart_clear.txt` and XOR'd the contents with `Heart_crypt.txt` and got a repeating XOR key of `Its right there what you are looking for.\n`. Using that key to decrypt `Mind_crypt.txt` lead to a [google play link](https://play.google.com/store/apps/collection/promotion_3001629_watch_live_games?hl=en). After derping around on the page a bit I tried the words at the top of the page "Never Miss a Game" and voila! 500 Points. The point system seemed to be a bit wonky as this challenge was **super** easy, and I spent a hugely disproportional amount of time on the RE challenges for fewer points.

Flag:
> Never Miss a Game

```python
with open("Heart_clear.txt") as f:
    clear = f.read()

with open("Heart_crypt.txt") as f:
    cipher = f.read()

with open("Mind_crypt.txt") as f:
    mc = f.read()

bytes = []
for plain_byte, cipher_byte in zip(clear, cipher):
    bytes.append(chr(ord(plain_byte) ^ ord(cipher_byte)))

xor_key = "".join(bytes)
# bytes == XOR key
# 'Its right there what you are looking for.\n'

print "XOR key -> %s" % xor_key

bytes = []
for xor_key_byte, cipher_byte in zip(xor_key, mc):
    bytes.append(chr(ord(xor_key_byte) ^ ord(cipher_byte)))

print "".join(bytes)
# https://play.google.com/store/apps/collection/promotion_3001629_watch_live_games?hl=en
# Flag -> "Never Miss a Game"
```
