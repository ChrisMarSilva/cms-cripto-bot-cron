import json
import requests
import re
import pandas as pd
import numpy as np
import datetime as dt
from apscheduler.schedulers.blocking import BlockingScheduler

import pytz
timezone = pytz.timezone('America/Sao_Paulo')

import warnings
warnings.filterwarnings('ignore')

import cryptocompare
cryptocompare_api_key = '00ff6c8217eec5d6894a77d4bc335d5306072e0e22fc1af970bf0f68f00eb6bf'
cryptocompare.cryptocompare._set_api_key_parameter(api_key=cryptocompare_api_key)

import telebot
telegram_chat_id = '452513294'  # CMS  - '452513294'   # Mae - '1031430125'
telegram_token = '1238835452:AAGTATI9bldZfHtD2iMrvHiVztz9DguLHck'

def gerar_msg_alerta_cripto() -> str:
    dthr = dt.datetime.now(tz=timezone).strftime("%d/%m/%Y %H:%M:%S")
    msg = ''
    msg += f'<u><b>Alerta Cripto</b></u><br><br>'

    msg += f'<b>ETH/BRL</b><br>'
    msg += f'Qtd: 0,3888906600<br>'
    msg += f'P.Médio: R$ 12.857,032874<br>'
    msg += f'P.Atual: R$ 18.067,97 <b>(5,53%)</b><br>'
    msg += f'T.Invest: R$ 4.999,98<br>'
    msg += f'T.Atual: R$ 7.026,46<br>'
    msg += f'<b>Valrz: R$ 2.026,48 (40,53%)</b><br>'
    msg += f'<br>'

    msg += f'<b>XRP/BRL</b><br>'
    msg += f'Qtd: 1.599,2902220000<br>'
    msg += f'P.Médio: R$ 6,917756<br>'
    msg += f'P.Atual: R$ 7,25 <b>(5,53%)</b><br>'
    msg += f'T.Invest: R$ 11.063,50<br>'
    msg += f'T.Atual: R$ 11.596,45<br>'
    msg += f'<b>Valrz: R$ 532,95 (4,82%)</b><br>'
    msg += f'<br>'

    # msg += f'<b>#LINK/BRL</b><br>'
    # msg += f'Qtd: xxxxxxxx<br>'
    # msg += f'P.Médio: R$ xxxxxxxx<br>'
    # msg += f'P.Atual: R$ xxxxxxxx<br>'
    # msg += f'T.Invest: R$ xxxxxxxx<br>'
    # msg += f'T.Atual: R$ xxxxxxxx<br>'
    # msg += f'<b>Valrz: R$ xxxxxxxx (xxxxxxxx%)</b><br>'
    # msg += f'<br>'
    # # LINK/BRL       	 Qtd: 41,0997624500                  	 Preço Médio: R$ 194,640541                	 Preço Atual: R$ 205,51               	 Total Invest.: R$ 7.999,68             	 Total Atual: R$ 8.446,41             	 Lucro: R$ 446,73               (5,58% )

    # msg += f'<b>#LTC/BRL</b><br>'
    # msg += f'Qtd: xxxxxxxx<br>'
    # msg += f'P.Médio: R$ xxxxxxxx<br>'
    # msg += f'P.Atual: R$ xxxxxxxx<br>'
    # msg += f'T.Invest: R$ xxxxxxxx<br>'
    # msg += f'T.Atual: R$ xxxxxxxx<br>'
    # msg += f'<b>Valrz: R$ xxxxxxxx (xxxxxxxx%)</b><br>'
    # msg += f'<br>'
    # # LTC/BRL        	 Qtd: 5,7005689700                   	 Preço Médio: R$ 1.402,940661              	 Preço Atual: R$ 1.518,99             	 Total Invest.: R$ 7.997,56             	 Total Atual: R$ 8.659,11             	 Lucro: R$ 661,55               (8,27% )

    msg += f'<b>TOTAL</b><br>'
    msg += f'T.Invest: R$ 32.060,72<br>'
    msg += f'T.Atual: R$ 35.728,44<br>'
    msg += f'<b>Valrz: R$ 3.667,72 (11,44%)</b><br>'
    msg += f'<br>'

    msg += f'<i><u>{dthr}</u></i><br>'

    # msg = msg.replace('<br>', '\n')
    return msg

sched = BlockingScheduler(timezone=pytz)

@sched.scheduled_job('interval', minutes=1)
def processar():
    try:

        chat_text = gerar_msg_alerta_cripto()
        chat_text = chat_text.replace('<br>', '\n')

        bot = telebot.TeleBot(token=telegram_token)
        try:
            bot.send_message(chat_id=telegram_chat_id, text=chat_text, parse_mode="HTML", disable_web_page_preview=False)
        finally:
            bot.stop_bot()

    except Exception as e:
        print(f'Falha Geral: {str(e)}')

sched.start()

# if (__name__ == '__main__'):
#     try:
#         processar()
#         # sched = BlockingScheduler(timezone=pytz)
#         # sched.add_job(func=processar, trigger='interval', minutes=1)  # 10
#         # sched.start()
#     except Exception as e:
#         print(f'Falha Geral: {str(e)}')

# pip freeze > requirements.txt
# pip install -r requirements.txt

# heroku ps:scale clock=1

# pip install --upgrade pip
# pip install --upgrade setuptools
# pip install pytz
# pip install pandas --upgrade --no-cache-dir
# pip install numpy --upgrade --no-cache-dir
# pip install pyTelegramBotAPI --upgrade --no-cache-dir
# pip install cryptocompare --upgrade --no-cache-dir
# pip install apscheduler
