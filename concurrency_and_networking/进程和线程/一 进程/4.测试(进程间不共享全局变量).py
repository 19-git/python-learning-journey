import multiprocessing

my_list = [1,2,3]

def fun_one():
    my_list.append(4)
    print(my_list)

def fun_two():
    my_list.append(5)
    print(my_list)

p1 = multiprocessing.Process(target=fun_one)
p2 = multiprocessing.Process(target=fun_two)

if __name__ == "__main__":
    p1.start()
    p2.start()