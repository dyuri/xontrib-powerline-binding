from setuptools import setup

try:
    with open('README.md') as fh:
        LONG_DESC = fh.read()
except (IOError, OSError):
    LONG_DESC = ''

setup(
    name="xontrib-powerline-binding",
    version='0.3.1',
    url='https://github.com/dyuri/xontrib-powerline-binding',
    license='MIT',
    author='Gyuri Horák',
    author_email='dyuri@horak.hu',
    description='Powerline binding for xonsh',
    install_requires=[
        'powerline-status',
    ],
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',
    packages=['xontrib', 'powerline_xonsh'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    data_files=[("", ["LICENSE.txt"])],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Desktop Environment',
        'Topic :: System :: Shells',
        'Topic :: System :: System Shells',
    ]
)
