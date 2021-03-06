import os

from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES


def gen_data_files():
    """
    Generates a list of items suitables to be used as 'data_files' parameter of setup().
    Something like:
        ('arduino_proxy/webui/static', [
            'arduino_proxy/webui/static/py-arduino-proxy.js',
            'arduino_proxy/webui/static/web-ui.css',
            'arduino_proxy/webui/static/web-ui__footer.html',
            ]),
    """
    base_directory = os.path.split(__file__)[0]
    base_directory = os.path.abspath(base_directory)
    base_directory = os.path.normpath(base_directory)

    # ignored directories - relatives to 'base_directory'
    IGNORED_DIRS = [
        "arduino_proxy/webui/static/jquery-ui/development-bundle/demos",
        "arduino_proxy/webui/static/jquery-ui/development-bundle/docs",
    ]

    # to safely ignore it's children
    IGNORED_DIRS_WITH_SLASH = [item + '/' for item in IGNORED_DIRS]

    data_files = []

    walk_directory = os.path.join(base_directory, 'arduino_proxy', 'webui', 'static')
    for dirpath, _, filenames in os.walk(walk_directory):
        # dirpath -> absolute path
        # dirpath: /aaa/bbb/ccc/project/src/arduino_proxy/webui/static
        # dirpath: /aaa/bbb/ccc/project/src/arduino_proxy/webui/static/subdir1
        # dirpath: /aaa/bbb/ccc/project/src/arduino_proxy/webui/static/subdir2

        # dirpath = base_directory + src + arduino_proxy -> len(dirpath) < len(base_directory)
        # tmp -> relative to 'base_directory'
        tmp = dirpath[(len(base_directory) + 1):]

        # tmp: src/arduino_proxy/webui/static
        # tmp: src/arduino_proxy/webui/static/subdir1
        # tmp: src/arduino_proxy/webui/static/subdir2

        if tmp in IGNORED_DIRS:
            continue
        if [item for item in IGNORED_DIRS_WITH_SLASH if tmp.startswith(item)]:
            continue

        # tmp2 = tmp[(len("src") + 1):] # remove 'src', to use as 1st item of list
        tmp2 = tmp

        # tmp2: arduino_proxy/webui/static
        # tmp2: arduino_proxy/webui/static/subdir1
        # tmp2: arduino_proxy/webui/static/subdir2

        data_files.append([
            tmp2,
            [os.path.join(os.path.join(tmp2), f) for f in filenames]
        ])

        # print "append:", data_files[-1]

    return data_files

name = "PyArduinoProxy"
version = "0.0.3"
description = 'Communicate with Arduino from Python, a web page and JavaScript'
author = "Horacio G. de Oro"
author_email = "hgdeoror@gmail.com"
url = "http://pyarduinoproxy.blogspot.com/"
packages = [
    'arduino_proxy',
    'arduino_proxy.tests',
    'arduino_proxy.webui',
    'arduino_proxy.cli',
    'arduino_proxy.cli.ping',
    'arduino_proxy.cli.webserver',
]

install_requires = (
    'cherrypy<3.3', # 3.2.x
    'jinja2<2.7', # 2.6.x
    'pyserial',
    'simplejson',
)

classifiers = [ # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    "Programming Language :: C",
    "Programming Language :: JavaScript",
    "Programming Language :: Python",
    "Topic :: Communications",
    "Topic :: Utilities",
]

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

setup(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    packages=packages,
    classifiers=classifiers,
    data_files=gen_data_files(),
    install_requires=install_requires,
)
