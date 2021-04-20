from utils.db_api.db import getCon
import random

async def get_random_code():
    code = 0
    while code < 1000:
        code = round(random.random()*10000)
    return code

'''
add_ - добавить
set_ - настроить или изменить
del_ - удалить
get_  - получить
'''

async def get_all_id(mission_id):
    SET = [
        str(mission_id)
    ]
    con = await getCon()
    cursor = con.cursor()
    set_id = []
    try:
        all_id = cursor.execute("SELECT ID FROM CODE WHERE MISSION_ID=?",(SET)).fetchall()
        for id in all_id:
            set_id.append(id[0])
        con.close()
        return set_id
    except:
        print("i can't to get set all id where the code's MISSION_ID is: " + str(mission_id))
        con.close()
        return None

async def add_new_code(mission_id, game_id):
    SET = [
        mission_id,
        await get_random_code(),
        "checkpoint",
        "0",
        game_id,
        "no comment"

    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()

    try:
        cursor.execute(
            "INSERT INTO CODE (MISSION_ID, CODE, TYPE, BONUS_TIME, GAME_ID, COMMENT) VALUES (?,?,?,?,?,?)",
            SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to add a new code")
        con.commit()
        con.close()
        return False

async def del_code(code_id):
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("DELETE FROM CODE WHERE ID='" + str(code_id) + "'")
        con.commit()
        con.close()
        return True
    except:
        print("i can't to delete a CODE where id is : " + str(code_id))
        con.commit()
        con.close()
        return False

async def set_code(code_id, code):

    SET = [
        code,
        code_id
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE CODE SET CODE =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a CODE where the CODE's id is: " + str(code_id))
        con.commit()
        con.close()
        return False
async def get_code(code_id):

    SET = [
        str(code_id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        code = cursor.execute("SELECT CODE FROM CODE WHERE ID=?", (SET) ).fetchall()
        con.close()
        return str(code[0][0]).rstrip()
    except:
        print("i can't to get title where the game's id is: " + str(code_id))
        con.close()
        return None

async def set_type(code_id, type):

    SET = [
        type,
        code_id
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE CODE SET TYPE =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a TYPE where the CODE's id is: " + str(code_id))
        con.commit()
        con.close()
        return False
async def get_type(code_id):

    SET = [
        str(code_id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        type = cursor.execute("SELECT TYPE FROM CODE WHERE ID=?", (SET) ).fetchall()
        con.close()
        return str(type[0][0]).rstrip()
    except:
        print("i can't to get TYPE where the game's id is: " + str(code_id))
        con.close()
        return None

async def set_bonus_time(code_id, time):

    SET = [
        time,
        code_id
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE CODE SET BONUS_TIME =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a BONUS_TIME where the CODE's id is: " + str(code_id))
        con.commit()
        con.close()
        return False
async def get_bonus_time(code_id):

    SET = [
        str(code_id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        time = cursor.execute("SELECT BONUS_TIME FROM CODE WHERE ID=?", (SET) ).fetchall()
        con.close()
        return str(time[0][0]).rstrip()
    except:
        print("i can't to get TIME where the game's id is: " + str(code_id))
        con.close()
        return None

async def get_mission_id(code_id):

    SET = [
        str(code_id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        mission_id = cursor.execute("SELECT MISSION_ID FROM CODE WHERE ID=?", (SET) ).fetchall()
        con.close()
        return str(mission_id[0][0]).rstrip()
    except:
        print("i can't to get MISSION_ID where the game's id is: " + str(code_id))
        con.close()
        return None
async def get_game_id(code_id):

    SET = [
        str(code_id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        game_id = cursor.execute("SELECT GAME_ID FROM CODE WHERE ID=?", (SET) ).fetchall()
        con.close()
        return str(game_id[0][0]).rstrip()
    except:
        print("i can't to get GAME_ID where the game's id is: " + str(code_id))
        con.close()
        return None

async def set_comment(code_id, comment):

    SET = [
        comment,
        code_id
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE CODE SET COMMENT =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a COMMENT where the CODE's id is: " + str(code_id))
        con.commit()
        con.close()
        return False
async def get_comment(code_id):

    SET = [
        str(code_id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        comment = cursor.execute("SELECT COMMENT FROM CODE WHERE ID=?", (SET) ).fetchall()
        con.close()
        return str(comment[0][0]).rstrip()
    except:
        print("i can't to get COMMENT where the game's id is: " + str(code_id))
        con.close()
        return None