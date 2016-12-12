# -*- coding: utf-8 -*-

import io
import os
from ftplib import FTP, error_perm
from socket import _GLOBAL_DEFAULT_TIMEOUT


class Tunnel(object):
    def __init__(self, src_host, src_user, src_passwd, src_acct,
                 timeout=_GLOBAL_DEFAULT_TIMEOUT):

        self.src_server = FTP(host=src_host, user=src_user, passwd=src_passwd,
                              acct=src_acct, timeout=timeout)
        self.recv_servers = {}

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def add_receiver_server(self, recv_host, recv_user, recv_passwd, recv_acct):
        """Adding new server to receive files

        :param recv_host: hostname of server
        :type recv_host: str
        :param recv_user: username for connecting
        :type recv_user: str
        :param recv_passwd: user's password
        :type recv_passwd: str
        :param recv_acct: accounting information
        :type recv_acct: str
        """
        self.recv_servers['host'] = FTP(recv_host, recv_user, recv_passwd, recv_acct)

    def remove_receiver_server(self, host):
        """Removing server from recipients

        :param host: host name
        :type host: str
        """
        server = self.recv_servers.pop(host, default=None)
        try:
            server.quit()
        except AttributeError:
            raise Exception('There is no such host')

    def get_file_binary(self, path):
        """Getting file in bytearray format

        :param path: path to file
        :type path: str
        :return: file content
        :rtype: bytearray
        """
        output = bytearray()
        self.src_server.retrbinary('RETR {}'.format(path), output.extend)
        return output

    def upload_file(self, path, byte_arr):
        """Uploading file to recipient servers from byte array

        :param path: path to upload
        :type path: str
        :param byte_arr: data
        :type byte_arr: io.BytesIO
        """
        dirname, filename = os.path.split(path)
        for server in self.recv_servers.values():
            if dirname and dirname != server.pwd():
                # if path contains folder we need to change directory to it
                try:
                    # try to change active directory
                    server.cwd(dirname)
                except error_perm:
                    # exception if there is no such directory, thus we need to create it
                    server.mkd(dirname)
                    server.cwd(dirname)
                server.storbinary('STOR {}'.format(filename), byte_arr)

    def transfer(self, file_path, dest_path=None):
        """Transferring file to recipient servers

        :param file_path: path of file to transfer
        :type file_path: str
        :param dest_path: transfer path destination
        :type dest_path: str
        """
        if not dest_path:
            # set destination path to path of file if it's not provided
            dest_path = file_path
        data = self.get_file_binary(file_path)
        self.upload_file(dest_path, io.BytesIO(data))

    def close(self):
        """Closing connection for all related servers"""
        self.src_server.close()
        for server in self.recv_servers.values():
            server.close()
