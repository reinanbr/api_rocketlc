from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)


@app.get('/ssl') #response_model=List[LaunchInfo], summary="Obter informações de lançamentos", tags=["SSL"])
async def ssl_info(request: Request):
    data_launch = sll.launchs()
    return JSONResponse(data_launch)

