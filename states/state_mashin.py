from aiogram.dispatcher.filters.state import StatesGroup, State

class Game_state(StatesGroup):

    Title = State()
    Description = State()
    Capture = State()
    Price = State()
    Data_relise = State()
    Data_end = State()
    Bot = State()
    Time_end = State()
    Type_game = State()

class Profile(StatesGroup):

    LogIn = State()
    Password = State()
    FirstName = State()
    LastName = State()
    CITY = State()
    Team = State()

class Mission(StatesGroup):

    Title = State()
    Description = State()
    Capture = State()
    Over_time = State()
    Number = State()

class Code(StatesGroup):

    Code_ = State()
    TypeCode = State()
    BonusTime = State()
    Comment = State()

class Hint(StatesGroup):
    Title = State()
    Description = State()
    Capture = State()
    Over_time = State()
    Number  = State()
