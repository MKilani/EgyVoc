import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EgyVoc", # Replace with your own username
    version="0.0.8",
    author="Marwan Kilani",
    author_email="kilani.edu@gmail.com",
    description="Vocaliazer for Ancient Egyptian",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MKilani/EgyVoc",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.',
)