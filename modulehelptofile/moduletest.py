
import time
import os
from varinfo import *


def help_to_file(topic):
    out = open(f'_{topic}','w')
    out.write(str(help(topic)))
    out.close()

help_to_file('time.time')