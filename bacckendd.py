from fastapi import FastAPI, fastapi, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel, Field
from datetime import date

from database import get_connection

#Create a fastapi application

app = FastAPI(title="Personal Expense Traker API")

#Allow the frontend to communicate with the backend.
#This is conveninent for local development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#Define the information required for a new expense.
class Expense(BaseModel):
    item: str = Field(min_length=1, max_length=100)
    amount: float = Field(gt=0)
    category: str = Field(min_length=1, max_length=50)
    date: date



    #Home API
    @app.get("/")
    def home():
        return {"message": "Welcome to the Personal Expense Tracker API!"}

    #Add a new expense
    @app.post("/expenses")
    def add_expense(expense: Expense):
        connection = get_connection()
        cursor = connection.execute(
            "INSERT INTO expenses (item, amount, category, date) VALUES (?, ?, ?, ?)",
            (expense.item, 
             expense.amount,
               expense.category,
                 expense.date.isoformat())
        )
        connection.commit()

        new_id = cursor.lastrowid
        connection.close()

        return{
            "message": "Expense added successfully",
            "expense_id": new_id
        }


#get all expenses    

    @app.get("/expenses")
    def get_expenses():
        connection = get_connection()
        records = connection.execute("SELECT * FROM expenses order by date desc").fetchall()
        connection.close()

        return {dict(record) for record in records}
#Delete an expense by ID

    @app.delete("/expenses/{expense_id}")
    def delete_expense(expense_id: int):
        connection = get_connection()
        cursor = connection.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        connection.commit()
        deleted = cursor.rowcount
        connection.close()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Expense not found")

        return {"message": "Expense deleted successfully"}  


#Calculate total spending

    @app.get("/summary")
    def total_spending():
        connection = get_connection()
        result = connection.execute("SELECT COALESCE(SUM(amount), 0) as total_spending FROM expenses").fetchone()
        connection.close()

        return {"total_spending": result["total_spending"]}
    
    