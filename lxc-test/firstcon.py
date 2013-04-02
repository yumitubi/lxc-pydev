#!/usr/bin/python3.3
# -*- coding: utf-8 -*-

import lxc


name = "mak_test"
template = "debian"


def create_container(CONTAINER_NAME, TEMPLATE):
    """initalizating new container

    Arguments:
    - `CONTAINER_NAME`:
    - `TEMPLATE`:
    """
    # create instance
    print("Getting instance for '%s'" % CONTAINER_NAME)
    container = lxc.Container(CONTAINER_NAME)
    container.config_file_name == "%s/%s/config" % (lxc.default_config_path,
                                                    CONTAINER_NAME)
    # create root filesystem
    container.create(TEMPLATE)
    return container


def start_container(container):
    """

    Arguments:
    - `container`:
    """
    try:
        container.start()
        container.wait("RUNNING", 3)
        return True
    except:
        return False


def connect_to_console(container):
    """

    Arguments:
    - `container`:
    """
    print("Attaching to tty1")
    container.console(tty=1)


if __name__ == '__main__':
    new_container = create_container(name, template)
    start_container(new_container)
    connect_to_console(new_container)
