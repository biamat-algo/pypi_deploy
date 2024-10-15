from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    name='great-module',
    version='0.2.0',
    description="Blah blah blah 0.2.0",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    url='https://github.com/Algolytics/dq_client',
    packages=[
        'great_module',
    ],
    package_dir={'great_module': 'great_module'},
    include_package_data=True,
    test_suite='tests'
)