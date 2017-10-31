# coding: utf-8

import os
import flat.settings as settings
from pathlib import Path
from datetime import datetime
import shutil
from svn.remote import RemoteClient
import subprocess
import conf.deploy as deploy_conf
from .package import *



class DeployManager(object):
    """
    manage package deployment
    """
    def __init__(self):


        self.SVN_CHECKOUT_DIR = Path(deploy_conf.SVN_CHECKOUT_DIR)


        # if settings.DEBUG and self.SVN_CHECKOUT_DIR.is_dir():
        #     shutil.rmtree(str(self.SVN_CHECKOUT_DIR))

        self._file_objs = self.filelist = []

    def set_request_obj(self, request):

        self._clean()


        self.request = request
        self._pull_packages()

        self._file_objs = self._get_file_objs()


    def _clean(self):
        if self._file_objs and len(self._file_objs) > 0:
            for i in self._file_objs:
                del i

        print "======cleaned", self._file_objs


    def _pull_packages(self):
        try:
            rc = RemoteClient(self.request.POST.get("svn_url", ""), username = deploy_conf.SVN_USERNAME, password = deploy_conf.SVN_PASSWORD)
            rc.checkout(str(self.SVN_CHECKOUT_DIR))
        except Exception as e:
            raise Exception("get packages failed!\n")
        

    def _get_file_objs(self):
        self.filelist = [i for i in self.SVN_CHECKOUT_DIR.glob("**/*.*ar") if i.is_file()]

        jar_server_ip = self.request.POST['jar_server_ip']
        awar_server_ip = self.request.POST['awar_server_ip']
        cwar_server_ip = self.request.POST['cwar_server_ip']

        _file_objs = []

        for i in self.filelist:

            o = None 

            if i.suffix == ".jar" and jar_server_ip != '':     # jar
                # print 'creating jar object'
                o = JARPackage(i.name, jar_server_ip)

            elif i.suffix == ".war":
                if  'Admin' in i.name and awar_server_ip != '':  # admin war
                    o = AWARPackage(i.name, awar_server_ip)
                    # print 'creating awar object'
                elif cwar_server_ip != '':       # common war
                    o = CWARPackage(i.name, cwar_server_ip)
                    # print 'creating jar object'

            if o is not None:
                _file_objs.append(o)

                # print "========object ", o

        return _file_objs



    def deploy(self):

        for i in self._file_objs:
            i.backup()
            i.upload()
            i.replace()
            i.restart()

    # def rollback(self):
    #     for i in self._file_objs:
    #         i.rollback()


    def get_pkg_obj(self, pkg):

        for i in self._file_objs:
            if pkg == i.name:
                return i

        return None
