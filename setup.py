from setuptools import setup, find_packages

setup(
    name='ML_Project',
    version='0.1.0',
    description='End to End Machine Learning Project.',
    author='Tejendra Kanwar',
    author_email='tejendrakanwar143@gmail.com',
    license='IIIT',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'numpy>=1.20.0'
    ]
)
