import logging
import datetime

log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H.log")
logging.basicConfig(level=logging.INFO,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename=log_filename)
# 定義 handler 輸出 sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# 設定輸出格式
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# handler 設定輸出格式
console.setFormatter(formatter)
# 加入 hander 到 root logger
logging.getLogger('').addHandler(console)


def records(operation_type,IP,Ccontent,method="info"):
    if method == "info":
        method = logging.info
    elif method == "debug":
        method = logging.debug
    elif method == "warning":
        method = logging.warning
    elif method == "error":
        method = logging.error
    method("{}:{}:{}".format(operation_type,IP,Ccontent))
