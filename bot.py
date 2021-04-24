import discord
from discord.abc import Messageable
from discord.ext import commands, tasks
import random
import alien as a
from tinydb import TinyDB, Query
import asyncio

client = commands.Bot(command_prefix='~b ')

aliens = a.aliens

# ID of the channel you want the bot to be active in
# Right click on the channel and click Copy ID
channel_id = 0

is_guessing = False

current_alien_guessing = None

guessed_aliens = []

db = TinyDB('points.json')
users = Query()


# gets called when the bot is activated
@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game('Ben10'))
    create_guess.start()
    print('ready')


# sends an embed of the alien passed as an argument
# if no alien is passed, it sends an embed of a random alien
@client.command()
async def alien(ctx, *, alien=None):
    if alien is not None:
        alien = normalize_text(alien)

    elif alien is None:
        selected_alien = random.choice(list(aliens.values()))

    elif alien not in aliens:
        await ctx.send(f'{alien} is not a valid alien')
        return

    else:
        selected_alien = aliens[alien]

    if selected_alien.image is None:
        selected_alien.image = 'https://i.pinimg.com/originals/59/41/73/594173036931a34e7952732d76b000c3.png'

    embedVar = discord.Embed(title=selected_alien.name, description="", color=0x00ff00)
    embedVar.add_field(name="Species", value=selected_alien.species, inline=True)
    embedVar.add_field(name="Home Planet", value=selected_alien.homeworld, inline=False)
    embedVar.set_image(url=selected_alien.image)
    embedVar.add_field(name="Abilities", value=selected_alien.description, inline=True)
    await ctx.channel.send(embed=embedVar)


# Every few minutes the bot will send an embed with a picture of a random alien
# Use this command to guess which alien it is
@client.command()
async def guess(ctx, *, alien=None):
    global current_alien_guessing
    if alien is None:
        return
    alien = normalize_text(alien)
    if alien == current_alien_guessing:
        await ctx.channel.send(f'The alien is {aliens[current_alien_guessing].name}. '
                               f'You got it right {ctx.message.author.mention}!')
        current_alien_guessing = None
        update_database(str(ctx.message.author))


# Sends an embed of the leaderboard
@client.command()
async def leaderboard(ctx):
    stats = sorted(db.all(), key=lambda i: i['points'], reverse=True)
    embed = discord.Embed(title='Leaderboard', color=0x00ff00)
    for stat, i in zip(stats, range(1, len(stats) + 1)):
        embed.add_field(name=str(str(i) + '. ' + stat['name'] + str(stat['points']).rjust(25 - len(stat['name']))),
                        value='\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014', inline=False)

    await ctx.channel.send(embed=embed)


# Changes the channel where the bot is active
@client.command()
async def setmainchannel(ctx):
    global channel_id
    channel_id = ctx.message.channel.id
    await client.get_channel(channel_id).send('Set to new main channel')


# Removes a number of messages sent by the bot
@client.command()
async def purge(ctx, number):
    number = int(number)
    async for x in Messageable.history(ctx.message.channel, limit=number):
        if x.author == client.user:
            await x.delete()
            print(f'deleted {x.content}')
    print('done purging')


# Creates a guess every 15 minutes
# Can be adjusted by using seconds=, minutes= or hours=
@tasks.loop(minutes=15)
async def create_guess():
    global channel_id
    global current_alien_guessing
    guessed_aliens.clear()
    random_alien = random.choice(list(aliens.keys()))
    current_alien_guessing = random_alien
    embed = discord.Embed(title='Type ~ben guess [alien] to guess the alien', color=0x00ff00)
    embed.set_image(url=aliens[random_alien].image)
    await client.get_channel(channel_id).send(embed=embed)
    await asyncio.sleep(35)
    if current_alien_guessing is not None:
        await client.get_channel(channel_id).send(f'The alien is {aliens[current_alien_guessing].name}')
    current_alien_guessing = None


def normalize_text(text):
    text = text.strip()
    text = text.lower()
    text = text.replace(' ', '')
    text = text.replace('-', '')
    return text


def update_database(user):
    id = user[-4:]
    name = user[:-5]

    if len(db.search(users.id == id)) == 0:
        db.insert({'id': id, 'name': name, 'points': 5})
    else:
        new_num = db.search(users.id == id)[0]['points']
        new_num += 5
        db.update({'points': new_num}, users.id == id)


# The bot ID
# Gotten from the discord developer website
client.run('')
