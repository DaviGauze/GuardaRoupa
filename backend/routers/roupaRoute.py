from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.banco import get_db
from backend.models.roupaModel import Roupa
from backend.schemas.roupaSchema import RoupaCreate, RoupaResponse


@app.get("/roupa/{id_roupa}")
def read_roupa(id_roupa: int):
    return{"id_roupa": id_roupa}

@router.post("/", response_model=RoupaResponse)
def create_roupa(roupa: RoupaCreate, db: Session = Depends(get_db)):

    nova_roupa = Roupa(
        id_usuario=roupa.id_usuario,
        nome=roupa.nome,
        tipo_peca=roupa.tipo_peca_id,
        categoria=roupa.categoria_id,
        cor=roupa.cor,
        estacao=roupa.estacao_id,
        caminho_imagem=roupa.imagem_id
    )

    db.add(nova_roupa)
    db.commit()
    db.refresh(nova_roupa)

    return nova_roupa

@app.delete("/roupa/{id_roupa}")
def delete_roupa(id_roupa: int):
    return "roupa deletada"