# CRYPTO80: Procrastination

## Challenge
**Description:** Watching videos is fun! Hint: Stegano skills required.

**Attachment:** [crypto80.zip](https://ctf.internetwache.org/files/crypto80.zip)

The content of ``crypto80.zip`` is the file ``song.webm``.

**Service:** [https://procrastination.ctf.internetwache.org](https://procrastination.ctf.internetwache.org/)
https://www.youtube.com/watch?v=oHg5SJYRHA0

## Solution

### Investigate WebM File
We take a look at ``song.webm`` with ``ffmpeg``:

```
$ ffmpeg -i song.webm 
ffmpeg version 2.8.6 Copyright (c) 2000-2016 the FFmpeg developers
  built with Apple LLVM version 7.0.2 (clang-700.1.81)
<snip>
Input #0, matroska,webm, from 'song.webm':
  Metadata:
    encoder         : Lavf56.40.101
  Duration: 00:00:36.04, start: 0.000000, bitrate: 520 kb/s
    Stream #0:0: Video: vp8, yuv420p, 320x240, SAR 1:1 DAR 4:3, 1k fps, 30 tbr, 1k tbn, 1k tbc (default)
    Stream #0:1: Audio: vorbis, 44100 Hz, stereo, fltp (default)
    Stream #0:2: Audio: vorbis, 8000 Hz, mono, fltp
```

We can see that there are three streams stored in the WebM container, two of which are audio. We grab the non-default audio steam (Stream #0:2) and output as a WAV file:

```
$ ffmpeg -i song.webm -map 0:2 audio2.wav
```

### Analyze DTMF Tones
We open the file with VLC and we hear what sounds like DTMF tones.

The website [DialABC](http://dialabc.com/sound/detect/index.html) has a free online converter that takes a WAV file and outputs the resulting tone-to-digit mapping. We upload ``audio2.wav`` to DialABC and get the convertion. The result we get is:

```
011101270173010401220600116063012301370127061012401100137012001100
```

If we treat the values separated by 0's as octal, we divide the series so that we have the following array:

```
>>> array = [0o111, 0o127, 0o173, 0o104, 0o122, 0o60, 0o116, 0o63, 0o123, 0o137, 0o127, 0o61, 0o124, 0o110, 0o137, 0o120, 0o110]
```

We convert the octal values to ASCII:

```
>>> "".join([chr(x) for x in array])
'IW{DR0N3S_W1TH_PH'
```

It looks the online converter cut off some of the values, but someone on our team made a guess to find the key:

```
IW{DR0N3S_W1TH_PH0N3S}
```
