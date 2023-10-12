from fastapi import FastAPI, APIRouter
import uvicorn


from auth.register import register_router
from auth.login import login_router

app = FastAPI(
    title="Auth"
)

main_api_router = APIRouter()
main_api_router.include_router(register_router, prefix='/register')
main_api_router.include_router(login_router, prefix='/login')

app.include_router(main_api_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

