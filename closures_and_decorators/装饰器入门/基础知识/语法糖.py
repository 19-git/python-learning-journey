def check_logic(fn_name):
    def fn_inner():
        print("校验登录...登陆成功~")
        fn_name()
    return fn_inner

@check_logic
def comment():
    print("发表评论~")


if __name__ == "__main__":
    comment()