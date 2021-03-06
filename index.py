import asyncio
import os

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import defer_call, info as session_info, run_async, run_js



chat_msgs = []
online_users = set()

port_number = 1000;


MAX_MESSAGES_COUNT = 250

async def main():
    global chat_msgs
    
    put_markdown("## \U0001F33F Самый ламповый чат")

    msg_box = output()
    put_scrollable(msg_box, height=245, keep_bottom=True)

    nickname = await input("Вход в чат", required=True, placeholder="Введите имя", validate=lambda n: "Человек с таким ником уже в чате" if n in online_users or n == '📢' else None)
    online_users.add(nickname)

    chat_msgs.append(('📢', f'`{nickname}` теперь в чате!'))
    msg_box.append(put_markdown(f'📢 `{nickname}` теперь в чате!'))

    refresh_task = run_async(refresh_msg(nickname, msg_box))

    while True:

        data = await input_group("", [
            input(placeholder="Текст сообщения ...", name="msg"),
            actions(name="cmd", buttons=[ "Отправить", {'label': "Выйти из чата", 'type': 'cancel'}])],
             validate = lambda m: ('msg', "Введите текст сообщения!") if m["cmd"] == "Отправить" and not m['msg'] else None)

    
        if data is None:
            break

        msg_box.append(put_markdown(f"`{nickname}` {data['msg']}"))
        chat_msgs.append((nickname, data['msg']))

    refresh_task.close()

    online_users.remove(nickname)
    toast("Вы вышли из чата!")
    msg_box.append(put_markdown(f'📢 `{nickname}` Больше не в чате!'))
    chat_msgs.append(('📢', f' `{nickname}` Больше не в чате!'))

    put_buttons(['Перезайти'], onclick=lambda btn:run_js('window.location.reload()'))

async def refresh_msg(nickname, msg_box):
    global chat_msgs
    last_idx = len(chat_msgs)

    while True:
        await asyncio.sleep(1)
        
        for m in chat_msgs[last_idx:]:
            if m[0] != nickname: # if not a message from current user
                msg_box.append(put_markdown(f"`{m[0]}` {m[1]}"))
        
        # remove expired
        if len(chat_msgs) > MAX_MESSAGES_COUNT:
            chat_msgs = chat_msgs[len(chat_msgs) // 2:]
        
        last_idx = len(chat_msgs)

if __name__ == "__main__":
    start_server(main, port=port_number, debug=True, cdn=False)
    
    
    
  


    


