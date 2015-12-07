from setuptools import setup


with open('requirements.txt', 'r') as f:
    install_requires = [l.strip() for l in f.readlines()]


setup(
    name='sling',
    version='0.1.0',
    url='https://github.com/slinghq/sling',
    license='Apache',
    author='SlingHQ',
    author_email='support@slinghq.com',
    install_requires=install_requires,
    packages=['sling', 'sling.core', 'sling.ext'],
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
