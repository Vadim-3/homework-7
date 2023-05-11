from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.2',
    description='sorts the files in a folder',
    url='https://github.com/Vadim-3/homework-7.git',
    author='Bezhuk Vadim',
    author_email='bezhukvadim.56@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'clean-folder=clean_folder.clean:main']}  # clean.py
)
