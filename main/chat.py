# import asyncio
#
# from pywebio import start_server
# from pywebio.input import *
# from pywebio.output import *
# from pywebio.session import defer_call, info as session_info, run_async, run_js
#
# class Chat:
#     chat_msgs = []
#     online_users = set()
#
#     MAX_MESSAGES_COUNT = 100
#
#
#     async def main(self):
#         global chat_msgs
#
#         put_markdown("## 💬 Welcome to this Chat!")
#
#         msg_box = output()
#         put_scrollable(msg_box, height=500, keep_bottom=True, border=True)
#
#         nickname = await input('Join the chat!', required=True, placeholder='Enter your name',
#                                validate=lambda n:'A user with this nickname has already joined the chat. Please, choose your nickname and try again...' if n in online_users else None)
#
#         self.online_users.add(nickname)
#
#         chat_msgs.append(('🔉', f'{nickname} has joined the chat!'))
#         msg_box.append(put_markdown(f'🔉 {nickname} has joined the chat!'))
#
#         refresh_task = run_async(self.refresh_msg(nickname, msg_box))
#
#         while True:
#             data = await input_group('💭 New message', [
#                 input(placeholder='Text a message ...', name='msg'),
#                 actions(name='cmd', buttons=['Send', {'label': 'Leave the chat', 'type':'cancel'}])
#             ], validate=lambda m: ('msg','Type something here!') if m['cmd']=='Send' and not m['msg'] else None)
#
#             if data is None:
#                 break
#
#             msg_box.append(put_markdown(f"{nickname}: {data['msg']}"))
#             chat_msgs.append((nickname, data['msg']))
#
#         refresh_task.close()
#
#         self.online_users.remove(nickname)
#         toast('You have left the chat!')
#         msg_box.append(put_markdown(f'🔉The user {nickname} has left the chat!'))
#         chat_msgs.append(('🔉', f' the user {nickname} has left the chat!'))
#
#
#         put_buttons(['Join again'], onclick=lambda btn: run_js('window.location.reload()'))
#
#     async def refresh_msg(self, nickname, msg_box):
#         global chat_msgs
#         last_idx = len(chat_msgs)
#
#         while True:
#             await asyncio.sleep(1)
#
#             for m in chat_msgs[last_idx:]:
#                 if m[0] != nickname:
#                     msg_box.append(put_markdown(f"{m[0]}:{m[1]}"))
#
#             if len(chat_msgs) > self.MAX_MESSAGES_COUNT:
#                 chat_msgs =chat_msgs[len(chat_msgs) // 2:]
#
#             last_idx = len(chat_msgs)
#
#
#     if __name__ == "__main__":
#         start_server(main, debug=True, port=8080, cdn=False)
#
