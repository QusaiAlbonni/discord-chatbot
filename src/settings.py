from environs import Env

env = Env()
env.read_env()

TOKEN = env('BOT_TOKEN')
GEMINI_KEY = env('GEMINI_KEY')