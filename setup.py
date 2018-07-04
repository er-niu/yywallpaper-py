from setuptools import setup, find_packages

setup(
    name="yywallpaper-py",
    version="0.1",
    packages=find_packages(exclude=('tests', 'tests.*')),
    scripts=[],
    include_package_data=True,
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['docutils>=0.3', 'setuptools>=16.0'],


    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.cfg'],
        # And include any *.msg files found in the 'hello' package, too:
        'conf': ['*.cfg'],
    },

    # metadata for upload to PyPI
    author="Me",
    author_email="me@example.com",
    description="This is an Example Package",
    license="PSF",
    keywords="hello world example examples",
    url="http://yywallpaper.top",  # project home page, if any
    zip_safe=False,
    # could also include long_description, download_url, classifiers, etc.
)
