import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qc_financial",
    version="0.0.3",
    author="Álvaro Díaz Valenzuela",
    author_email="alvaro@efaa.cl",
    description="Libreria para la valorización de swaps de tasa de interés y moneda y forwards de tipo de cambio.",
    long_description=long_description,
    include_package_data=True,
    long_description_content_type="text/markdown",
    url="https://github.com/adiaz-efaa/Qcf-Install-Py2.7-win3.10.git",
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
    ],
    packages=setuptools.find_packages(),
)
