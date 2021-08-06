from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI() 

class Resp(BaseModel):
    valor1: int
    valor2: int
    operador: str
    
    def operation(self):
        if self.operador == '+':
            result = self.valor1 + self.valor2
            return {
                'resultado': result
            }
        elif self.operador == '-':
            result = self.valor1 - self.valor2
            return {
                'resultado': result
            }
        elif self.operador == '*':
            result = self.valor1 * self.valor2
            return {
                'resultado': result
            }
        elif self.operador == '/':
            result = self.valor1 / self.valor2 
            return {
               "resultado": result
            }



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/operador/")
async def operacao(resp: Resp):
    return resp.operation()
    
