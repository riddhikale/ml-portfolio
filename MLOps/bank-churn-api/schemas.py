from pydantic import BaseModel, Field
from typing import Literal
 
 
class ChurnRequest(BaseModel):
    credit_score: int = Field(..., ge=300, le=900, description="Credit score")
    age: int = Field(..., ge=18, le=100)
    tenure: int = Field(..., ge=0, le=15, description="Years with the bank")
    balance: float = Field(..., ge=0)
    num_of_products: int = Field(..., ge=1, le=4)
    has_cr_card: int = Field(..., ge=0, le=1, description="1 if has credit card, else 0")
    is_active_member: int = Field(..., ge=0, le=1)
    estimated_salary: float = Field(..., ge=0)
    geography: Literal["France", "Germany", "Spain"]
    gender: Literal["Male", "Female"]