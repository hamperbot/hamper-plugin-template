from distutils.core import setup

with open('requirements.txt') as f:
    requirements = [l.strip() for l in f]

setup(
    name='{{package_name}},
    version='0.1',
    packages=['{{package_name}}'],
    author='{{full_name}}',
    author_email='{{email}}',
    url='https://github.com/{{github_username}}/{{cookiecutter.repository_name}}',
    install_requires=requirements,
    package_data={'cah': ['requirements.txt', 'README.md', 'LICENSE']}
)
