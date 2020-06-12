import logging.handlers
import os
import time

BASE_ARITCAL_TITLE = "我的面试_{}".format(time.strftime("%d%H%M%S"))
BASE_PATH = os.path.dirname(os.path.abspath("__file__"))


# 日志配置的基础函数
def base_loger_config():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 创建处理器
    ls = logging.StreamHandler()
    lht = logging.handlers.TimedRotatingFileHandler(filename=BASE_PATH + "/log/test_log", when="midnight", interval=1,
                                                    backupCount=2)
    # 创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 将格式化器绑定到处理器
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(ls)
    logger.addHandler(lht)
