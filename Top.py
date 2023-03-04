import web
from DB import Db 

web.config.debug = False

urls = (
    '/top','Top',
    '/', 'Index'
)

class Top:
    def GET(self):
        db=Db().getDb()
        albums=db.select('Album', limit=9)
        artists=db.select('Artist', limit=9)
        genres=db.select('Genre', limit=9)
        mediatypes=db.select('MediaType', limit=9)
        tracks =db.select('Track', limit=9)
        playlists=db.select('Playlist', limit=9)
        result = '<html><head><title>Top09</title>'
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
        result += '<h1 class="text-success text-center">Voici le classement des musiques en ce moments</h1>'
        result += '<table border="1" class="table table-striped container mt-4">'
        result += '<thead class="thead-dark">'
        result += '<tr><th>#</th><th>Artists</th><th>Albums</th><th>Genres</th><th>Mediatypes</th><th>Tracks</th><th>Playlists</th></tr>'
        result += '<tbody>'
        
        for artist in artists:
            result += '<tr>'
            result += '<td>' +str(artist.ArtistId)+'</td>'
            result += '<td>' + artist.Name + '</td>'
            for album in albums:
                result += '<td>' + album.Title + '</td>'
                break
            for genre in genres:
                result +='<td>' + genre.Name + '</td>'
                break
            for mediatype in mediatypes:
                result +='<td>' + mediatype.Name + '</td>'
                break
            for track in tracks:
                result +='<td>' + track.Name + '</td>'
                break
            for playlist in playlists:
                result += '<td>' + playlist.Name + '</td>'
                break
            result += '</tr>'
        result += '</tbody>'
        result += '</table>'
        result += '</body></html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
