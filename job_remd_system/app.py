from flask import *
import pickle

app = Flask(__name__)
@app.route("/" ,methods=["GET","POST"])
def home():
      if request.method=="POST":
          f = open("JOB.model", "rb")
          model = pickle.load(f)
          f.close()  
 
          exp = float(request.form["num"])
          sal = float(request.form["sal"])
          if sal <=199999:
            return render_template("home.html", m="salary expectation must be minimum 200000 ")
          else:
            edu = request.form["edu"]
            if edu == "BE":
              d = [[exp,sal,1,0,0]]
            elif edu == "ME":
              d = [[exp,sal,0,1,0]]
            else :
              d = [[exp,sal,0,0,1]]

          job = model.predict(d)  
          if job =="No suitable job":
            return render_template("home.html", m=job[0])
          else:
            return render_template("home.html", m="Suitable job for you is " +job[0])
      else:
          return render_template("home.html")
if __name__ == "__main__":
  app.run(debug =True, use_reloader=True)