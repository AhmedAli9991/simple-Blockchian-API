from pydantic import BaseModel
class block(BaseModel):
    index: int
    timestamp: str
    data: str
    proof: str
    previous_hash: str