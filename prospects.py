from pydantic import BaseModel
from typing import Optional

# CODIGO DA VAGA
# NOME
# COMENTARIO
# SITUACAO DO CANDIDATO
# TEM QUE VIR TODAS AS PROPECCOES

class prospects(BaseModel):
    codigo_vaga: str  # Código do candidato (ou currículo)
    titulo: str
    #modalidade: str
    nome: str         # nome do candidato
    comentario: str
    situacao_candidato: str
    data_candidatura: str
    recrutador: str
    #opinion: Optional[str] = None  # Opinião gerada pela IA
    #file: str  # Nome ou caminho do arquivo analisado