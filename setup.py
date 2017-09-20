"""
Flask-Couchbase
---------------

Couchbase Flask Extension
"""
from setuptools import setup


setup(
    name='Flask-Couchbase',
    version='1.0',
    url='https://github.com/oliora/flask_couchbase',
    license='MIT',
    author='Andrey Upadyshev',
    author_email='oliora@gmail.com',
    description='Couchbase Flask Extension',
    keywords='flask couchbase nosql extension',
    long_description=__doc__,
    py_modules=['flask_couchbase'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'couchbase>=2.0'  # ???
    ],
    tests_require='nose',
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
