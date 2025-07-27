from pydantic import BaseModel

# NIVEL ACADEMICO
# INGLES
# ESPANHOL
# CONHECIMENTOS TECNICOS
# AREA DE ATUACAO
# CV COMPLETO
# CHAVEADO PELO CODIGO DO CANDIDATO

class Applicants(BaseModel):
    id: str
    job_id: str