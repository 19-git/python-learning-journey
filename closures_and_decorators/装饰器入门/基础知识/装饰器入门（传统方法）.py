"""
发表评论前需要登录
"""

def check_logic(comment):
    def fn_inner():
        print("校验登录...登陆成功~")
        comment()
    return fn_inner

def comment():
    print("发表评论~")


if __name__ == "__main__":
    comment = check_logic(comment)
    comment()




