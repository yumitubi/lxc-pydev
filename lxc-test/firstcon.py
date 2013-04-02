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
    container.create(TEMPLATE)
    return container.name


if __name__ == '__main__':
    create_container(name, template)
