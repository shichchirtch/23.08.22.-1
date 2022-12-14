class FileAcceptor:

    def __init__(self, *args):
            self.arr = args
    def __add__(self, other):
        return FileAcceptor(self.arr+other.arr)

    def __call__(self, *args, **kwargs):
        return all(arg.endswith(*self.arr) for arg in args)





filenames = ["boat.jpg",  "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png",
             "eq_2.xls"]
# new_arr = []
# for t in filenames:
#     i = t.split(".")[-1]
#     new_arr.append(i)
# # print(new_arr)
# filenames = new_arr
# filenames = [ "khi","txt", "doc", "khi" ] "akaaekjg.khi"
acceptor1 = FileAcceptor("jpg", "jpeg", "png")
# print(acceptor1.arr)
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2  # ("jpg", "jpeg", "png", "bmp")
# print(acceptor12.arr)

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
d = acceptor_images + acceptor_docs
print("d= ",d.arr)
f = list(filter(acceptor_images + acceptor_docs, filenames))
print(f)
