import web
from DB import Db
web.config.debug = False

urls = (
    '/album','Album',
    '/', 'index',
    '/artist','Artist',
    '/genres','genre',
    '/mediatype','mediatype'
)

class Album:
    def GET(self):
        db=Db().getDb()
        albums = db.select('Album', limit=9)
        
        result = '<html><head><title>ListAlbum</title>'
        result +='<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">'
        result +='<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.3/dist/jquery.slim.min.js"></script>'
        result +='<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>'
        result +='<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>'
        result += '<style>'
        result += 'h1 {'
        result += 'font-family: cursive;'
        result +='}'
        result += '</style>'
        result +='</head><body>'
        result += '<nav class="navbar navbar-expand-sm bg-dark navbar-dark">'
        result += '<div class="container">'
        result += '<div class="dropdown">'
        result += '<button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">Top Music</button>'
        result += '<div class="dropdown-menu">'
        result += '<a class="dropdown-item active" href="/">Accueil</a>'
        result += '<a class="dropdown-item" href="/artist">Artist</a>'
        result += '<a class="dropdown-item " href="/genre">Genre</a>'
        result += '<a class="dropdown-item " href="/album">Album</a>'
        result += '<a class="dropdown-item" href="/tracks">Tracks</a>'
        result += '<a class="dropdown-item " href="/mediatype">Mediatypes</a>'
        result += '<a class="dropdown-item " href="/playlist">Playlist</a>'
        result += '</div>'
        result += '</div>'
        result += '</div>'
        result += '</nav>'
        result += '<h1 class="text-center text-success mt-4">Tableau des Albums</h1>'
        result += '<table border="1" class="table table-striped container mt-4">'
        result += '<thead class="thead-dark ">'
        result += '<tr><th>Album</th></tr>'
        result += '</thead>'
        result += '<tbody>'
        for album in albums:
                result += '<tr>'
                result += '<td>' + album.Title + '</td>'
        result += '</tr>'
        result += '</tbody>'
        result += '</table>'
        result += '</body></html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()