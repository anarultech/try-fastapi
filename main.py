from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
async def home_page():
    root_url = 'http://localhost:8000'
    api_endpoint = {
        'home': f'{root_url}/',
        'posts': f'{root_url}/posts/'
    }
    return {
        'home': f'{root_url}/',
        'posts': f'{root_url}/posts/'
    }


if __name__ == '__main__':
    uvicorn.run(app=app, host='localhost', port=8080)