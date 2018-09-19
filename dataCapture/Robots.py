# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

import urllib


def robot_check(robotstxt_url, headers, url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robotstxt_url)
    rp.read()
    result = rp.can_fetch(headers['User-Agent'], url)
    return result

    # for url in urls:
    #     if robot_check(robotstxt_url, headers, url):
    #         data = get_data(url)
