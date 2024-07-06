
from fastapi import APIRouter, FastAPI
import uvicorn

from api import router as my_router

app = FastAPI()



# Include routers
app.include_router(my_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



