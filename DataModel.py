from pydantic import BaseModel
from typing import Optional


class DataModel(BaseModel):
    Grupo: int
    Sexo: int
    Edad: int
    Modo_Llegada: int
    Lesion: int
    Queja_Principal: Optional[str]
    Estado_Mental: int
    Dolor: int
    dolor_NRS: Optional[str]
    SBP: Optional[float]
    DBP: Optional[float]
    HR: Optional[float]
    RR: Optional[float]
    BT: Optional[float]
    Saturacion: Optional[float]
    KTAS_enfermera: int
    Diagnostico_En_Urgencias: Optional[str]
    Disposicion: int
    KTAS_experto: int
    Grupo_De_Error: int
    Duracion_Estancia_Min: int
    Duracion_KTAS_Min: Optional[str]  
    Error_Triaje: int

    def columns(self):
        return ["Grupo", "Sexo", "Edad", "Modo_Llegada", "Lesion", "Queja_Principal",
                "Estado_Mental", "Dolor", "dolor_NRS", "SBP", "DBP", "HR", "RR", "BT",
                "Saturacion", "KTAS_enfermera", "Diagnostico_En_Urgencias", "Disposicion",
                "KTAS_experto", "Grupo_De_Error", "Duracion_Estancia_Min", "Duracion_KTAS_Min",
                "Error_Triaje"]
