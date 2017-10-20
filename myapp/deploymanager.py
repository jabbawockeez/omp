# coding: utf-8

import os
import flat.settings as settings
from pathlib import Path
from datetime import datetime
import shutil
from svn.remote import RemoteClient
import subprocess
import conf.deploy as deploy_conf

# import paramiko
from fabric.api import env, hosts
from fabric.operations import run, put
from fabric.contrib import files as fab_files


class DeployManager(object):
    """
    manage package deployment
    """
    def __init__(self, request):

        self.request = request

        # self.SVN_URL = request.POST.get("svn_url", "")    # newest packages' url

        # self.DIR_SRC = Path(deploy_conf.DIR_SRC)
        # self.DIR_DEST = Path(deploy_conf.DIR_DEST)
        # self.BACKUP_DIR = Path(deploy_conf.BACKUP_DIR_PREFIX).joinpath(datetime.now().strftime(deploy_conf.BACKUP_DIR_TIME_FORMAT))

        self.SVN_CHECKOUT_DIR = Path(deploy_conf.SVN_CHECKOUT_DIR)

        # self.FILES = list(map(lambda i : i + "-0.0.1-SNAPSHOT.jar", deploy_conf.FILES_PREFIX))

        # self.server_ip = request.POST.get("server_ip").split(';')

        # self.connections = {}   # connections with remote servers

        # for i in request.POST.get('server'):
        # for i in ["192.168.1.102", "192.168.1.103"]:
            # self.init_connection(ip, username, port)

        if settings.DEBUG and self.SVN_CHECKOUT_DIR.is_dir():
            shutil.rmtree(str(self.SVN_CHECKOUT_DIR))

        self._pull_packages()

        # self.files = {}     
        # self.files = {
        #     'jar' : ['1.jar', '2.jar'], 
        #     'war' : ['3.war', '4.war']
        # }
        # self._get_filelist()

        self.pkg_obj_list = []
        self._get_pkg_obj()

        self._init_fab()


    def _init_fab(self):

        env.hosts = self.request.POST.get("server_ip").split(';')
        # env.host_string = self.request.POST.get("server_ip")
        env.key_filename = "~/.ssh/id_rsa"
        env.abort_exception = Exception     # see http://docs.fabfile.org/en/latest/usage/env.html#abort-exception

        
        
    # def init_connection(self, ip, username, port):       
        # ip = '10.17.0.179'
        # username = 'root'
        # port = 22
        # paramiko.util.log_to_file('ssh.log')
        # s = paramiko.SSHClient()
        # s.load_system_host_keys()
        # s.connect(ip, port, username, key_filename = "/root/.ssh/id_rsa")
        # stdin, stdout, stderr = s.exec_command('free -m')

        # s.close()

        # self.connections[ip] = s


    # def _get_filelist(self):
    #     self.filelist = list(self.SVN_CHECKOUT_DIR.joinpath(self.package_type).glob("*.{}".format(self.package_type)))

    def _get_pkg_obj(self):
        filelist = list(self.SVN_CHECKOUT_DIR.joinpath(self.package_type).glob("*.{}".format(self.package_type)))


    def _pull_packages(self):
        try:
            rc = RemoteClient(self.request.POST.get("svn_url", ""), username = deploy_conf.SVN_USERNAME, password = deploy_conf.SVN_PASSWORD)
            rc.checkout(str(self.SVN_CHECKOUT_DIR))
        except Exception as e:
            raise Exception("_pull_packages: get packages failed!\n" + str(e))
        

    def backup_old(self):

        # print env

        if not fab_files.exists(self.DIR_DEST):     # remote directory is exists?
            raise Exception("{} does not exist!".format(self.DIR_DEST))

        if not fab_files.exists(self.DIR_SRC):
            run("mkdir -p {}".format(self.DIR_SRC)) # create directories on remote server

        run("mkdir -p {}".format(self.BACKUP_DIR))

        # print self.DIR_DEST
        # start to backup
        for pt in self.request.package_type:
            for i in self.files[pt]:    # list all files type of "pt"(jar or war)
                try:
                    # print '=========',self.DIR_DEST / i, i
                    run("cp {} {}".format(self.DIR_DEST.joinpath(i.name), self.BACKUP_DIR))    # upload packages to remote dir
                except Exception as e:
                    # print(e)
                    raise Exception("backup_old: backup failed!\n" + str(e))
                else:
                    return True


    # @hosts(env.hosts)
    def upload(self):
        # start to upload
        for pt in self.request.package_type:
            for i in self.files[pt]:    # list all files type of "pt"(jar or war)
                try:
                    # copyfile( self.DIR_DEST.joinpath(i), self.BACKUP_DIR )
                    # self.connections[ip].exec_command("cp {} {}".format(self.DIR_DEST.joinpath(i), self.BACKUP_DIR))
                    put(local_path = str(i), remote_path = str(self.DIR_SRC))    # upload packages to remote dir
                except Exception as e:
                    # print(e)
                    raise Exception("backup_old: failed!\n" + str(e))
                else:
                    return True


    def replace(self):

        def replace_jar():
            for i in self.files['jar']: 
                run("cp {} {}".format(self.DIR_SRC.joinpath(i.name), self.DIR_DEST))

        def replace_war():
            pass

        try:
            replace_jar()
            replace_war()

        except Exception as e:
            raise Exception("replace: failed!\n" + str(e))
        else:
            return True





    def restart(self):
        
        def restart_jar():
            print self.files['jar']
            for i in self.files['jar']:
                script_name = i.stem.split("-")[0] + ".sh"
                run("sh {} restart".format(self.DIR_DEST.joinpath(script_name)))


        def restart_war():
            pass

        try:
            restart_jar()
            restart_war()

        except Exception as e:
            raise Exception("restart: failed!\n" + str(e))
        else:
            return True


    def rollback(self):
        pass


    def deploy(self):
        self.backup_old()
        self.upload()
        self.replace()
        self.restart()


    # def test(self):
    #     env.hosts = ['192.168.164.26', '192.168.164.26']
    #     # env.host_string = self.request.POST.get("server_ip")
    #     env.key_filename = "~/.ssh/id_rsa"

    #     run("ls -al /tmp")


class JarDeployManager(DeployManager):

    def __init__(self, request):
        super(JarDeployManager, self).__init__(request)

        self.package_type = "jar"