import os
import ProxyCloud
# Bot
BOT_TOKEN = '5498539677:AAH0AH7iXdCVgOItknkYLBCBMYvIVH9Bd5o'
TG_API_ID = '9902519'
TG_API_HASH = '9d8097d05bbc90a6ed2a7a81abcd4e8a'
TG_ADMIN = 'EL_Wizard'
TG_USER = 'Stvz20'
# Database
DB_LOCAL = False
DB_HOST = 'sql.freedb.tech'
DB_HOST_USERNAME = 'freedb_hiyabo'
DB_HOST_PASSWORD = '?vj&ZrZhGu5txSW'
DB_NAME = 'freedb_educaDb'

if DB_LOCAL:
    # Database Local
    DB_HOST = ''
    DB_HOST_USERNAME = ''
    DB_HOST_PASSWORD = ''
    DB_NAME = 'clutilprodb'
