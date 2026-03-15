


""" (إدخال البيانات) Formsاستخدام الـ 
ليعبئ المستخدم درجاته في مربعات getresult.html أنشأنا ملف 
لسحب البيانات من المربعات بدلاً من الرابط request.form استخدمنا 
المشكلة التي ظهرت: البيانات كانت تظهر وتختفي بمجرد إغلاق الصفحة. لا يوجد "ذاكرة" للموقع

"""

# request: هي المسؤولة عن قراءة ما كتبه المستخدم داخل المربعات
from flask import Flask , render_template, request
import json  # JSON المترجم" الذي يفهم لغة" 

# ليعرف بايثون أن هذا هو التطبيق الرئيسي
app= Flask(__name__)


## (Dynamic URL Building) بناء الروابط ديناميكياً 
# ثم توجه المستخدم لصفحة النتائج total_score تأخذ مدخلات من المستخدم، تحسب
@app.route("/submit", methods=['GET','POST'])
def submit():
    if request.method=='POST':

        # سحب الدرجات المربعات وتحويلها لأرقام عشرية
        science= float(request.form['science'])
        maths= float(request.form['maths'])
        c= float(request.form['c'])
        data_science= float(request.form['datascience'])

        total_score= (science + maths + data_science + c) / 4
        res = "True" if total_score >= 50 else "False"

        # عرض النتيجة مباشرة (المشكلة هنا: الرابط لا يتغير والبيانات تضيع)
        return render_template('result.html', results=res, score=total_score)


    return render_template('getresult.html')


if __name__ == "__main__":
    app.run(debug=True)



    