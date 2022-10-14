from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class User(BaseModel):
	name: str
	age: int
	gender: str | None = None
	
	def insert(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender


users = []


@app.get("/")
async def root():
	return {"message": "Hello World"}


@app.get("/users")
async def get_users():
	return users


@app.post("/insert")
async def insert_data(name: str, age: int, gender: str | None = None):
	data = {"name": name, "age": age, "gender": gender}
	return users.append(data)
