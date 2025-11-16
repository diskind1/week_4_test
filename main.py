from fastapi import FastAPI

app = FastAPI()

if __name__ == "main":
    @app.get("/test/")
    def say_hello():
        return {"msg": "hi from test"} 

    @app.get("/test/{name}")
    def names(name: str):
        with open("names.txt", "a") as f:
            f.write(name)
        return {"msg": "saved user"}





    @app.post("/Caesar")
    def Caesar_chiper(data:dict):
        print(data)
        return data
    