# الهدف عمل زر في الموقع لارسال البيانات

from flask import Flask , render_template, request
import json  # JSON المترجم" الذي يفهم لغة" 

# ليعرف بايثون أن هذا هو التطبيق الرئيسي
app= Flask(__name__)


# الصفحة الرئيسية
@app.route("/")
def index():
    return render_template('index.html')

# عرض صفهة فيها معلومات 
@app.route("/about")
def about():
    return render_template('about.html')

# submit عند ضغط زر
@app.route("/submit", methods=['GET','POST'])
def submit():

    # GET: تعني "يا سيرفر، أعطني الصفحة فقط لأراها
    # POST: تعني "يا سيرفر، خذ هذه البيانات التي كتبتها
    if request.method=='POST':  # وظيفته معرفة نوع "الطلب" القادم من المتصفح

        name= request.form['name']
        return f"Hello {name}!"     # هل كذا ترجع النتائج في الرابط؛ تأكد
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)
