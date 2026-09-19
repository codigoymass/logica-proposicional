from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from estructura import crear

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", include_in_schema=False, name="home")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html")
    
@app.get("/conjuncion", include_in_schema=False, name="conjuncion")
def conjuncion(request: Request):
    txt_input = "p∧q"
    tabla = None
    error = None

    try:
        tabla = crear(txt_input)
    except ValueError as e:
        error = str(e)

    return templates.TemplateResponse(
        request,
        "conjuncion.html",
        {"input": txt_input, "tabla": tabla, "error": error}
    )

@app.get("/disyuncion-inclusiva", include_in_schema=False, name="disyuncion-inclusiva")
def disyuncion(request: Request):
    txt_input = "p∨q"
    tabla = None
    error = None

    try:
        tabla = crear(txt_input)
    except ValueError as e:
        error = str(e)

    return templates.TemplateResponse(
        request,
        "disyuncion_inclusiva.html",
        {"input": txt_input, "tabla": tabla, "error": error}
    )

@app.get("/disyuncion-exclusiva", include_in_schema=False, name="disyuncion-exclusiva")
def disyuncion_exclusiva(request: Request):
    txt_input = "p⊕q"
    tabla = None
    error = None

    try:
        tabla = crear(txt_input)
    except ValueError as e:
        error = str(e)

    return templates.TemplateResponse(
        request,
        "disyuncion_exclusiva.html",
        {"input": txt_input, "tabla": tabla, "error": error}
    )
    
@app.get("/condicion", include_in_schema=False, name="condicion")
def condicion(request: Request):
    txt_input = "p→q"
    tabla = None
    error = None

    try:
        tabla = crear(txt_input)
    except ValueError as e:
        error = str(e)

    return templates.TemplateResponse(
        request,
        "condicion.html",
        {"input": txt_input, "tabla": tabla, "error": error}
    )

@app.get("/bicondicion", include_in_schema=False, name="bicondicion")
def bicondicion(request: Request):
    txt_input = "p↔q"
    tabla = None
    error = None

    try:
        tabla = crear(txt_input)
    except ValueError as e:
        error = str(e)

    return templates.TemplateResponse(
        request,
        "bicondicion.html",
        {"input": txt_input, "tabla": tabla, "error": error}
    )

@app.post("/resultado", include_in_schema=False, name="resultado")
async def validate(request: Request, txt_input: str = Form(...)):
    tabla = None
    error = None

    try:
        tabla = crear(txt_input)
    except ValueError as e:
        error = str(e)

    return templates.TemplateResponse(
        request,
        "home.html",
        {"input": txt_input, "tabla": tabla, "error": error}
    )