from os import getenv

API_ID = int(getenv("API_ID", "7217645")) #optional
API_HASH = getenv("API_HASH", "78ba6352dd5cdc166fdef5aa84ba7c67") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1793699293").split()))
OWNER_ID = int(getenv("OWNER_ID", "1793699293"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/Roninopp/userboooot")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "1BVtsOKMBu0wCUPfFNnMRtIB-920Wuk1Uu0Ujw3r_ilouGQRJrjKoJ4cavTroZpKAmZ2k3U042CIW3uZbZsKN3H8aQQckQ_E3XyONuj6tJhaYnOECF2ATc-bvjgBTcwPkuXTz3tWe4uSiSqQQ6VWRo3MWzLU8Pscgk0qE2J75gQZvWzrMzS0K8Q0HZdlz0QVoDzF6dCEARguEIbllyD4GUjp6VbIqBdSDZ3MKA99beEyLNSfLdeWJZNGlO6cj21WNSJGg2aR49krCg8TrRPiiDOYNpgBmOncitnQUrod-yj2a4oCyVWoYzfISE--9Nh5u_jzmxam_4Ghl_WiIP3iXkSdHZkvRAqE=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
