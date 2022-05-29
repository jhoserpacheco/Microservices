import os

os.system('rmdir /s /q build')
os.system('rmdir /s /q dist')
os.system('rmdir /s /q auth_lib_services.egg-info')

os.system('python setup.py bdist_wheel')
os.system('twine upload dist/*')