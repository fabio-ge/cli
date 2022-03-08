from cli import __version__
from subprocess import getstatusoutput

prg_hello = '..\cli\hello.py'

def test_version():
    assert __version__ == '0.1.0'

def test_hello():
    """
        Controllo se il funzionamento di hello è ok
    """
    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f'{prg_hello} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'
