# -*- coding: utf-8 -*-

from . import models


def simple_transfer(src_host, recv_host, **kwargs):
    """Tunnel object between 2 ftp servers

    :param src_host: hostname of server from which data sends
    :type src_host: str
    :param recv_host: hostname of server that receives data
    :type recv_host: str
    :param src_user: username for sender server
    :type src_user: str
    :param src_passwd: user's password for sender server
    :type src_passwd: str
    :param src_acct: accounting information for sender server
    :type src_acct: str
    :param recv_host: hostname of server from which data sends
    :type recv_host: str
    :param recv_host: hostname of server that receives data
    :type recv_host: str
    :param recv_user: username for sender server
    :type recv_user: str
    :param recv_passwd: user's password for sender server
    :type recv_passwd: str
    :param recv_acct: accounting information for sender server
    :type recv_acct: str
    :rtype: ftp2ftp.Tunnel
    """
    transfer = models.Tunnel(src_host, **kwargs)
    transfer.add_receiver_server(recv_host, **kwargs)
    return transfer


def simple_transfer_file(src_host, recv_host, file_path, dest_path, **kwargs):
    """Transferring file between 2 ftp servers

    :param src_host: hostname of server from which data sends
    :type src_host: str
    :param recv_host: hostname of server that receives data
    :type recv_host: str
    :param src_user: username for sender server
    :type src_user: str
    :param src_passwd: user's password for sender server
    :type src_passwd: str
    :param src_acct: accounting information for sender server
    :type src_acct: str
    :param recv_host: hostname of server from which data sends
    :type recv_host: str
    :param recv_host: hostname of server that receives data
    :type recv_host: str
    :param recv_user: username for sender server
    :type recv_user: str
    :param recv_passwd: user's password for sender server
    :type recv_passwd: str
    :param recv_acct: accounting information for sender server
    :type recv_acct: str
    :param file_path: path of file to transfer
    :type file_path: str
    :param dest_path: transfer path destination
    :type dest_path: str
    :rtype: ftp2ftp.Tunnel
    """
    with simple_transfer(src_host, recv_host, **kwargs) as transfer:
        transfer.transfer(file_path, dest_path)
