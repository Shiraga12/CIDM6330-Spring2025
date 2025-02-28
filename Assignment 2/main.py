from fastapi import FastAPI
import random;

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Welcome to the FastAPI API!"}

@app.get('/api/greet')
async def greet():
    return {"message": "Hello, world!"}

@app.get('/api/greet/{name}')
async def greet_name(name: str):
    return {"message": f"Hello, {name}!"}

@app.get('/api/random_number/{min_value}/{max_value}')
async def random_number(min_value: int, max_value: int):
    return {"random_number": random.randint(min_value, max_value)}

if __name__ == "__main__":
    import uvicorn;

    uvicorn.run(app, host="127.0.0.1", port=8000)