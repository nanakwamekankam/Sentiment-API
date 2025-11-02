from pydantic import BaseModel, Field, constr

class PredictIn(BaseModel):
    text: constr(strip_whitespace=True, min_length=1) = Field(...) # type: ignore

class PredictOut(BaseModel):
    label: str
    score: float
