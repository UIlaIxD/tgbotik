import psycopg
from bdconfig import host, user, password, bd_name


conn = psycopg.Connection.connect(
    host=host,
    user=user,
    password=password,
    dbname=bd_name
    )
conn.autocommit = True
cur = conn.cursor()
try:
    cur.execute("")
except:
    print('ahahahah')
conn.close()
cur.close()











# async def psycopgtest():
#     with psycopg.AsyncConnection.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=bd_name
#     ) as aconn:
#         with aconn.cursor() as acur:
#             acur.execute("""
#                 CREATE TABLE testik (
#                     id serial PRIMARY KEY,
#                     num integer,
#                     data text
#                 )""")
# asyncio.run(psycopgtest())


# @dp.message(F.text.lower() == 'testo')
# async def testik(message: Message):
#     idchat = message.chat.id
#     idthread = message.message_thread_id
#     print(idchat)
#     print(idthread)


# @dp.message()
# async def xdef(message: Message):
#     if message.chat.id == -1002620398013 and message.message_thread_id == 1087:
#         print('otvet')


