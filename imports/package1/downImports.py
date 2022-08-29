from utils.helper import helperFun
from utils.subutils.subhelper import subHelperFun


##### when running from the level of main.py
# from package1.utils.helper import helperFun
# from package1.utils.subutils.subhelper import subHelperFun




if __name__ == "__main__":
    ret = helperFun()
    print("Returned Value from helper function", ret)

    ret = subHelperFun()
    print("Returned Value from sub-helper function", ret)