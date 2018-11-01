from setuptools import setup, find_packages

def load_requirements():
    with open('requirements.txt') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    return content


kayrros_requirements = []
requirements = load_requirements() + kayrros_requirements

setup(
    name='stations clustering',
    version='0.1',
    author='',
    author_email='',
    description='clustering the stations',
    packages=find_packages(),
    install_requires=requirements,
    dependency_links=[
    ]
)
