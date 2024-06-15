import discord
import os
import asyncio
import datetime
import random
import sqlite3
import aiohttp
import roblox
import roblox.thumbnails
from discord import ui, ButtonStyle
from discord import client, member
from discord.ext import commands
from roblox import Client, utilities, thumbnails
from roblox import groups, members
from roblox.thumbnails import AvatarThumbanilType
from typing import Optional
from key_generator.key_generator import generate
from wonderwords import RandomSentence


connection = sqlite3.connect("database.sqlite")
cursor = connection.cursor()
client = Client("ROBLOX_ACCOUNT_TOKEN")

class Main(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot



  @commands.command(name="slap")
  async def slap(ctx, member: discord.User):
    await ctx.send(f'{ctx.message.author.mention} slaps {member.mention}!')

  @commands.command(name="echo")
  async def echo(self, ctx, *, args):
    sentence = str(args)
    await ctx.send(args)



  @commands.command(name="getrole")
  async def getrole(self, ctx, *, args)
  bot = self.bot
  role = str(args)
  guild = bot.get_guild(900405874886049863)
  user = ctx.message.author
  choosable_roles = ["event", "minor", "announcement", "partnership", "upload", "chat", "welcome", "giveaway", "gamenight"]
  if role and role in choosable_roles:
    if role == "event":
      role = get(guild.roles, name="════ ⋆★⋆ ════Event════ ⋆★⋆ ════")
      if role in user.roles:
        await user.remove_roles(role)
        await ctx.reply("Removed role: Event Pings")



await def setup(bot: commands.Bot):
  await bot.add_cog(Main(bot))





