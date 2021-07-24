# 相对引入
from my_package import module_A as A

if __name__ == "__main__":
    A.test_fuc()
    print(__name__)

