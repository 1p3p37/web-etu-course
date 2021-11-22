import sqlite3

import tortoise.queryset
from tortoise.fields import CharField
from tortoise.functions import Count

from core.db import sql_connection
from sqlite3 import Error
from tortoise import Model
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise import Tortoise, fields, run_async
from tortoise.models import Model
from datetime import datetime

# from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
'''
def sql_table(con):
    cursorObj = con.cursor()

    cursorObj.execute(
        "CREATE TABLE User(email integer PRIMARY KEY, password text)")

    con.commit()


con = sql_connection()
sql_table(con)'''


class User(Model):
    # fields are null = False by default but i specified it for clarity
    id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=20, null=False, unique=True)
    email = fields.CharField(max_length=200, null=False, unique=True)
    password = fields.CharField(max_length=100, null=False)
    is_verified = fields.BooleanField(default=False)
    join_date = fields.DatetimeField(default=datetime.utcnow)

    def gall(self) -> tuple[CharField, CharField, CharField]:
        return self.username, self.email, self.password


# user_pydanticIn will be used to create users since it allows
# readOnly fields same for all the others
user_pydantic = pydantic_model_creator(User, name="User", exclude=("is_verified",))
user_pydanticIn = pydantic_model_creator(User, name="UserIn", exclude_readonly=True, exclude=("is_verified", 'join_date'))
user_pydanticOut = pydantic_model_creator(User, name="UserOut", exclude=("password",))


async def runn():
    print("aboba")
    await Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()
    user = await User.create(username="amogus", email="amogus1337@mail.ru", password="12345")
    print(user_pydanticOut.)




if __name__ == "__main__":
    run_async(runn())
