import fastapi
import uvicorn
import logging
import datetime

logging.root.setLevel(logging.INFO)

app = fastapi.FastAPI()


@app.get("/api/cats")
async def root():
    return [
        {
            "name": f"Pussy cat {i}",
            "image": f"/public/cat{i}.jpg",
        } for i in range(1, 4)
    ]


if __name__ == '__main__':
    uvicorn.run(app, port=8900)

