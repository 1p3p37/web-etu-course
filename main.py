import jinja2
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import PlainTextResponse
import H_p
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from babel.plural import PluralRule
import glob
import json

import trans
app = FastAPI()
# uvicorn main:app --reload

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

default_fallback = 'en'
languages = {}
locales = ""
language_list = glob.glob("languages/*.json")
print(language_list)
for lang in language_list:
    filename = lang#.split('\\')
    languages1 = filename.split('.')[0]
    lang_code = languages1.split('/')[1]
    print(lang_code)

    #lang_code = filename[1].split('.')[0]

    locales += lang_code



    with open(lang, 'r', encoding='utf8') as file:
        languages[lang_code] = json.load(file)

"""translations = get_gettext_translations()
env = jinja2.Environment(extensions=["jinja2.ext.i18n"])
env.install_gettext_translations(translations)
"""
@app.get("/All1/{locale}", response_class=HTMLResponse)
async def All1(request: Request, locale: str):
    """for i in locales:
        if i != locale:
            locale = default_fallback
            print(locale)"""
    if locale is None:
        locale = default_fallback
        print("biba")
    print(locale)

    if((locale not in locales) or (locale is None)):
        locale = default_fallback
        print("ZALOOpa")

    result = {"request": request}
    result.update(languages[locale])

    return templates.TemplateResponse("index.html", result)
@app.get("/All1/")
async def aboltus(request: Request):
    return All1(request, "en")


@app.get("/")
async def root():
    return {"АМОГУС"}
@app.get("/All/", response_class=HTMLResponse)
async def all_page():
    return H_p.all_html
@app.get("/Billy/", response_class=HTMLResponse)
async def billy_page():
    return H_p.billy_html
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
@app.get("/Text/ru1", response_class=PlainTextResponse)
async def text():
    meme = "— Писать курсач больнее, чем родить ребёнка. \n— <Ты когда-нибудь рожал ребенка?>\n" \
           "— Нет, но женщины иногда говорят <Давай заведем ещё одного>, но ни один студент не скажет " \
           "\n<А напишу-ка я ещё один курсач>!"
    return meme
@app.get("/Text/en", response_class=PlainTextResponse)
async def trans_text():
    trans_meme = "— Writing a coursework is more painful than having a baby. \n— <Have you ever had a baby?>\n" \
            "— No, but women sometimes say <Let's have another one>, but no student will say\n"\
            "<I'll write another coursework>!"
    return trans_meme
    """
@app.get("/Text/en1", response_class=PlainTextResponse)
async def trans1_text():
    meme = "— Писать курсач больнее, чем родить ребёнка. \n— <Ты когда-нибудь рожал ребенка?>\n" \
           "— Нет, но женщины иногда говорят <Давай заведем ещё одного>, но ни один студент не скажет " \
           "\n<А напишу-ка я ещё один курсач>!"
    print(trans(meme))
    return trans(meme)



"""
"""
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""