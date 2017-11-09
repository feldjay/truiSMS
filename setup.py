from setuptools import setup, find_packages

setup(
    name='truiSMS',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.12.2',
        'Gunicorn>=19.7.1',
        'nose>=1.3.7',
        'twilio>=6.8.3',
    ]
)
