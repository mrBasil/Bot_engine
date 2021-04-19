from utils.db_api.db import getCon

from data.config import STOPPER, DESCRIPTION, PRICE

'''
add_ - добавить
set_ - настроить или изменить
del_ - удалить
get_  - получить
'''

TITLE = "Новая игра"

async def get_all_id(user_id):
    SET = [
        str(user_id)
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    set_id = []
    try:
        all_id = cursor.execute("SELECT ID FROM GAME WHERE OWNER_USER_ID=?", (SET)).fetchall()
        for id in all_id:
            set_id.append(id[0])
        con.close()
        return set_id
    except:
        print("i can't to get set all id where the game's OWNER_USER_ID is: " + str(user_id))
        con.close()
        return None

async def add_new_game(user_id):
    '''
    Создает новую игру
    '''

    SET = [
        TITLE,
        str(user_id),
        DESCRIPTION,
        PRICE,
        'PERSONAL',
        'NOW',
        STOPPER
    ]
    print(STOPPER)
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()

    try:
        cursor.execute(
            "INSERT INTO GAME (TITLE, OWNER_USER_ID, DESCRIPTION, PRICE, TYPE, DATA_CREATE, TITLE_KEY) VALUES (?,?,?,?,?,?,?)", SET)
        con.commit()
        con.close()
        return True
    
    except:
        print("i can't to add a new GAME")
        con.commit()
        con.close()
        return False

async def del_game(id):
    '''

    '''
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("DELETE FROM GAME WHERE ID='" + str(id) + "'")
        con.commit()
        con.close()
        return True
    except:
        print("i can't to delete a GAME where id is : " + str(id))
        con.commit()
        con.close()
        return False

async def set_title(id, title):

    SET = [
        title,
        id
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE GAME SET TITLE =? WHERE ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a title where the game's id is: " + str(id))
        con.commit()
        con.close()
        return False
async def get_title(id):

    SET = [
        str(id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT TITLE FROM GAME WHERE ID=?", (SET) ).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get title where the game's id is: " + str(id))
        con.close()
        return None


async def set_description(id, description):
    SET = [

        description,
        id
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE GAME SET DESCRIPTION=? WHERE ID=?", (SET))
        con.commit()
        con.close()
        return True
    except:
        print("i can't to update a description where the game's id is" + str(id))
        return False
async def get_description(id):

    SET = [
        str(id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT DESCRIPTION FROM GAME WHERE ID=?", (SET) ).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get DESCRIPTION where the game's id is: " + str(id))
        con.close()
        return None

async def set_price(id, price):

    if str(price).isdigit():

        SET = [
            price,
            id
        ]

        con = await getCon()
        #con = getCon()
        cursor = con.cursor()
        try:
            cursor.execute("UPDATE GAME SET PRICE=? WHERE ID=?", (SET))
            con.commit()
            con.close()
            return True
        except:
            print("i can't to update a price where the game's id is" + str(id))
            return False
    else:
        print( "in the string are the letters")
        return False
async def get_price(id):
    SET = [
        str(id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT PRICE FROM GAME WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get a price where the game's id is: " + str(id))
        con.close()
        return None

async def set_org_1(id, user_id):
    SET = [

        user_id,
        id
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE GAME SET ORG_1_USER_ID=? WHERE ID=?", (SET))
        con.commit()
        con.close()
        return True
    except:
        print("i can't to update a ORG_1_USER_ID where the game's id is" + str(id))
        return False
async def get_org_1(id):
    SET = [
        str(id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT ORG_1_USER_ID FROM GAME WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get a ORG_1_USER_ID where the game's id is: " + str(id))
        con.close()
        return None

async def set_org_2(id, user_id):
    SET = [

        user_id,
        id
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE GAME SET ORG_2_USER_ID=? WHERE ID=?", (SET))
        con.commit()
        con.close()
        return True
    except:
        print("i can't to update a ORG_2_USER_ID where the game's id is" + str(id))
        return False
async def get_org_2(id):
    SET = [
        str(id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT ORG_2_USER_ID FROM GAME WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get a ORG_2_USER_ID where the game's id is: " + str(id))
        con.close()
        return None

async def set_type(id, type):
    if type == 1:
        t = "PERSONAL"
    else:
        t = "TEAM"

    SET = [

        t,
        id
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE GAME SET TYPE=? WHERE ID=?", (SET))
        con.commit()
        con.close()
        return True
    except:
        print("i can't to update a TYPE where the game's id is" + str(id))
        return False
async def get_type(id):
    SET = [
        str(id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT TYPE FROM GAME WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get a TYPE where the game's id is: " + str(id))
        con.close()
        return None

async def set_capture(id,capture):
    #capture = f.read()
    #print(capture)
    SET = [
        capture,
        id
    ]
    # print(photo)
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:

        cursor.execute("UPDATE GAME SET CAPTURE=(?) WHERE ID=? ", (SET))
        con.commit()
        con.close()
        return True
    except:
        print("i can't to update CAPTURE where game's id is" + str(id))
        con.commit()
        con.close()
        return False

async def get_capture(id):
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    SET=[
        id
    ]

    ph = cursor.execute("SELECT CAPTURE FROM GAME WHERE id=?", (SET)).fetchall()


    photo = (ph[0][0]).read()
    ph[0][0].close()
    #print(dir(BlobReader))
    #print(photo)

    file = open('D:\\pythonProject5\\captire\\newP.jpg', 'wb')

    file.write(photo)

    file.close()

    con.close()

async def set_capture_token(id, token):
    SET = [

        token,
        id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE GAME SET TITLE_KEY=? WHERE ID=?", (SET))
        con.commit()
        con.close()
        return True
    except:
        print("i can't to update a TITLE_KEY where the game's id is" + str(id))
        return False
async def get_capture_token(id):
    SET = [
        str(id)
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT TITLE_KEY FROM GAME WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get a TITLE_KEY where the game's id is: " + str(id))
        con.close()
        return None

async def set_dataEnd(id, data_end):
    '''

    :param id:
    :param data_end: должна быть формата дд.мм.гггг
    :return:
    '''
    SET = [

        data_end,
        id
    ]

    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:

        cursor.execute("UPDATE GAME SET DATE_END=(?) WHERE ID=? ", (SET))
        con.commit()
        con.close()
        return True
    except:
        print("i can't to update DATA_END where game's id is" + str(id))
        con.commit()
        con.close()
        return False
async def get_dataEnd(id):
    SET = [
        str(id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT DATE_END FROM GAME WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get a DATE_END where the game's id is: " + str(id))
        con.close()
        return None

async def set_timeEnd(id, time_end):
    '''

    :param id:
    :param data_end: должна быть формата дд.мм.гггг
    :return:
    '''
    SET = [

        time_end,
        id
    ]

    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:

        cursor.execute("UPDATE GAME SET TIME_END=(?) WHERE ID=? ", (SET))
        con.commit()
        con.close()
        return True
    except:
        print("i can't to update DATA_END where game's id is" + str(id))
        con.commit()
        con.close()
        return False
async def get_timeEnd(id):
    SET = [
        str(id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT TIME_END FROM GAME WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get a TIME_END where the game's id is: " + str(id))
        con.close()
        return None

async def set_dataRelise(id, data_relise):
    '''

    :param id:
    :param data_end: должна быть формата дд.мм.гггг
    :return:
    '''
    SET = [

        data_relise,
        id
    ]

    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:

        cursor.execute("UPDATE GAME SET DATA_RELESE=(?) WHERE ID=? ", (SET))
        con.commit()
        con.close()
        return True
    except:
        print("i can't to update DATA_RELESE where game's id is" + str(id))
        con.commit()
        con.close()
        return False
async def get_dataRelise(id):
    SET = [
        str(id)
    ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT DATA_RELESE FROM GAME WHERE ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get a DATA_RELESE where the game's id is: " + str(id))
        con.close()
        return None