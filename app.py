from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from controllers.conectores import conjuncion, disyuncion_inclusiva, disyuncion_exclusiva
from controllers.estructura import crear

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", include_in_schema=False, name="home")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html")

@app.post("/resultado", include_in_schema=False, name="resultado")
async def validate(request: Request, txt_input: str = Form(...)):
    return templates.TemplateResponse(request, "home.html", {"input": txt_input})
    
@app.get("/conjuncion", include_in_schema=False, name="conjuncion")
def conjuncion(request: Request):
    result = crear("p∧q")
    return templates.TemplateResponse(request, "conjuncion.html", {"result": result})

@app.get("/disyuncion-inclusiva", include_in_schema=False, name="disyuncion-inclusiva")
def disyuncion(request: Request):
    return templates.TemplateResponse(request, "disyuncion_inclusiva.html")

@app.get("/disyuncion-exclusiva", include_in_schema=False, name="disyuncion-exclusiva")
def disyuncion(request: Request):
    return templates.TemplateResponse(request, "disyuncion_exclusiva.html")
    
@app.get("/condicion", include_in_schema=False, name="condicion")
def condicion(request: Request):
    return templates.TemplateResponse(request, "condicion.html")

@app.get("/bicondicion", include_in_schema=False, name="bicondicion")
def bicondicion(request: Request):
    return templates.TemplateResponse(request, "bicondicion.html")