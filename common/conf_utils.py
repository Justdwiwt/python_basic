# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

from common.named_tuples import MySQL
import configparser


class ConfigReader:
    def __init__(self, path):
        if path is None or len(path) < 1:
            raise ValueError('The config ini file path required.')
        else:
            self.conf = configparser.ConfigParser()
            self.conf.read(path)

    def get_mysql_info(self):
        host = self.conf.get('MySQL', 'host')
        user = self.conf.get('MySQL', 'user')
        pswd = self.conf.get('MySQL', 'password')
        port = self.conf.get('MySQL', 'port')
        schema = self.conf.get('MySQL', 'schema')
        charset = self.conf.get('MySQL', 'charset')
        return MySQL(host, user, pswd, int(port), schema, charset)
