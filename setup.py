"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smm_wrapper",
    version="1.0.1",
    # Author details
    author="Alexandra Stannida, Roberto Ulloa",
    author_email="alexandra.stankevich@gesis.org,roberto.ulloa@gesis.org",
    description="A light Python wrapper for the SMM API (Politicians Social Media Monitoring API)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gesiscss/smm_wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    # What does your project relate to?
    keywords='social media smm politicians',
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['requests', 'pandas']
)
