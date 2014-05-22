import os
import click
from pybloomfilter import BloomFilter

size = 10000000
error_rate = 0.001
bloomfilter_filename = 'nsrl.bloom'

@click.group()
def nsrl():
    """A simple tool to convert the NSRL database to a bloomfilter."""
    pass

@click.command('build', short_help='build bloomfilter from NSRL database')
def build():
    """Build bloomfilter from NSRL database."""
    if os.path.isfile('/nsrl/NSRLFile.txt'):
        bf = BloomFilter(size, error_rate, bloomfilter_filename)
        hashes = [line.split(",")[1].strip('"') for line in open('/nsrl/NSRLFile.txt')]
        bf.update(hashes)
    else:
        click.echo("ERROR: No such file or directory: '/nsrl/NSRLFile.txt'")

@click.command('search', short_help='search NSRL Database for hash')
@click.argument('hash')
def search(hash):
    """Search NSRL Database for hash."""
    bf = BloomFilter.open(bloomfilter_filename)
    print hash in bf

nsrl.add_command(build)
nsrl.add_command(search)

if __name__ == '__main__':
    nsrl()
