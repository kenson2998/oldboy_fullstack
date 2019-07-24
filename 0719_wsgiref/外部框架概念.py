'''

外部服務器 : 用於解析HTTP協議
Apache 、 Nginx

外部應用: 用於和外部服務器溝通

外部框架
Django Flask


外部服務網關接口:
WSGI
外部框架和外部服務器溝通是透過WSGI(Web Server Gateway Interface)

MVC架構與MTV架構

Model 模型:
負責業務對象與數據庫對象(ORM)

Control 控制:
接收客戶輸入調用模型和視圖完成用戶的請求

Template 模板:
負責如何把頁面展示給用戶

View 視圖:
負責用戶的交互(頁面)


Django 可以叫MTV也可以叫MVC
你跟Java、PHP的說 MTV他們不懂



views.py 中的 return render() 其實也是回傳HttpResponse
render() <~ 叫做渲染

setting.py
STATIC_URL = '/statics/'  # 別名
這個別名用來統一HTML文件上的 statics 路徑 都會依別名在前端呈現
本地目錄可能是別的目錄名 假如是abc
STATIC_URL = '/statics/'  # 別名

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"abc"),
)

HTML裡面依舊是static不用再去HTML修改路徑
 <script src="/static/xxx.js"></script>
 一樣還是 <script src="/static/xxx.js"></script>
 但本地會去abc/xxx.js



 HTML 前面加上
 {% load staticfiles %}
 後面的static可以這樣改
 <script src="/static/xxx.js"></script>
 <script src="{% static 'jquery-3.4.1.min.js' %}"></script>


'''