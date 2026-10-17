"""
发表评论前 先登录，再验证验证码
"""


def check_login(fn_name):
    def fn_inner():
        print("请先登录")
        fn_name()
    return fn_inner

def check_code(fn_name):
    def fn_inner():
        print("验证验证码中~")
        fn_name()
    return fn_inner



def comment():
    print("请发表评论~")

comment_in = check_code(comment)
comment_out = check_login(comment_in)

comment_in()
print()
comment_out()