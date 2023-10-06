from fastapi import FastAPI, HTTPException
from App.Model.Curso import Curso
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

app = FastAPI()

cursos = []
mensagem = ''

@app.post("/cursos/inserir/", summary="Criar um novo curso")
async def post_curso(curso: Curso):
    cursos.append(curso)
    dicRetorno = {"message": "Curso inserido com sucesso!", "curso": curso}

    jsonRetorno = jsonable_encoder(dicRetorno)
    return JSONResponse(content=jsonRetorno, status_code=201)


@app.get("/cursos/", summary="Listar todos os cursos cadastrados")
async def get_curso():
    if len(cursos) == 0:
        raise HTTPException(status_code=404, detail="Nenhum curso cadastrado")

    jsonRetorno = jsonable_encoder(cursos)
    return JSONResponse(content=jsonRetorno, status_code=200)


@app.get("/cursos/id/{curso_id}", summary="Listar um curso específico pelo ID", )
async def get_curso_id(curso_id: int):
    for curso in cursos:
        if curso.id ==  curso_id:
            jsonRetorno = jsonable_encoder(curso)
            return JSONResponse(content=jsonRetorno, status_code=200)
    raise HTTPException(status_code=404, detail="Curso não encontrado")

@app.put("/cursos/alterar/{curso_id}", summary="Alterar um curso específico pelo ID")
async def put_curso(curso_id: int, updated_curso = Curso):
    if curso_id < 0 or curso_id >= len(cursos):
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    cursos[curso_id] = updated_curso
    dicRetorno = {"message": "Curso inserido com sucesso!", "curso": cursos[curso_id]}

    jsonRetorno = jsonable_encoder(dicRetorno)
    return JSONResponse(content=jsonRetorno, status_code=200)

@app.delete("/cursos/apagar/{curso_id}", summary="Apagar um curso específico pelo ID")
async def delete_curso(curso_id: int):
    if curso_id < 0 or curso_id >= len(cursos):
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    cursos.pop(curso_id)
    dicRetorno = {"message": "Curso inserido com sucesso!"}

    jsonRetorno = jsonable_encoder(dicRetorno)
    return JSONResponse(content=jsonRetorno, status_code=201)