# coding: utf-8

from pathlib import Path
import conf.deploy as deploy_conf



class Package(object):

    def __init__(self):
        self.DIR_SRC = Path(deploy_conf.DIR_SRC)


class JARPackage(Package):
    pass

class WARPackage(Package):
    pass

class AWARPackage(Package):
    pass