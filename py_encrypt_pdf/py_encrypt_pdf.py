import os
import sys
import click

def ensure_dir_exists(path):
    if not(os.path.isdir(path)):
        os.makedirs(path)

def encrypt_file(passwd, file):
    if not os.path.isfile(file):
        print('WARNING: {} does not exist.'.format(file))
        return
    path, filename = os.path.split(file)
    target_dir = os.path.join(path, 'encrypt')
    ensure_dir_exists(target_dir)
    target_file = os.path.join(target_dir, filename)
    cmd = 'gswin64c -dNOPAUSE -q -dBATCH -sDEVICE=pdfwrite -sOwnerPassword={0} -sUserPassword={0} -sOutputFile={1} {2}'.format(passwd,target_file,file)
    os.system(cmd)

def encrypt_dir(passwd, path):
    if not os.path.isdir(path):
        return
    dirlist = os.listdir(path)
    for file in dirlist:
        if file.endswith('.pdf'):
            file = os.path.join(path, file)
            encrypt_file(passwd, file)

@click.command()
@click.option('--passwd', prompt=True, hide_input=True,
              confirmation_prompt=True, help="Password without prompt.")
@click.argument('files_or_dir', nargs=-1)
def encrypt(passwd, files_or_dir):
    '''
    py-encrypt-pdf.py wraps gswin64c and is a convenience function 
    for setting user and ower password for pdfs.
    '''
    for fod in files_or_dir:
        if os.path.isfile(fod):
            encrypt_file(passwd, fod)
        elif not fod.endswith('.pdf'):
            encrypt_dir(passwd, fod)
        else:
            print('WARNING: {} does not exist.'.format(fod))
            
if __name__ == '__main__':
    encrypt()
    