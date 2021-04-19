
from .db import getCon


async def get_limit_game(user_id):
    SET = [
        str(user_id)
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()

    try:
        limit_game = cursor.execute("SELECT LIMITE_GAME FROM ORG WHERE USER_ID=?", (SET)).fetchall()

        con.close()
        return limit_game[0][0]
    except:
        print("i can't to get limit where the org'sUSER_ID is: " + str(user_id))
        con.close()
        return None

async def add_new_org(user_id):
    '''
        Создает нового орга
        '''

    SET = [
        user_id,
        "5",
        "No team"
    ]

    con = await getCon()
    # con = getCon()
    cursor = con.cursor()

    try:
        cursor.execute(
            "INSERT INTO ORG (USER_ID, LIMITE_GAME, TEAM) VALUES (?,?,?)", SET)
        con.commit()
        con.close()
        return True
    except:
        print("i can't to add a new ORG")
        con.commit()
        con.close()
        return False


async def set_login(user_id, login):
    SET = [
            login,
            user_id
        ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE ORG SET LOGIN =? WHERE USER_ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a login where the org's user_id is: " + str(user_id))
        con.commit()
        con.close()
        return False

async def get_login(user_id):
    SET = [
        user_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT LOGIN FROM ORG WHERE USER_ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get LOGIN where the ORG's USER_ID is: " + str(id))
        con.close()
        return None


async def set_pas(user_id, password):
    SET = [
            password,
            user_id
        ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE ORG SET PASS =? WHERE USER_ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a PASS where the org's user_id is: " + str(user_id))
        con.commit()
        con.close()
        return False

async def get_pas(user_id):
    SET = [
        user_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT PASS FROM ORG WHERE USER_ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get PASS where the ORG's USER_ID is: " + str(id))
        con.close()
        return None


async def set_first_name(user_id, first_name):
    SET = [
            first_name,
            user_id
        ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE ORG SET FIRST_NAME =? WHERE USER_ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a FIRST_NAME where the org's user_id is: " + str(user_id))
        con.commit()
        con.close()
        return False

async def get_first_name(user_id):
    SET = [
        user_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT FIRST_NAME FROM ORG WHERE USER_ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get FIRST_NAME where the ORG's USER_ID is: " + str(id))
        con.close()
        return None


async def set_last_name(user_id, last_name):
    SET = [
            last_name,
            user_id
        ]
    con = await getCon()
    #con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE ORG SET LAST_NAME =? WHERE USER_ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a LAST_NAME where the org's user_id is: " + str(user_id))
        con.commit()
        con.close()
        return False

async def get_last_name(user_id):
    SET = [
        user_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT LAST_NAME FROM ORG WHERE USER_ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get LAST_NAME where the ORG's USER_ID is: " + str(id))
        con.close()
        return None


async def set_city(user_id, city):
    SET = [
        city,
        user_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE ORG SET CITY =? WHERE USER_ID=?", SET)
        con.commit()
        con.close()
        return True

    except:
        print("i can't to update a CITY where the org's user_id is: " + str(user_id))
        con.commit()
        con.close()
        return False

async def get_city(user_id):
    SET = [
        user_id
    ]
    con = await getCon()
    # con = getCon()
    cursor = con.cursor()
    try:
        title = cursor.execute("SELECT CITY FROM ORG WHERE USER_ID=?", (SET)).fetchall()
        con.close()
        return str(title[0][0]).rstrip()
    except:
        print("i can't to get CITY where the ORG's USER_ID is: " + str(id))
        con.close()
        return None