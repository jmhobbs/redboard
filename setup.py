from setuptools import setup


setup(
    name='redboard',
    version='0.0.1',
    url='https://github.com/jmhobbs/redboard',
    license='MIT',
    author='John Hobbs',
    author_email='john@velvetcache.org',
    description='redboard is a Flask embeddable dashboard for Redis.',
    long_description=__doc__,
    package_dir={'': 'src'},
    packages=['redboard'],
    scripts=['src/redboard_server.py', 'src/redboard_monitor.py'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['Flask', 'redis'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Monitoring',
    ]
)
