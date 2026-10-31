from flask import Flask

app = Flask(__name__)

# 根路径 / ：首页
@app.route('/')
def home():
    return "欢迎来到我的学习之旅"

# 关键区别在下面这个路由：
# /user/<name> 里的 <name> 是"网址参数"（尖括号是 Flask 的固定写法）
# 访问 /user/张三 时，name 自动变成"张三"；访问 /user/李四 时，name 变成"李四"
# 注意：路由里的 <name> 和函数参数 name 必须同名，Flask 才能对上号
@app.route("/user/<name>")
def user(name):
    # f"..." 是格式化字符串：{} 里的 name 会被替换成网址里传进来的值
    # 同一个函数，因为网址不同，返回的内容也不同
    return f"你好,{name}！这是你的专属界面。"

app.run()