from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста


'''Data base settings'''

DB_PATH = env.str("DB_PATH")
DB_IP = env.str("DB_IP")
DB_PORT = env.str("DB_PORT")
DB_USER = env.str("DB_USER")
DB_PASSWORD = env.str("DB_PASSWORD")

# urls

URL_CHANEL_MQ = env.str("URL_CHANEL_MQ")

# path to file


STOPPER = env.str("STOPPER")
DESCRIPTION = env.str("DESCRIPTION")
PRICE = env.str("PRICE")