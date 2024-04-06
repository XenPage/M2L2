import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


organic = ["kayu", "bahan kimia", "sisa makanan", "daun kering", "kotoran hewan", "bambu", "rotan"]
anorganic = ["plastik", "styrofoam", "kaca", "Ban bekas", "Aneka elektronik", "Kaleng aluminium", "Botol-botol plastik", "Sendok"]

@bot.command()
async def pilih_sampah(ctx):
    await ctx.send("Apakah jenis sampah yang mau diketahui?")
    msg = await bot.wait_for("message")

    if msg.content in organic:
          await ctx.send("ini adalah sampah organik")
    
    if msg.content in anorganic:
          await ctx.send("ini adalah sampah anorganik")
    
    if msg.content not in organic or anorganic:
          await ctx.send("Sampah tidak terdaftar")

bot.run("NzU1MzUwMDkxMjY2NTIzMTQ2.GlQSaj.QJkAqwAnP9Hrtx896F6qhRKcH3K4ajJmZ2ZN5Q")