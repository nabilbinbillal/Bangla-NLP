from setuptools import setup, find_packages

setup(
    name="bangla-nlp",
    version="0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.8",
    description="Bangla NLP toolkit: tokenization, stopwords, POS, NER, sentiment (offline, editable datasets).",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nabilbinbillal/Bangla-NLP",
    author="Nabil Bin Billal",
    author_email="nabilbinbillal@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic"
    ],
)
