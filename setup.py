import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_yadavSimran',
	version = '0.0.3',
	author = 'Simran Yadav',
	author_email = 'yadavsimran281198@gmail.com',
	description = 'This is preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'
	)