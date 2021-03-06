import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timeconMT",
    version="0.0.2",
    author="Cole Malphrus",
    author_email="cole@malphrus.tech",
    description="time converter utilities",
    long_description=long_description,
    url="https://github.com/colemalphrus/timeconMT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)