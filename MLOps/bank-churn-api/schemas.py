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

    def to_model_input(self) -> dict:
        """Converts the human-friendly request into the one-hot encoded columns
        the trained model actually expects, matching pd.get_dummies(..., drop_first=True)
        from the training notebook exactly."""
        return {
            "CreditScore": self.credit_score,
            "Age": self.age,
            "Tenure": self.tenure,
            "Balance": self.balance,
            "NumOfProducts": self.num_of_products,
            "HasCrCard": self.has_cr_card,
            "IsActiveMember": self.is_active_member,
            "EstimatedSalary": self.estimated_salary,
            "Geography_Germany": 1 if self.geography == "Germany" else 0,
            "Geography_Spain": 1 if self.geography == "Spain" else 0,
            "Gender_Male": 1 if self.gender == "Male" else 0,
        }

    class Config:
        json_schema_extra = {
            "example": {
                "credit_score": 650,
                "age": 58,
                "tenure": 3,
                "balance": 120000,
                "num_of_products": 1,
                "has_cr_card": 1,
                "is_active_member": 0,
                "estimated_salary": 90000,
                "geography": "Germany",
                "gender": "Female",
            }
        }


class ChurnResponse(BaseModel):
    churn_probability: float
    churn_prediction: int