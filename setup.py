from setuptools import setup, find_packages

requires = [
    'flask'
]

setup(
    name='webapp',
    version='0.1',
    description='Unit 10.2 webapp',
    author='<Liam T>',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)

