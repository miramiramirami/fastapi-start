from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def get_some():
    return {
        'name': 'hello',
        'user': 'world',
    }

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)