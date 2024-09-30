from setuptools import setup, find_packages

setup(
    name='taskcli',
    version='0.1',
    author='McAlvaro',
    author_email='mc.alvaro641@gmail.com',
    description='A simple CLI for managing tasks',
    packages=find_packages(),
    url='https://github.com/McAlvaro/task-tracker-cli',
    license='MIT',
    install_requires=[
        'tabulate',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'taskcli = taskcli.taskcli:main'
        ]
    }
)
