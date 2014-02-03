from distutils.core import setup

with open('requirements.txt') as f:
    requirements = [l.strip() for l in f]

setup(
    name='{{cookiecutter.package_name}}',
    version='{{cookiecutter.version}}',
    packages=['{{cookiecutter.package_name}}'],
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}',
    install_requires=requirements,
    package_data={'cah': ['requirements.txt', 'README.md', 'LICENSE']}
)
