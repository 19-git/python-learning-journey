# request 是 Flask 提供的"请求对象"：用来读取浏览器发过来的数据
from flask import Flask,request

app = Flask(__name__)

# 首页：返回一段 HTML（网页代码）
@app.route("/")
def home():
    # 三引号 '''...''' 包起来的是一整段多行字符串，这里写的是 HTML
    return '''
        <form method="post" action="/hello">
            输入你的名字: <input name="name">
            <button type="submit">提交</button>
        </form>
    '''
    # 逐段解释这段 HTML：
    # <form>...</form>   —— 表单标签，圈出一个"可以填内容的区域"
    #   method="post"    —— 提交方式用 POST（把数据"装进包裹"发给服务器，比 GET 更安全，适合传数据）
    #   action="/hello"  —— 点提交后，数据发往哪个网址（/hello，也就是下面那个函数）
    # <input name="name"> —— 一个输入框；name="name" 是给这个输入框起个名字，
    #                        程序靠这个名字从 request.form["name"] 里取到用户填的内容
    # <button type="submit">提交</button> —— 一个按钮，点它就会触发表单提交

#处理 /hello 这个网址，且只接受 POST 方式的提交
# 如果没写 methods=["POST"]，浏览器用 GET 访问 /hello 会报 405（方法不允许）
@app.route("/hello",methods=["POST"])
def hello():
    # request.form 是"浏览器 POST 过来的所有表单数据的集合"
    # ["name"] 就是按 input 的 name 属性取值——用户在这个框里填了什么，这里就拿到什么
    name = request.form["name"]
    # 拿到数据 → 处理 → 返回结果页面
    return f"你好,{name}！我收到了你提交的内容。"

app.run()