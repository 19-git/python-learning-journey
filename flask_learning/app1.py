#导入 Flask(网页服务器工具包) 框架
from flask import Flask

#创建一个 Flask 应用对象 app
#__name__ 表示”以当前这个文件为起点“,Flask 靠它找到项目位置
app = Flask(__name__)

# @app.route("/") 的意思是：浏览器访问网址的根路径（首页，即 http://127.0.0.1:5000/）时，
# 就自动调用下面紧挨着的这个函数
@app.route('/')
def home():
    # return 的字符串会原样显示在浏览器页面上
    return "你好，这是我在 Flask 上的第一个网页！"

# 启动服务器：程序运行到这一行后不会结束，而是"一直监听"
app.run()