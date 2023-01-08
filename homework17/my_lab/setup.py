import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="alashnikov_temp_conv",
    version="0.1",
    author="Alex Alashnikov",
    author_email="tonikark6@gmail.com",
    description="This is a temperature conversion package.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexAlashnikov/Homework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)