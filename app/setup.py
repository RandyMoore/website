from setuptools import setup

setup(
    name='app',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
        'flask_login',
        'flask_blogging',
        'passlib'
    ],
)