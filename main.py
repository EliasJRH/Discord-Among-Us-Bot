import discord,os,sys

BOT_TOKEN = ""
BOT_CHANNEL = ""
COMMAND_PREFIX = "$"
#finds the length of the command prefix to allow for prefixes longer than 1 character
prefix_length = len(COMMAND_PREFIX)

# commands.Bot is an sub class of discord.client that allows commands to be used
bot = discord.Client()

try:
	BOT_TOKEN = os.environ["BOT_TOKEN"]
	BOT_CHANNEL = os.environ["BOT_CHAN"]
except KeyError:
	try:
		import auth
		BOT_TOKEN = auth.BOT_TOKEN
		BOT_CHANNEL = auth.BOT_CHAN
	except Exception as e:
		print("Ensure you have set your variables. Ie, run as BOT_TOKEN=foo BOT_CHAN=bar python3 main.py",e)
		sys.exit(1)

@bot.event
async def on_message(message):
	# Allow responses only to a certain channel
	if str(message.channel.id) != BOT_CHANNEL and BOT_CHANNEL != "all":
		return
	# Checks the beginning characters (depending on length of profix) of the message content and checks if it is the same as the prefix, then resends everything after the prefix
	if message.content[:prefix_length] == COMMAND_PREFIX:
		await message.channel.send(message.content[prefix_length:])


@bot.event
async def on_reaction_add(reaction, user):
	# Ignore reactions on messages outside of the bot set channel
	if str(reaction.message.channel.id) != BOT_CHANNEL and BOT_CHANNEL != "all":
		return

	# Ensure the message being reacted to is a bot message and the reaction was not added by the bot itself
	if reaction.message.author.id == bot.user.id and user.id != bot.user.id:
		# Print the Message ID and Emoji
		print(f"Reaction Added\nMessage ID: {reaction.message.id}\nEmoji: {reaction.emoji}")

print("**BOT_TOKEN is ", BOT_TOKEN)
print("CHANNEL bound to is ", BOT_CHANNEL)
bot.run(BOT_TOKEN)
