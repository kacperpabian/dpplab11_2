from distutils.core import setup

setup(name='lab11dpp2',
	  version='1.0',
	  author='Kacper Pabian',
	  author_email='226123@student.pwr.edu.pl',
	  url='https://github.com/kacperpabian/dpplab11_2.git',
	  download_url='https://github.com/kacperpabian/dpplab11code.git',
	  packages=['lab11lib2', 'lab11lib2.classes', 'lab11lib2.MainDir'], requires=['PyRECONSTRUCT']
	  )