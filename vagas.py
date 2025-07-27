from pydantic import BaseModel

# SAP
# CLIENTE SOLICITANTE / CLIENTE
# NIVEL PROFISSIONAL
# IDIOMAS
# PRINCIPAIS ATIVIDADES
# COMPETENCIAS TECNICAS

class vagas(BaseModel):
    codigo_vaga: str
    titulo_vaga: str
    vaga_sap: str
    cliente: str
    solicitante_cliente: str
    areas_atuacao: str
    principais_atividade: str
    competencia_tecnicas_e_comportamentais: str
    nivel_ingles: str
    nivel_espanhol: str
    outro_idioma: str