from setuptools import setup, find_packages

setup(
    name="folder-sorter",
    version="0.1.0",
    description="A utility to sort files in a folder by file type.",
    author="Beatrice M. Antoniu",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "folder-sorter = main:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
