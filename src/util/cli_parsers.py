import click

@click.command('add',
               help='add a new file to the database')
@click.argument('title')
@click.argument('genre')
@click.argument('location')
@click.option('-a',
              'authors',
              multiple=True,
              help='the author(s) of the file')
@click.option('-t',
              'tags',
              multiple=True,
              help='tags describing the file')
def add(title, genre, authors, tags, location):
    print(authors)
    pass

@click.command('edit',
               help='edit an existing entry in the database')
def edit():
    pass

@click.command('delete',
               help='delete an entry in the database')
@click.option('-i',
              '--file_id',
              help='the id of the file being deleted')
@click.option('-t',
              '--title',
              help='the title of the files being deleted')
@click.option('-g',
              '--genre',
              help='the genre of the files being deleted')
@click.option('-a',
              '--authors',
              multiple=True,
              help='the author of the files being deleted')
def delete():
    pass

@click.command('search',
               help='search for entries in the database')
@click.option('-i',
              '--id',
              help='the id of the file being searched') 
@click.option('--title',
              help='the title of the file being searched') 
@click.option('-g',
              '--genre',
              help='the title of the file being searched') 
@click.option('-a',
              '--authors',
              help='an author of the file being searched') 
@click.option('-t',
              '--tags',
              help='a tag describing the file being searched') 
def search():
    pass

@click.command('open',
               help='open a file')
@click.argument('file_id')
def open_file(file_id):
    pass
