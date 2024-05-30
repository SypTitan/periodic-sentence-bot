import disnake, dotenv, os
import elementFinder
from disnake.ext import commands

dotenv.load_dotenv()
bot_token = os.environ.get('TOKEN')
run_flask = os.environ.get('RUNFLASK', 'False') == 'True'

if run_flask:
    import keepalive
    keepalive.keep_alive()
    print("Flask server started")
    
intents = disnake.Intents.default()
intents.messages = True
bot = commands.Bot(intents=intents,command_prefix=disnake.ext.commands.when_mentioned)

@bot.event
async def on_ready():
    print(f"Bot started as {bot.user}")
    

    
bot.run(bot_token)