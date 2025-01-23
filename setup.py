from setuptools import setup, find_packages

setup(
    name='notify-mattermost',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    package_dir={'': '.'},
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
        "requests",
        "argparse"
    ],
    entry_points={
        'console_scripts': [
            'mattermost-notify=mattermost_notify.cli:main',
        ],
    },
    author='Noah Kleinschmidt',
    author_email='noah.kleinschmidt@unibe.ch',
    description='A tool to send notifications to Mattermost',
    url='https://github.com/NoahHenrikKleinschmidt/mattermost-notify',
)