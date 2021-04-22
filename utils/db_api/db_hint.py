from utils.db_api.db import getCon

from data.config import STOPPER, DESCRIPTION, PRICE

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
    # con = getCon()
    cursor = con.cursor()
    set_id = []
    try:
        all_id = cursor.execute("SELECT ID FROM HINT WHERE MISSION_ID=?", (SET)).fetchall()
        for id_m in all_id:
            set_id.append(id_m[0])
        con.close()
        return set_id
    except:
        print("i can't to get set all id where the HINT's mission_id is: " + str(mission_id))
        con.close()
        return None

async def del_hint(hint_id):
    '''

    '''
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("DELETE FROM HINT WHERE ID='" + str(hint_id) + "'")
        con.commit()
        con.close()
        return True
    except:
        print("i can't to delete a HINT where id is : " + str(hint_id))
        con.commit()
        con.close()
        return False

async def add_hint(mission_id, game_id):
    '''
      Создает новую миссию
      '''
    SET = [
        game_id,
        mission_id,
        STOPPER,
        DESCRIPTION,
        "Подсказка"
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute(
                "INSERT INTO HINT (GAME_ID, MISSION_ID, CAPTURE_TOKEN, DESCRIPTION, TITLE) VALUES (?,?,?,?,?)",
                SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to add a new HINT" , mission_id)
        con.commit()
        con.close()
        return False

async def set_title(hint_id, title):
    SET = [
        title,
        hint_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE HINT SET TITLE =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a title where the hint's id is: " + str(hint_id))
        con.commit()
        con.close()
        return False
async def get_title(hint_id):

    SET = [
        str(hint_id)
    ]
    con = await getCon()
    cursor = con.cursor()

    try:
        title = cursor.execute("SELECT TITLE FROM HINT WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()

    except:
        print("i can't to get title where the HINT's id is: " + str(hint_id))
        con.close()
        return None

async def get_mission_id(hint_id):

    SET = [
        str(hint_id)
    ]
    con = await getCon()
    cursor = con.cursor()

    try:
        title = cursor.execute("SELECT MISSION_ID FROM HINT WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()

    except:
        print("i can't to get mission_id where the HINT's id is: " + str(hint_id))
        con.close()
        return None
async def get_game_id(hint_id):

    SET = [
        str(hint_id)
    ]
    con = await getCon()
    cursor = con.cursor()

    try:
        title = cursor.execute("SELECT GAME_ID FROM HINT WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()

    except:
        print("i can't to get game_id where the HINT's id is: " + str(hint_id))
        con.close()
        return None


async def set_description(hint_id, description):
    SET = [
        description,
        hint_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE HINT SET DESCRIPTION =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a DESCRIPTION where the hint's id is: " + str(hint_id))
        con.commit()
        con.close()
        return False
async def get_description(hint_id):
    SET = [
        str(hint_id)
    ]
    con = await getCon()
    cursor = con.cursor()

    try:
        title = cursor.execute("SELECT DESCRIPTION FROM HINT WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()

    except:
        print("i can't to get Description where the HINT's id is: " + str(id))
        con.close()
        return None

async def set_capture_token(hint_id, capture_token):
    SET = [
        capture_token,
        hint_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE HINT SET CAPTURE_TOKEN =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a CAPTURE_TOKEN where the hint's id is: " + str(hint_id))
        con.commit()
        con.close()
        return False
async def get_capture_token(hint_id):
    SET = [
        str(hint_id)
    ]
    con = await getCon()
    cursor = con.cursor()

    try:
        title = cursor.execute("SELECT CAPTURE_TOKEN FROM HINT WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()

    except:
        print("i can't to get CAPTURE_TOKEN where the HINT's id is: " + str(id))
        con.close()
        return None

async def set_over_time(hint_id, time):
    SET = [
        time,
        hint_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE HINT SET OVER_TIME =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a OVER_TIME where the hint's id is: " + str(hint_id))
        con.commit()
        con.close()
        return False
async def get_over_time(hint_id):
    SET = [
        str(hint_id)
    ]
    con = await getCon()
    cursor = con.cursor()

    try:
        title = cursor.execute("SELECT OVER_TIME FROM HINT WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()

    except:
        print("i can't to get OVER_TIME where the HINT's id is: " + str(id))
        con.close()
        return None

async def set_number(hint_id, number):
    SET = [
        number,
        hint_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE HINT SET NUMBER =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a NUMBER where the hint's id is: " + str(hint_id))
        con.commit()
        con.close()
        return False
async def get_number(hint_id):
    SET = [
        str(hint_id)
    ]
    con = await getCon()
    cursor = con.cursor()

    try:
        title = cursor.execute("SELECT NUMBER FROM HINT WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()

    except:
        print("i can't to get NUMBER where the HINT's id is: " + str(id))
        con.close()
        return None

async def set_capture(hint_id, capture):
    ''' BLOB wait '''

    SET = [
        capture,
        hint_id
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:

        cursor.execute("UPDATE HINT SET CAPTURE=(?) WHERE ID=? ", (SET))
        con.commit()
        con.close()
        return True
    except:
        print("i can't to update CAPTURE where HINT's id is" + str(id))
        con.commit()
        con.close()
        return False
