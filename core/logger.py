import logging
import sys

def setup():
    l = logging.getLogger("AEGIS")
    l.setLevel(logging.INFO)
    fmt = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    fh = logging.FileHandler("logs/operation.log")
    fh.setFormatter(fmt)
    l.addHandler(sh)
    l.addHandler(fh)
    return l

log = setup()

