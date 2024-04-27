from setuptools import setup, find_packages


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="ozon_ord",
    author="Artem Frolov",
    author_email="pypi-username@mail.ru",
    version="0.0.1.b1",
    keywords="ozon, ord, ozon-ord, api, sdk, python",
    description="Ozon ОРД API - Python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/frollow/ozon_ord",
    package_dir={"": "ozon_ord"},
    packages=find_packages("ozon_ord"),
    install_requires=["requests>=2.31.0", "pydantic>=2.7.0"],
    zip_safe=False,
    license="MIT",
    python_requires=">=3.8",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
