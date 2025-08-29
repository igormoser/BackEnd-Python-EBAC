from fastapi import FastAPI,HTTPException
app = FastAPI()

lista_livros = {"id": 1, "nome_livro": "Harry Potter e a Pedra Filosofal", "autor_livro": "J.K.Rowling", "ano_livro": 1997}

@app.get("/livros")
def get_livros():
    if not lista_livros:
        return {"Este livro não existe na lista!"}
    else:
        return {"Livros": lista_livros}
@app.get("/adicionar")
def post_livros(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: str):
    if id_livro in lista_livros:
        raise HTTPException(status_code=400, detail="Este livro já existe na lista!")
    else:
        lista_livros[id_livro] = {"nome_livro": nome_livro, "autor_livro": autor_livro, "ano_livro": ano_livro}
        return {"message": "O livro foi adicionado com sucesso!"}

@app.put("/atualizar/{id_livro}")
def put_livros(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: str):
    meu_livro = lista_livros.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail="Este livro não foi encontrado!")
    else:
        {"nome_livro": "Harry Potter e a Câmara Secreta", "autor_livro": "J.K.Rowling", "ano_livro": 1998}
        if nome_livro:
            lista_livros["nome_livro"] = nome_livro
        if autor_livro:
            lista_livros["autor_livro"] = autor_livro
        if ano_livro:
            lista_livros["ano_livro"] = ano_livro
        return {"message": "O livro foi atualizado com sucesso!"}

@app.delete("/deletar/{id_livro}")
def delete_livros(id_livro: int):
    if id_livro not in lista_livros:
        raise HTTPException(status_code=404, detail="Este livro não foi encontrado!")
    else:
        del lista_livros[id_livro]
        return {"message": "O livro foi deletado!"}