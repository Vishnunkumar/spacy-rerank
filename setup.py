import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
  'transformers',
  'torch',
  'spacy'
]


setuptools.setup(
    name="spacyrerank",
    version="0.0.1",
    author="Vishnu Nandakumar",
    author_email="nkumarvishnu25@gmail.com",
    description="Rank phrases and text based on query by leveraging hugging-face models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/Vishnunkumar/spacyrerank',
    packages=[
        'spacyrerank',
    ],
    package_dir={'spacyrerank': 'spacyrerank'},
    package_data={
        'spacyrerank': ['spacyrerank/*.py', 'spacyrerank/']
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='reranker, spacy, transformers',
    classifiers=(
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ),
)
