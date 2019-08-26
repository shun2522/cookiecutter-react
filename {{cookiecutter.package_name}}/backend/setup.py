
#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='{{cookiecutter.package_name}}',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask'
    ]
)
