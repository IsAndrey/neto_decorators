import setuptools


required = ['setuptools>=75.0.0']

setuptools.setup(
    name='simple_logger',
    version='1.01',
    packages=setuptools.find_packages(
        include=['neto_decorators']
    ),
    install_reqires=required,
    python_requires='>=3.8'
)
