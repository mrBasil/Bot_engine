from utils.db_api.db import getCon

from data.config import STOPPER, DESCRIPTION, PRICE

'''
add_ - добавить
set_ - настроить или изменить
del_ - удалить
get_  - получить
'''


async def get_all_id(game_id):

    SET = [
        str(game_id)
    ]

    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    set_id = []
    try:
        all_id = cursor.execute("SELECT ID FROM MISSION WHERE GAME_ID=?", (SET)).fetchall()
        for id_m in all_id:
            set_id.append(id_m[0])

        con.close()
        return set_id
    except:
        print("i can't to get set all id where the mission's game_ID is: " + str(game_id))
        con.close()
        return None
async def get_game_id(mission_id):
    SET = [
        str(mission_id)
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT GAME_ID FROM MISSION WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get GAME_ID where the MISSION's id is: " + str(mission_id))
        con.close()
        return None
async def del_mission(mission_id):
    '''

    '''
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("DELETE FROM MISSION WHERE ID='" + str(mission_id) + "'")
        con.commit()
        con.close()
        return True
    except:
        print("i can't to delete a MISSIONS where id is : " + str(mission_id))
        con.commit()
        con.close()
        return False

async def add_mission(user_id, game_id):
    '''
      Создает новую миссию
      '''
    SET = [
        game_id,
        user_id,
        STOPPER,
        DESCRIPTION,
        "Задание "
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute(
                "INSERT INTO MISSION (GAME_ID, USER_ID, CAPTURE_TOKEN, DESCRIPTION, TITLE) VALUES (?,?,?,?,?)",
                SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to add a new MISSION")
        con.commit()
        con.close()
        return False


async def set_title(mission_id, title):
    SET = [
        title,
        mission_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE MISSION SET TITLE =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a title where the mission's id is: " + str(id))
        con.commit()
        con.close()
        return False

async def get_title(mission_id):
    SET = [
        str(mission_id)
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT TITLE FROM MISSION WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get title where the MISSION's id is: " + str(id))
        con.close()
        return None

async def set_description(mission_id, description):
    SET = [
        description,
        mission_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE MISSION SET DESCRIPTION =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a DESCRIPTION where the mission's id is: " + str(mission_id))
        con.commit()
        con.close()
        return False
async def get_description(mission_id):
    SET = [
        str(mission_id)
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT DESCRIPTION FROM MISSION WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get DESCRIPTION where the MISSION's id is: " + str(mission_id))
        con.close()
        return None

async def set_over_time(mission_id, over_time):
    SET = [
        over_time,
        mission_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE MISSION SET OVER_TIME =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a OVER_TIME where the mission's id is: " + str(mission_id))
        con.commit()
        con.close()
        return False
async def get_over_time(mission_id):
    SET = [
        str(mission_id)
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT OVER_TIME FROM MISSION WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get OVER_TIME where the MISSION's id is: " + str(mission_id))
        con.close()
        return None

async def set_capture_token(mission_id, capture_token):
    SET = [
        capture_token,
        mission_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE MISSION SET CAPTURE_TOKEN =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a CAPTURE_TOKEN where the mission's id is: " + str(mission_id))
        con.commit()
        con.close()
        return False
async def get_capture_token(mission_id):
    SET = [
        str(mission_id)
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT CAPTURE_TOKEN FROM MISSION WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get CAPTURE_TOKEN where the MISSION's id is: " + str(mission_id))
        con.close()
        return None

async def set_number(mission_id, number):
    SET = [
        number,
        mission_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE MISSION SET NUMBER =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a NUMBER where the mission's id is: " + str(mission_id))
        con.commit()
        con.close()
        return False
async def get_number(mission_id):
    SET = [
        str(mission_id)
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT NUMBER FROM MISSION WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get NUMBER where the MISSION's id is: " + str(mission_id))

        con.close()
        return None

async def set_capture(id, capture):

    SET = [
        capture,
        id
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:

        cursor.execute("UPDATE MISSION SET CAPTURE=(?) WHERE ID=? ", (SET))
        con.commit()
        con.close()
        return True
    except:
        print("i can't to update CAPTURE where MISSION's id is" + str(id))
        con.commit()
        con.close()
        return False
