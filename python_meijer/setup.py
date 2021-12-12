from setuptools import setup

setup(
    name='python_meijer',
    version='0.1.0',
    description='A python wrapper for the Meijer API',
    url='https://github.com/sllawcj/python_Meijer',
    author='sllawcj',
    author_email='cjsllaw@gmail.com',
    license='MIT',
    packages=['meijer'],
    install_requires=[
        'cached-property==1.5.2', 'certifi==2021.10.8', 'charset-normalizer==2.0.7', 'idna==3.3', 'requests==2.26.0', 'urllib3==1.26.7'],

    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
