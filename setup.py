from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='clcomuna',
      version='1.0',
      description='Given the name of a comuna in Chile, it returns its code',
      url='http://github.com/slarrain/clcomuna',
      author='Santiago Larrain',
      author_email='santiagolarrain@gmail.com',
      license='MIT',
      packages=['clcomuna'],
      install_requires=[
          'fuzzywuzzy',
      ],
      #data_files=[('data', ['comunas.csv'])],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
