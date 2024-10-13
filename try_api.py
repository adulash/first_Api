from fastapi import FastAPI, Query
from pydantic import BaseModel        #لأجل تحديد نموذج المدخلات والمخرجات
from fastapi.middleware.cors import CORSMiddleware #لأجل السماح بتشغيل اي بي اي على اي منصة 




app = FastAPI()

#اعداد السماح بتشغيل اي بي اي على اي منصة اسمها ميدلوير
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"], allow_methods=["*"],allow_headers=["*"],)


class BMIoutput(BaseModel):   #تحديد نموذج المخرجات
    bmi: float
    message: str


@app.get("/")

def hi():
    return {"message": "Marhaban Alf with FastApi"}

@app.get("/calculate_bmi")      #=> دالة كيوري  للتحقق التلقائي > ... تعني اجباري والباقي أعلى من وأقل من والوصف
def calculate_bmi(weight: float=Query(..., gt=20,lt=200, description="الوزن بالكيلوجرام"),
                   height:float=Query(..., gt=1.00,lt=2.00,description="الطول بالمتر")):
    bmi = weight / (height**2)
    if bmi < 18.5:
        message = "لديك نقص في الوزن كل أكثر"
    elif 18.5 <= bmi <25:
        message = "لديك وزن طبيعي، حافظ عليه"
    elif 25 <= bmi <30:
        message = "لديك زيادة في الوزن تمرن أكثر"
    else:
        message = "أنت تعاني من السمنة ، استشر  طبيبك"
    return BMIoutput(bmi=bmi,message=message) #تحسين  نموذج المخرجات
    #return {"bmi": f"{bmi:.2f}", "message": message} نموذج سابق



#uvicorn try_api:app --reload
#http://127.0.0.1:8000/calculate_bmi?weight=76&height=1.67
#http://127.0.0.1:8000/docs التوثيق التلقائي
