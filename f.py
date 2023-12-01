import asyncio
import random
import discord
from discord.ext import commands
import bloxflip
import tensorflow as tf
from sklearn.model_selection import train_test_split  n
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd  
from time import 
import turtle  UI

bot = commands.Bot(command_prefix='.', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}.")

@bot.command(name='auto_mines', description='auto player mines')
async def auto_mines(ctx, bet_amount: int, mine_amount: int, auth_token: str):
    """
    Automated Mines game command.

    Parameters:
    - bet_amount (int): The amount to bet in the Mines game.
    - mine_amount (int): The number of mines to choose.
    - auth_token (str): The authentication token for the player.
    """
    if bet_amount < 5:
        await ctx.send("Bet amount must be higher than 5!")
        return

    try:
        start_game = bloxflip.Mines.Create(betamount=bet_amount, mines=mine_amount, auth=auth_token)
        if start_game.status_code == 400:
            await ctx.send("Failed to start game | Bet amount probably higher than balance")
            return
        bloxflip.Currency.Balance(auth=auth_token)
    except:
        await ctx.send("Invalid auth token")
        return

    await ctx.send('Attempting to click mines')

    async def click_mines():
        try:
            for _ in range(mine_amount):
                a = random.randint(0, 24)
                bloxflip.Mines.Choose(choice=int(a), auth=auth_token)
                await asyncio.sleep(0.5)  # Optional: Add a delay between each click
        except Exception as e:
            await ctx.send(f"Failed to click mines: {e}")

    await click_mines()

    try:
        bloxflip.Mines.Cashout(auth=auth_token)
        balance = bloxflip.Currency.Balance(auth=auth_token)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name='AUTOMATED MINES', value=f'You Won! | Balance: **{balance}**')
     
        await ctx.send(embed=embed)
    except:
        balance = bloxflip.Currency.Balance(auth=auth_token)
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name='AUTOMATED MINES', value=f'You Lost! | Balance: **{balance}**')
      
        await ctx.send(embed=embed)

@bot.command(name='plot_results', description='Plot results using matplotlib')
async def plot_results(ctx, predicted_data, true_data):
.

@bot.command(name='turtle_graphics', description='Create Turtle graphics')
async def turtle_graphics(ctx):
  
    # Turtle graphics code
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.done()

bot.run('bot token here')
