import web
from DB import Db
web.config.debug = False

urls = (
    '/tracks', 'Track'
    '/', 'Index',
    '/artist','Artist',
    '/album','Album',
    '/genres','genre',
    '/mediatype','mediatype',
     '/playlist', 'Playlist'
)

class Track:
    def GET(self):
        db=Db().getDb()
        tracks = db.select('Track', limit=9)
        result = '<html><head><title>Track</title>'
        result +='<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">'
        result +='<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.3/dist/jquery.slim.min.js"></script>'
        result +='<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>'
        result +='<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>'
        result +='<style>'
        result += 'h1 {'
        result += 'font-family: cursive;'
        result +='}'
        result +='</style>'
        result +='</head><body>'
        result += '<nav class="navbar navbar-expand-sm bg-light navbar-light">'
        result += '<div class="container">'
        result += '<div class="dropdown">'
        result += '<button type="button" class="btn btn-dark dropdown-toggle" data-toggle="dropdown">Top Music</button>'
        result += '<div class="dropdown-menu">'
        result += '<a class="dropdown-item" href="/artist">Artist</a>'
        result += '<a class="dropdown-item " href="/genre">Genre</a>'
        result += '<a class="dropdown-item " href="/album">Album</a>'
        result += '<a class="dropdown-item" href="/tracks">Tracks</a>'
        result += '<a class="dropdown-item " href="/mediatype">Mediatypes</a>'
        result += '<a class="dropdown-item " href="/playlist">Playlist</a>'
        result += '<a class="dropdown-item " href="/top">Top 09</a>'
        result += '</div>'
        result += '</div>'
        result += '</div>'
        result += '</nav>'
        result += '<h1 class="text-center text-succes mt-4">Top Tracks</h1>'
        result += '</div>'
        result += '<table border="1" class="table table-striped container mt-4">'
        result += '<thead class="thead-dark">'
        result += '<tr><th></th><th>Tracks</th></tr>'
        result += '<thead>'
        result += '<tbody>'
        for track in tracks:
            result += '<tr>'
            result += '<td>' + tracks + '</td>'
        result += '</tr>'
        result += '</tbody>'
        result += '</table>'
        result += '</body></html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()