from setuptools import setup
import os
import subprocess


def install_dependencies():
    subprocess.check_call(["pip", "install", "pyminifier", "pyarmor"])


install_dependencies()

setup(
    name='testedwin',
    version='0.1',
    license='MIT',
    author="Mario Nascimento",
    author_email='marionascimento047@gmail.com',
    packages=['testedwin'],
    url='https://github.com/darkarp/testedwin',
    keywords='example project',
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'background_task=testedwin.background_task:configure_package',
            'post_install=testedwin.post_install:run',
        ]
    }
)
