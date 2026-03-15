

""" (JSON ملف) إضافة الذاكرة 
sample.json ربطنا بملف 
الهدف: حفظ كل الدرجات التي يدخلها المستخدم للأبد. حتى لو أغلقت السيرفر

بعد إرسال الدرجات (Refresh) المشكلة لو المستخدم ضغط زر تحديث الصفحة 
المتصفح يرسل البيانات مرة أخرى فتحفظ نفس الدرجات مرتين render_template لما نستخدم
"""

# redirect: نستخدمها لنقل المستخدم من صفحة الإرسال إلى صفحة عرض النتيجة
from flask import Flask , render_template, request

# لا تدعم التعليقات JSON ملاحظة ملفات
# "JSON": طريقة لتنظيم البيانات على شكل قاموس بايثون تماماً JavaScript Objectاختصار لـ
import json  # JSON المترجم" الذي يفهم لغة" 

# ليعرف بايثون أن هذا هو التطبيق الرئيسي
app= Flask(__name__)

# ===
# (الخزنة) sessionضروري جداً لتشفير البيانات داخل الـ 
app.secret_key = "my_secret_key_123"  # مفتاح الأمان


## (Dynamic URL Building) بناء الروابط ديناميكياً 
# ثم توجه المستخدم لصفحة النتائج total_score تأخذ مدخلات من المستخدم، تحسب
@app.route("/submit", methods=['GET','POST'])
def submit():
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
            # نفتح الملف للقراءة أولاً لجلب البيانات القديمة (إذا أردت  )
            with open(r'C:\Users\Lenovo\Desktop\Ai hasan\one\python\Big_Data\NET\Flask\3_flask\templates\sample.json', 'r') as f:
                # قرأنا ما هو موجود حالياً في الملف (عشان ما نمسحه)
                content = json.load(f)  
        
        # إذا الملف غير موجود أو فارغ
        except (FileNotFoundError, json.JSONDecodeError):
            content = []  # نبدأ بقائمة فارغة

        # إضافة النتيجة الجديدة للقائمة
        content.append(data_to_save)

        # الحفظ في الملف
        with open(r'C:\Users\Lenovo\Desktop\Ai hasan\one\python\Big_Data\NET\Flask\3_flask\templates\sample.json', 'w') as f:
            # indent تجعل الملف منسقاً وسهل القراءة
            json.dump(content, f, indent=4)

        res = "Success" if total_score >= 50 else "Fail"

        # التوجه لصفحة النتيجة
        return render_template('result.html', results=res, score=total_score)
    
    return render_template('getresult.html')


if __name__ == "__main__":
    app.run(debug=True)


