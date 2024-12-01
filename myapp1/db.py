from pymongo import MongoClient

client = MongoClient("mongodb+srv://crud_user:Password123@cluster0.ahswj.mongodb.net/?retryWrites=true&w="
                     "majority&appName=Cluster0")
db = client["Employees"]