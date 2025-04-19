from config import database
from db import DB_Manager


db = DB_Manager(database)
db.create_tables()


def plus_xp(message):
    db.change('users',message.from_user.id,'xp',db.read('users',message.from_user.id,'xp')[0]+1)

def change_status(message, status_id: int, user_tag: int):
    if int(db.read('users',message.from_user.id,'status_id')[0]) == 2:
        return db.change('users',db.get_PK('users','tag',user_tag),'status_id',status_id)
    else:
        return 'недостаточно прав чтобы выполнить'
    
def delete_user(message, user_tag: int):
    if int(db.read('users',message.from_user.id,'status_id')[0]) == 2:
        return db.delete('users',db.get_PK('users','tag',user_tag))
    else:
        return 'недостаточно прав чтобы выполнить'


async def fetch_args(command: str, source: str) -> list[str]:
    return source.removeprefix(command).strip().split()