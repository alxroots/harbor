from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/telnyx/sms")
async def receive_sms(request: Request):
    body = await request.json()
    print("SMS recebido:", body)
    return {"status": "ok"}