from setuptools import find_packages, setup

setup(
    name='minerva',
    packages=find_packages(include=['minerva']),
    version='0.1.0',
    description='Python minerva framework is a data base and a dynamic web server.',
    author='Victor Bona',
    license='MIT',
    author_email='victor.bona@hotmail.com',
    download_url='https://pypi.org/project/minerva/',
    url='https://github.com/vicotrbb/minerva',
    project_urls={
        "Bug Tracker": "https://github.com/vicotrbb/minerva/issues",
        "Source Code": "https://github.com/vicotrbb/minerva"
    },
    keywords=['Python3'],
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    install_requires=[],
    setup_requires=['wheel', 'pytest-runner', 'flake8'],
    tests_require=['pytest'],
    python_requires=">=3.5",
    classifiers=(
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Web Framework",
        "Operating System :: OS Independent",
    ),
)
