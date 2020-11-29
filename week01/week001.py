import logging
from pathlib import Path
import os
import time


def week001_getlog():
    time_now = time.strftime("%Y-%m-%d" ,time.localtime())
    p = Path()
    path = str(p.resolve())+ f"/var/log/week001_getlog_{time_now}/"

    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)
    logging.basicConfig(filename='loginfo.log',
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(funcName)s running at %(asctime)s',
                        )
    logging.debug('')


if __name__ == '__main__':
    week001_getlog()