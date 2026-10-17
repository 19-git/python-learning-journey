"""
案例：基于传入的数值(每批次的条数),创建 生成器.生成批次歌词
"""
import math

#1.定义函数,接受每批次的歌词条数.返回生成器
def dataset_loader(batch_size):
    # 1.1读取文件数据
    with open('./data/jaychou_lyrics.txt','r',encoding='utf-8')as src_f:

        #1.2一次读取所有行
        lines = src_f.readlines()

        #1.3计算批次总数
        total_batch = math.ceil(len(lines)/batch_size)

        #1.4 for循环方式，获取到每批次的数据，放到生成器中，并返回
        for idx in range(total_batch):
            yield lines[idx*batch_size:idx*batch_size+batch_size]


#2.测试
dl = dataset_loader(100)
print(next(dl)) #第一批
print(next(dl)) #第二批

for batch_data in dl:
    print(batch_data)
































