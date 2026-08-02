from pydantic import BaseModel, Field


class ChurnRequest(BaseModel):
    age: int = Field(..., ge=18, le=100, description="Customer age")
    tenure: int = Field(..., ge=0, le=50, description="Years with the bank")
    balance: float = Field(..., ge=0, description="Account balance")
    num_products: int = Field(..., ge=1, le=10, description="Number of bank products held")
    is_active: int = Field(..., ge=0, le=1, description="1 if active member, else 0")


class ChurnResponse(BaseModel):
    churn_probability: float
    churn_prediction: int