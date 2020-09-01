import fastapi
import uvicorn
import logging
import datetime

logging.root.setLevel(logging.INFO)

app = fastapi.FastAPI()

request_count = 0


@app.get("/")
async def root():
    global request_count
    request_count+=1
    logging.info("(%d) Request at %s", request_count, datetime.datetime.now())
    return 'Hello'


if __name__ == '__main__':
    uvicorn.run(app, port=8080)

