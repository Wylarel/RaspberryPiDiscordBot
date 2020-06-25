try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
except ImportError:
    print("You must run this code on a raspberry pi")
print("Connecting to discord [0%]")
from discord.ext import commands

TOKEN = open("TOKEN", "r").read()
client = commands.Bot(command_prefix='!', case_insensitive=True)
print("Connecting to discord [50%]")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord! [100%]')


@client.command(name='raspberry', aliases=['rpi'], help='!raspberry [pin] <action>')
async def raspberry(ctx, pin=-1, action="get", mode=None):
    if type(pin) != int or pin <= 0:
        await ctx.send(":x: **Syntax:** `!raspberry [pin] <action>`")
        return
    try:
        GPIO.setup(pin, GPIO.OUT)
    except ValueError:
        await ctx.send(":x: **Invalid pin**")
        return
    if action == "get":
        if GPIO.input(pin):
            await ctx.send("**Pin " + str(pin) + " is set to :one:**")
        else:
            await ctx.send("**Pin " + str(pin) + " is set to :zero:**")
    elif action == "toggle":
        if GPIO.input(pin):
            GPIO.output(pin, False)
            await ctx.send(":white_check_mark: **Pin " + str(pin) + "** was **toggled** from :one: to :zero:")
        else:
            GPIO.output(pin, True)
            await ctx.send(":white_check_mark: **Pin " + str(pin) + "** was **toggled** from :zero: to :one:")
    elif action == "set":
        if mode:
            mode = mode.lower()
            if mode == "0" or mode == "zero" or mode == "false" or mode == "off" or mode == ":zero:":
                GPIO.output(pin, False)
                await ctx.send(":white_check_mark: **Pin " + str(pin) + "** was **set** to :zero:")
            elif mode == "1" or mode == "one" or mode == "true" or mode == "on" or mode == ":one:":
                GPIO.output(pin, True)
                await ctx.send(":white_check_mark: **Pin " + str(pin) + "** was **set** to :one:")
            else:
                await ctx.send(":x: **Unknown mode:** *" + mode + "*\nAvailable modes: `0 / zero / false / off | 1 / one / true / on`")
        else:
            await ctx.send(":x: **Syntax:** `!raspberry [pin] set [mode]`")
    else:
        await ctx.send(":x: **Unknown action:** *" + action + "*\nAvailable actions: `get | set | toggle`")

client.run(TOKEN)
