
""" البداية البسيطة (النتائج الثابتة)
/success/80 أنشأنا روابط بسيطة مثل 
(URL Variable) الهدف نريد فقط أن نرى كيف يقرأ بايثون "الرقم" من الرابط 
"المشكلة لا نريد من المستخدم أن يكتب البيانات في "الرابط """

from flask import Flask , render_template, request
import json  # JSON المترجم" الذي يفهم لغة" 

# ليعرف بايثون أن هذا هو التطبيق الرئيسي
app= Flask(__name__)


""" ## Variable Rule
واستخدامه كمتغير (URL) هي القدرة على أخذ جزء من الرابط 
@app.route("/success/<score>") داخل الدالة، مثل 
بتكون شرطة الي يكتبه المستخدم بعدها نقدر ناخذه  /success يعني بعد الرابط الاساسي
الأقواس < > تخبر فلاسك: أي شيء يُكتب هنا، اصطاده """
@app.route("/success/<score>")  # افتراضياً (string) تعتبر نص <score> هنا 
def success(score):
    return "The marks you got is"+ score

@app.route("/succ/<int:score>") # "int" الحين يستقبل 
def succ(score):
    return "The marks you got is "+ str(score)  # "str" لازم هنا عاد نغيرها الى 

# (إرسال النتائج) HTML ربط بايثون بملف 
@app.route("/sucs/<int:score>")
def sucs(score):
    res = "Pass" if score >= 50 else "Failed"

    # result.html هنا نرسل النتائج لملف 
    # HTML هو اسم المتغير الذي سيستخدمه جينجا داخل results الـ
    return render_template("result.html", results=res, score=score)


if __name__ == "__main__":
    app.run(debug=True)


