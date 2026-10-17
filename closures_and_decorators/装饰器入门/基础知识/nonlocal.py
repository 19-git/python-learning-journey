def fun_out():
    a = 100
    def fun_inn():
        nonlocal a
        a += 1
        print(f"a={a}")
    return fun_inn

fi = fun_out()
fi()
fi()
fi()
