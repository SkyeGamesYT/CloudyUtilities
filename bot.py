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


connection = sqlite3.commect("databanse.sqlite")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS warningsdb (user_id INTEGER, reason TEXT, moderator TEXT, warn_id TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS accounts (discord_id INTEGER, roblox_username TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS verify (discord_id INTEGER, roblox_username TEXT, sentence TEXT)")

connection.commit()

help_commands = commands.DefaultHelpCommand(
  no_catagory = 'Misc'
)

bot = commands.Bot(
  command_prefix = "c-",
  intents = discord.Intents.all(),
  help_command = help_commands,
  activity = discord.Activity(type=discord.activity.ActivityType.watching, name="Cloudy Lounge", status = discord.Status.idle)
)


@bot.event
async def setup_hook():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      await bot.load_extension(f'cogs.{filename[:-3]}')
      print(f"Loaded cog: {filename[:-3]}")
    else
      print("Unable to load pycache folder")

@bot.event
async def on_ready():
  print(f'logged in as {bot.user}')
