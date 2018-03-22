#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Spider of Bilibili
download all of the video
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals, with_statement)

import requests


def main():
    # base_url = 'http://api.bilibili.com/archive_stat/stat'
    base_url = 'http://www.bilibilijj.com/Api/AvToCid/'
    for av in range(21000000, 21020000):
        base_url += str(av)
        params = {
            # 'aid': av
        }
        r = requests.get(base_url, params=params)
        json = r.json()
        print(json)


if __name__ == '__main__':
    main()
