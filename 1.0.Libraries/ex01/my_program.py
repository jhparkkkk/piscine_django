from local_lib import path

if __name__ == "__main__":
    d = path.Path('./test')
    path.Path.mkdir(d)
    path.Path.write_text(d / 'test.txt', 'Hello, World!!!!')
