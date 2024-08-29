import discord
from discord.ext import commands
from sql import Conversation, create_tables, db
from settings import TOKEN
from gemini import generate_response

create_tables()

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.event
async def on_message(message: discord.Message):
    content = message.content.replace(f'<@!{bot.user.id}>', '').replace(f'<@{bot.user.id}>', '').strip()

    if message.author == bot.user:
        Conversation.create(channel_id=message.channel.id, user_id=message.author.id, user_name=message.author.name,
                            message_content=content, message_id=message.id, role='bot')
        return

    Conversation.create(channel_id=message.channel.id, user_id=message.author.id, user_name=message.author.name,
                        message_content=content, message_id = message.id, role='user')

    if message.content:
        history = Conversation.select().where(Conversation.channel_id == message.channel.id)
        try:
            response = generate_response(history)
            text = response.text
            await message.channel.send(text)
        except Exception as e:
            print(str(e))
            await message.channel.send("an error has occured \n" + str(e))
    await bot.process_commands(message)


@bot.command(name='history')
async def fetch_history(ctx, user_id: int):
    history = Conversation.select().where(Conversation.user_id == user_id)

    if history.exists():
        history_message = '\n'.join([f'{conv.user_name}: {conv.message_content}' for conv in history])
        await ctx.send(f'Conversation history for user {user_id}:\n{history_message}')
    else:
        await ctx.send(f'No conversation history found for user {user_id}.')


@bot.event
async def on_disconnect():
    db.close()

# Run the bot
bot.run(TOKEN)



