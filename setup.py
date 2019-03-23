import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fb-cli",
    version="0.0.2",
    author="Chinmaya Krishnan Mahesh",
    author_email="chinmaya.mahesh@gmail.com",
    description="Facebook Command Line Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chin123/fbcli",
    scripts=['fb-cli'],
    install_requires=['bs4', 'requests', 'colorama'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
