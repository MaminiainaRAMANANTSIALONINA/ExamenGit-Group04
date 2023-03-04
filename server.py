import web
web.config.debug = False
from DB import Db
from artist import Artist
from album import Album
from mediatypes import MediaType
from genre import Genre
from tracks import Track
from playlist import Playlist
from Top import Top

urls = (
    '/', 'index',
    '/artist','Artist',
    '/album','Album',
    '/mediatypes','MediaType',
    '/genre','Genre',
    '/playlist','Playlist',
    '/tracks','Tracks',
    '/top', 'Top'
)

class index:
    def GET(self):
        db=Db().getDb()
        result = '<html>'
        result +='<head><title>Accueil</title>'
        result +='<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">'
        result +='<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.3/dist/jquery.slim.min.js"></script>'
        result +='<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>'
        result +='<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>'
        result +='<style>'
        result += '.title{'
        result += 'position: absolute;'
        result += 'color: white;'
        result += 'margin-top: 35px;'
        result += 'margin-left: 32%;'
        result += 'font-family: cursive;'
        result += '}'
        result += 'body{'
        result += 'background-image: url("https://wallpaper-house.com/data/out/5/wallpaper2you_70397.jpg");'
        result += 'overflow-x: hidden;'
        result += '}'
        result +='nav{'
        result +='background: black;'
        result +='}'
        result +='</style>'
        result +='</head>'
        result += '<body>'
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
        result += '<div class="col-lg-12"><h1 class="title text-success">De la musique pour tous</h1></div>'
        result += '</body>'
        result += '</html>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
