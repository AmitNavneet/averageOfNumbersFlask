from flask import Flask,render_template
from flask import request


app=Flask(__name__)

numbers=[]

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/addToList')
def addToList():
    num=float(request.args['num'])
    numbers.append(num)
    print(numbers)

    return render_template('index.html')

@app.route("/printAverage")
def printAverage():
    sum=0
    tempList=numbers.copy()
    numbers.clear()
    print(numbers)
    for i in tempList:
        sum=sum+i
    
    if len(tempList)>0:
        average=sum/len(tempList)
        return render_template('printAvg.html',list=tempList,sum=sum,average=average)
    else:
        return render_template('index.html')
        

if __name__=='__main__':
    app.run(debug=True)