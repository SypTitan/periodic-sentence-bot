import disnake, dotenv, os
from elementFinder import recreate_string
from disnake.ext import commands

try:
    dotenv.load_dotenv()
finally:
    bot_token = os.environ.get('TOKEN')
    run_flask = os.environ.get('RUNFLASK', 'False') == 'True'

if run_flask:
    import keepalive
    port = os.environ.get('PORT', 8000)
    keepalive.keep_alive(port)
    print("Flask server started")
    
intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents,command_prefix=disnake.ext.commands.when_mentioned)

@bot.event
async def on_ready():
    print(f"Bot started as {bot.user}")
    
@bot.event
async def on_message(message: disnake.Message):
    if message.author == bot.user:
        return
    elementedMessage = recreate_string(message.content).strip()
    if (len(elementedMessage.replace(' ','')) < 5 and bot.user not in message.mentions):
        return
    if '?' not in elementedMessage:
        await message.reply("**Congrats! Your message can be spelled using the elements of the periodic table:**\n```" + elementedMessage+"```", mention_author=False)
        
@bot.slash_command(name="spell", description="Spell your message using the elements of the periodic table")
async def spell(inter: disnake.ApplicationCommandInteraction, message: str, hidden: bool = False, enforce_rules: bool = False):
    elementedMessage = recreate_string(message, ignore_repeats=(not enforce_rules)).strip()
    if ('?' not in elementedMessage and ((not enforce_rules) or len(elementedMessage.replace(' ','')) < 5)):
        await inter.response.send_message("**Your message can be spelled using the elements of the periodic table:**\n```" + elementedMessage+"```", ephemeral=hidden)
    else:
        await inter.response.send_message("Your message can't be spelled using the elements of the periodic table.", ephemeral=True)
    
bot.run(bot_token)
