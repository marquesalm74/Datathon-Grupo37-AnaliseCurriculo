from dataclasses import dataclass

@dataclass
class Analysis:
    id: str
    codigo_vaga: str
    content: str
    file: str
    opnion: str
    score: float
