# RaspberryPiDiscordBot
## A [Discord](https://discord.com/) bot to control your [Raspberry Pi](https://www.raspberrypi.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://wylarel.com/mit/)
[![Discord](https://img.shields.io/badge/Chat-Discord-blue)](https://discord.gg/7qvmeh2)
[![Python](https://img.shields.io/badge/Made%20with-Python-orange)](https://www.python.org/)

## Install
- For this script to work, it will **have** to run on a [Raspbarry Pi](https://www.raspberrypi.org/). That said, the discord bot will still connect if you are running it on another device, but the commands won't work.
- The dependancies are `discord` ([discord.py](https://discordpy.readthedocs.io/en/latest/)) and `RPi`, a library installed as default with the raspberry os.
- You will have to put your [Discord bot token](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) in the `TOKEN` file, or modify the code to hard code it ([bad practice](https://www.infoworld.com/article/3064355/how-you-might-be-leaking-your-secrets-onto-github.html)).
- Then, simply run the code with python 3 and it should work :smiley:

## Usage
The main and only command is `raspberry` alias `rpi`. The syntax of that command is `raspberry [pin] <get/set/toggle> <mode>`.
- `pin` is, the pin number according to the GPIO pins table:
![](https://i.imgur.com/HMzAMQG.png) This can be changed to BCM by changing the line `GPIO.setmode(GPIO.BOARD)` to `GPIO.setmode(GPIO.BCM)`.
[Simple Guide to the Raspberry Pi GPIO Header](https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/)
- `action` is either `get`, `set` or `toggle`.
- `mode` is needed if the action is `get` or `set`. It can be true `(1 / one / true / on)` or false `(0 / zero / false / off)`.

## Notes
*Usually, when I publish an open-source bot, I provide an instance of the bot that you can invite to your server. I do have a bot running this script on my raspberry, but I'm not going to make it public, simply because my raspberry is connected to essential items in my house. And even if you don't have any malicious intent, I don't want my bedroom lamp to be turned on at 3 in the morning just because we're not in the same timezone :wink: That said, you can still [join my server](https://discord.gg/7qvmeh2) to use a limited private demo.*

## [MIT License](https://wylarel.com/mit/)
```
Copyright (c) 2020 Wylarel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
