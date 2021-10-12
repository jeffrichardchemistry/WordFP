from setuptools import setup, find_packages

with open("README.md", 'r') as fr:
	description = fr.read()

setup(
    name='WordFP',
    version='1.0.0',
    url='https://github.com/jeffrichardchemistry/WordFP',
    license='GNU GPL',
    author='Jefferson Richard Dias',
    author_email='jrichardquimica@gmail.com',
    keywords='Encode, natural language processing, artificial intelligence,fingerprint',
    description='A new way to encode words and similarity calculate.',
    long_description = description,
    long_description_content_type = "text/markdown",
    packages=['WordFP'],
    install_requires=['pandas','numpy'],
	classifiers = [
		'Intended Audience :: Developers',
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Natural Language :: English',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX :: Linux',
		'Environment :: MacOS X',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',]
)
