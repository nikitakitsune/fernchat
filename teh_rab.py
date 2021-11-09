import asyncio
import os

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import defer_call, info as session_info, run_async, run_js
from pywebio_online_chat import port_number


async def main():
	put_markdown("## ❌ технические работы \nК сожалению чат пока недоступен")
	put_image('https://ru.meming.world/images/ru/thumb/7/78/%D0%A8%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BA%D0%BE%D1%82_3.jpg/300px-%D0%A8%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BA%D0%BE%D1%82_3.jpg')

    

if __name__ == "__main__":
    start_server(main, port=port_number, debug=True, cdn=False)
