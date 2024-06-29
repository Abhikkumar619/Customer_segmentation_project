from flask import Flask,request, render_template
from src.Customer_segementation.pipeline.predication_pipe import CustomData,PrediPipeline
from src.Customer_segementation.logger import logger
app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template("form.html")


@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method=="GET": 
        return render_template("form.html")
    else: 
        data=CustomData(
            Gender=request.form.get("Gender"),
            Ever_Married=request.form.get("Ever_Married"),
            Age=int(request.form.get("Age")),
            Graduated=request.form.get("Graduated"),
            Profession=request.form.get("Profession"),
            Work_Experience=int(request.form.get("Work_Experience")),
            Spending_Score=request.form.get("Spending_Score"),
            Family_Size=int(request.form.get("Family_Size"))
        )

        spending_scor=data.Spending_Score
        family_length=data.Family_Size
        designation=data.Profession

        logger.info(f"Spending score: {spending_scor}, family_size is {family_length}, designation: {designation}")
    
        final_Data=data.get_data_as_dataframe()
        logger.info(f"Data from form\n: {final_Data}")

        predict_obj=PrediPipeline()
        final_pred=predict_obj.predict(user_dataframe=final_Data)
        logger.info(f"Prediction of model: {final_pred[0]}")
        category=final_pred[0]


        if category== 0:
            result="A"
            return render_template("result.html",final_result=f"{result}, having spending score :{spending_scor}, Family_size: {family_length} and degination: {designation}")
        elif category == 1: 
            result="D"    
            return render_template("result.html",final_result=f"{result}, having spending score :{spending_scor}, Family_size: {family_length} and degination: {designation}")
        elif category==2: 
            result="B"
            return render_template("result.html",final_result=f"{result}, having spending score :{spending_scor}, Family_size: {family_length} and degination: {designation}")
        else:
            result="C"
            return render_template("result.html",final_result=f"{result}, having spending score :{spending_scor}, Family_size: {family_length} and degination: {designation}")   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)