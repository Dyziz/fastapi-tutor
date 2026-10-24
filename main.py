from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025"
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development.",
        "date_posted": "April 21, 2025"
    }
]


@app.get("/", response_class=HTMLResponse)
def read_root():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get("/api/posts")
def read_posts():
    return posts