
""" الفكرة هنا 
بالانتقال لرابط جديد (Refresh) منع تكرار إرسال البيانات عند عمل تحديث

"JSON"الحل الاول: القراءة من ملف الـ 
يمكننا جعل صفحة النتيجة تفتح الملف وتأخذ آخر نتيجة تم حفظها

"Session"الحل الثاني استخدام الـ 
"session" وضع النتيجة في "خزنة مؤقتة" تسمى الـ 
الرابط يظل نظيفاً والبيانات مخفية ومهما كان طولها
"""


# Session: للأمان وجمال الروابط redirect نستخدمها مع   
# url_for: نستخدمها لتبحث هي عن اسم "الدالة" وتعطينا رابطها الصحيح
# session: ذاكرة مؤقتة للبيانات تجعلها متاحة للتنقل بين الصفحات دون كشفها في المتصفح
from flask import Flask , render_template, request, redirect, url_for, session
import json  # JSON المترجم" الذي يفهم لغة" 

# ليعرف بايثون أن هذا هو التطبيق الرئيسي
app= Flask(__name__)

# (الخزنة) sessionضروري جداً لتشفير البيانات داخل الـ 
app.secret_key = "my_secret_key_123"  # مفتاح الأمان


## (Dynamic URL Building) بناء الروابط ديناميكياً 
# ثم توجه المستخدم لصفحة النتائج total_score تأخذ مدخلات من المستخدم، تحسب
@app.route("/submit", methods=['GET','POST'])
def submit():

    # Post/Redirect/Get pattern لسبب واحد يسمى POST بعد redirect كمبرمجين نستخدم  
    # بالانتقال لرابط جديد (Refresh) وظيفته منع تكرار إرسال البيانات عند عمل تحديث
    if request.method=='POST':

        # سحب الدرجات وتحويلها لأرقام عشرية
        science= float(request.form['science'])
        maths= float(request.form['maths'])
        c= float(request.form['c'])
        data_science= float(request.form['datascience'])

        total_score= (science + maths + data_science + c) / 4
# ---
        # تجهيز البيانات للحفظ (قاموس بايثون)
        data_to_save = {
            "science": science,
            "maths": maths,
            "c": c,
            "data_science": data_science,
            "average": total_score
        }
        
        # sample.json حفظ البيانات في ملف 
        try:
            # نفتح الملف للقراءة أولاً لجلب البيانات القديمة 
            with open('sample.json', 'r') as f:
                # قرأنا ما هو موجود حالياً في الملف 
                content = json.load(f)

        # إذا الملف غير موجود نبدأ بقائمة فارغة
        except (FileNotFoundError, json.JSONDecodeError):
            content = []

        # إضافة النتيجة الجديدة للقائمة
        content.append(data_to_save)

        # الحفظ في الملف
        with open('sample.json', 'w') as f:
            # indent تجعل الملف منسقاً وسهل القراءة
            json.dump(content, f, indent=4)
# ===        
        # (Session) وضع النتيجة في الخزنة
        # هنا نخفي البيانات عن الرابط ونحفظها في ذاكرة السيرفر مؤقتاً
        session['res_status'] = "Success" if total_score >= 50 else "Fail"
        session['res_score'] = total_score

        """ أفضل في حالة حفظ البيانات Redirectلماذا الـ  
        بعد إرسال الدرجات (Refresh) لو المستخدم ضغط على زر تحديث الصفحة 
        المتصفح سيرسل البيانات مرة أخرى و يحفظ نفس الدرجات مرتين render_template بـ 
        (/display) المتصفح سينتقل لصفحة جديدة مع النتيجة مثلاredirect لو استخدمت 
        إذا ضغط تحديث، سيعيد تحميل صفحة النتيجة فقط ولن يرسل و يحفظ البيانات مرة أخرى
        """
        """ url_for هذا هو "البناء الديناميكي" للرابط بستخدام
        'show_final' فلاسك سيبحث عن الدالة التي اسمها
        فحتى اذا غيرنا الرابط /display يجد أن رابطها
        مثلا /find سيجد أن رابطها الجديد أصبح 
        ويقوم بتحديث الروابط تلقائياً في الموقع """
        return redirect(url_for("show_final")) # show_final التوجه لصفحة النتيجة من خلال الدالة

        # يعيد الارسال (Refresh) راح يضل في نفس الرابط و لما نعمل redirect هذا بدون استخدام
        res = session.get('res_status')
        score = session.get('res_score')
        return render_template("result.html", results=res, score=score )

    return render_template('getresult.html')



# "result.html" هذا الرابط يرسل البيانات و يعرض صفحة
@app.route("/display")
def show_final():
    # فتح الخزنة وعرض البيانات
    res = session.get('res_status')
    score = session.get('res_score')

    return render_template("result.html", results=res, score=score )


if __name__ == "__main__":
    app.run(debug=True)


