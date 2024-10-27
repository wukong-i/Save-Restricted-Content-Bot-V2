# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "12862156"))
API_HASH = getenv("API_HASH", "d913a2ef10183c683144ff851481d9fd")
BOT_TOKEN = getenv("BOT_TOKEN", "8080772176:AAHhFwUPIV5uhsp4Rf52qFxAxm6MBOva4n8")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5065438135").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://muthu2:muthu2@cluster0.u0sdu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002375288954")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002426144162"))
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "")
