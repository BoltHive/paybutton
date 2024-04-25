from pydantic import BaseModel


class Paybutton(BaseModel):
    id: str
    wallet: str
