from setuptools import setup, find_packages


setup(
    name='ml_model_logging',
    version='0.1.0',
    author='Mohammed Berrada',
    author_email='medber1997@gmail.com',
    description='Logging for our models ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown', 
    url='https://github.com/tokismos/logging-for-ml-models',  #Ceci est le lien du repo qu'on a fork dans notre profile
    packages=find_packages(),
    install_requires=["ml_base>=0.2.0","rest_model_service>=0.3.1",'python-json-logger',
'setuptools'], # Les differents packages dont on aura besoin pour ce package
    classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent"
    ],
)