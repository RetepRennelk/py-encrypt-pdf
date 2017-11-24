from setuptools import setup, find_packages

setup( 
    name = 'py-encrypt-pdf',
    version = '0.1',
    description = 'Ghostscript wrapper for convenient PDF password encryption',
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'py-encrypt-pdf=py_encrypt_pdf.py_encrypt_pdf:encrypt']})
