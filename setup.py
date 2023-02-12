from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="chatgpt-api",
    version="0.1.1",
    author="Emanuel Ribeiro",
    author_email="imma.ribeiro@gmail.com",
    description="api calls to chatgpt, outputs files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/immaribeiro/chatgpt_api/",
    packages=find_packages(),
    install_requires=[
        "openai"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
    'console_scripts': ['chatgpt-api-start=config.start']
    },
    package_data={
        "my_project": ["utils/*"]
    },
    include_package_data=True
)
