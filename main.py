from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class Input(BaseModel):
    data: list[str]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/bfhl", status_code=status.HTTP_200_OK)
def get_req():
    return {"operation_code": 1}


@app.post("/bfhl")
def post_req(input: Input):
    data = input.data
    resp = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
    }

    alpha = []
    num = []
    low_alpha = []
    for i in data:
        if i.isalpha():
            alpha.append(i)
            if i.islower():
                low_alpha.append(i)
        elif i.isdigit():
            num.append(i)

    resp["numbers"] = num
    resp["alphabets"] = alpha
    resp["highest_lowercase_alphabet"] = max(low_alpha)
    return resp
