from flask import Flask,render_template,request 

app =Flask(__name__)

@app.route("/",methods=['GET','POST']) #homepage
def home():
    # name = input("Enter You Name")
    # if request.method =="POST":
    #     names = request.form.get('name')
    # return render_template("Home.html", names = name)  #only one position argument but key word  can be many # data must be in dictionary form
    name = input("Enter You Name")
    return render_template("Home.html", data = {"name":name}) 

@app.route("/about",methods=['GET','POST']) #aboutpage
def about():
    if request.method=="POST":
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        results  = num1+num2
                #reciving data
    return render_template("About.html",result=results)



if __name__ == "__main__":
    app.run(debug=True)
    