from setuptools import find_packages, setup

setup(
    name='auth_lib_services',
    packages=find_packages(include=['auth_lib']),
    version='0.0.2',
    description='Library for token verification',
    author='Sachikia',
    license='MIT',
    install_requires=['requests', 'djangorestframework', 'djangorestframework-simplejwt'],
)