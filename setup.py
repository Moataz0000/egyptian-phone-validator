from setuptools import setup, find_packages

setup(
    name='egyptian-phone-validator',
    version='0.1.0',
    description='A Django package to validate Egyptian phone numbers.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Moataz Fawzy',
    author_email='motazfawzy73@gmail.com',
    url='https://github.com/Moataz0000/egyptian-phone-validator',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)