from setuptools import setup, find_packages

version = '0.0.1'

install_requires = [
    'pymysql',
    'requests',
]

setup(
    name='pymysql_to_es',
    version=version,
    description="Unified standalone sign tool",
    classifiers=[],
    keywords='msyql elasticsearch sync',
    author='Baihui Wang',
    author_email='',
    url='',
    license='',
    packages=find_packages('src', exclude=['examples', 'tests']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'pymysql_to_es=pymysql_to_es.sync:main'
            ]
        },
    test_suite = 'tests',
)
