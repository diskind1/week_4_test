from fastapi import FastAPI

app = FastAPI()

if __name__ == "main":
    @app.get("/")
    def get_message():
        response =  {"msg": "hi from test"} 
        return response

    @app.post("/casar")
    def casar_chiper(data:dict):
        print(data)
        return data
    