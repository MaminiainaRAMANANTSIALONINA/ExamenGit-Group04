FROM python:3-bullseye

RUN apt update
RUN apt install mariadb-client -y
RUN pip install --no-cache-dir --upgrade web.py mysqlclient

COPY ./server.py /server.py
COPY ./DB.py /DB.py
COPY ./artist.py /artist.py
COPY ./album.py /album.py
COPY ./genre.py /genre.py
COPY ./mediatypes.py /mediatypes.py
COPY ./playlist.py /playlist.py
COPY ./tracks.py /tracks.py
COPY ./Top.py /Top.py

CMD [ "python", "/server.py" ]
