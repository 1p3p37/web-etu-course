import jinja2
from fastapi import FastAPI, Request, Form, Query
from fastapi.responses import HTMLResponse
from fastapi.responses import PlainTextResponse
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

import H_p
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from babel.plural import PluralRule
import glob
import json

from etuWEB.models import *
from typing import List
from etuWEB.authentication import (get_password_hash)

# signails
from tortoise.signals import post_save
from typing import List, Optional, Type
from tortoise import BaseDBAsyncClient

import trans

app = FastAPI()


# uvicorn main:app --reload
# sudo lsof -t -i tcp:8000 | xargs kill -9
# https://phrase.com/blog/posts/fastapi-i18n/amp/


@post_save(User)
async def create_user_ch(
        sender: "Type[User]",
        instance: User,
        created: bool,
        using_db: "Optional[BaseDBAsyncClient]",
        update_fields: List[str]) -> None:
    if created:
        user_ch_obj = await User_in_chat.create(
            user_name=instance.username, owner=instance)
        await user_ch_pydantic.from_tortoise_orm(user_ch_obj)
        # send email functionality
        # await send_email([instance.email], instance)


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

default_fallback = 'en'
languages = {}
locales = ""
language_list = glob.glob("languages/*.json")
for lang in language_list:
    filename = lang
    languages1 = filename.split('.')[0]
    lang_code = languages1.split('/')[1]

    # lang_code = filename[1].split('.')[0]

    locales += lang_code

    with open(lang, 'r', encoding='utf8') as file:
        languages[lang_code] = json.load(file)

"""translations = get_gettext_translations()
env = jinja2.Environment(extensions=["jinja2.ext.i18n"])
env.install_gettext_translations(translations)
"""

# post
"""
@app.get(f"/All1/", response_class=HTMLResponse)
#async def All1(request: Request, locale: str = None ):
async def All1(request: Request, locale: str = Query("en", description="Query inf")):
    print("{} | | |  _---------_________-------------_________________---_____ ||||||||||||||||||||||")

    if (locale not in locales) or (locale is None):
        locale = default_fallback
        print("biba")

    result = {"request": request}
    result.update(languages[locale])
    print(result)
    return templates.TemplateResponse("index.html", result)


@app.post("/All2/{same}", response_class=HTMLResponse)
#async def All2get(request: Request, same1: str = Query("en", description="Query inf"), same: str):
async def All2get(request: Request, same: str):
    print("{} | | |  _---------_________-------------_________________---_____ |||||||||||||||||||||||||||||||||||||||")
    if same == 'eng-lang':
        print("1aBOBOBAAA BA")
        locale = default_fallback
    elif same == 'rus-lang':
        print("2aABOBUSA")
        locale = 'ru'
    else:
        locale = default_fallback
    result = {"request": request}
    result.update(languages[locale])
    print(result)
    return templates.TemplateResponse("index2.html", result)

"""


@app.get("/memes/", response_class=HTMLResponse)
async def memes_get(request: Request, locale: str = Query("en", description="Query inf")):
    print("{1}")
    result = {"request": request}
    result.update(languages[locale])
    print(result)
    return templates.TemplateResponse("index2.html", result)


@app.post("/memes/")
async def memes(request: Request, action: str = Form(...)):
    print("{2}")
    locale = default_fallback
    result = {"request": request}
    if action == 'eng-lang':
        print("en")
        result.update(languages['en'])
    elif action == 'rus-lang':
        print("ru")
        result.update(languages['ru'])
    else:
        print("шотонетак")
        result.update(languages[locale])
    return templates.TemplateResponse("index2.html", result)


@app.post('/registration')
async def user_registration(user: user_pydanticIn):
    user_info = user.dict(exclude_unset=True)
    user_info['password'] = get_password_hash(user_info['password'])
    user_obj = await User.create(**user_info)
    new_user = await user_pydantic.from_tortoise_orm(user_obj)
    print(user.dict())
    return {"status": "ok",
            "data":
                f"Hello {new_user.username} thanks for choosing our services. Please check your emai"
                f"l inbox and click on the link to confirm your registration."}


register_tortoise(
    app,
    db_url='sqlite://database.sqlite3',
    modules={'models': ['etuWEB.models']},
    generate_schemas=True,
    add_exception_handlers=True
)

"""
    if action == 'eng-lang':
        print("1aBOBOBAAA BA")
        locale = default_fallback
        result = {"request": request}
        result.update(languages[locale])
        return templates.TemplateResponse("index2.html", result)
    elif action == 'rus-lang':
        print("2aBOBOBAAA BA")
        locale = 'ru'
        result = {"request": request}
        result.update(languages[locale])
        return templates.TemplateResponse("index2.html", result)
    else:
        result = {"request": request}
        result.update(languages[locale])
        return templates.TemplateResponse("index2.html", result)"""

"""@app.get("/All1/")
async def aboltus(request: Request):
    return All1(request, "en")"""


@app.get("/")
async def root():
    return {"АМОГУС"}


@app.get("/All/", response_class=HTMLResponse)
async def all_page():
    return H_p.all_html


@app.get("/Billy/", response_class=HTMLResponse)
async def billy_page():
    return H_p.Billy


@app.get("/Rybov/", response_class=HTMLResponse)
async def rybov_page():
    return H_p.rybov_html


@app.get("/Gosling/", response_class=HTMLResponse)
async def gosling_page():
    return H_p.ryan_html


@app.get("/Cat/", response_class=HTMLResponse)
async def cat_page():
    return H_p.cat_html


@app.get("/Filth/", response_class=HTMLResponse)
async def filth_page():
    return H_p.filth_html


@app.get("/Papi4/", response_class=HTMLResponse)
async def papi4_get(request: Request, locale: str = Query("en", description="Query inf")):
    result = {"request": request}
    result.update(languages[locale])
    return templates.TemplateResponse("Papi4.html", result)


@app.post("/Papi4/")
async def papi4(request: Request, action: str = Form(...)):
    locale = default_fallback
    result = {"request": request}
    if action == 'eng-lang':
        result.update(languages['en'])
    elif action == 'rus-lang':
        result.update(languages['ru'])
    else:
        result.update(languages[locale])
    return templates.TemplateResponse("Papi4.html", result)


"""
@app.get("/Text/ru1", response_class=PlainTextResponse)
async def text():
    meme = "— Писать курсач больнее, чем родить ребёнка. \n— <Ты когда-нибудь рожал ребенка?>\n" \
           "— Нет, но женщины иногда говорят <Давай заведем ещё одного>, но ни один студент не скажет " \
           "\n<А напишу-ка я ещё один курсач>!"
    return meme


@app.get("/Text/en", response_class=PlainTextResponse)
async def trans_text():
    trans_meme = "— Writing a coursework is more painful than having a baby. \n— <Have you ever had a baby?>\n" \
                 "— No, but women sometimes say <Let's have another one>, but no student will say\n" \
                 "<I'll write another coursework>!"
    return trans_meme



@app.get("/Text/en1", response_class=PlainTextResponse)
async def trans1_text():
    meme = "— Писать курсач больнее, чем родить ребёнка. \n— <Ты когда-нибудь рожал ребенка?>\n" \
           "— Нет, но женщины иногда говорят <Давай заведем ещё одного>, но ни один студент не скажет " \
           "\n<А напишу-ка я ещё один курсач>!"
    print(trans(meme))
    return trans(meme)
"""
