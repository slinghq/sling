from setuptools import setup


setup(
    name='sling',
    version='0.1.0',
    url='https://github.com/slinghq/sling',
    license='Apache',
    author='SlingHQ',
    author_email='support@slinghq.com',
    packages=['sling', 'sling.ext'],
    platforms='any',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Environment :: Web Environment',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
