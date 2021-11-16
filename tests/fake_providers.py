import random
from datetime import datetime
from datetime import timedelta
from src.modelo.album import Medio

from faker import Faker

from faker.providers import BaseProvider

class AlbumTituloProvider(BaseProvider):
    def albumTitulo(self):
        albumesTitulo = ['Latin Jazz Compilation', 'Bandas sonoras famosas', 'The Dark Side of the Moon',
                         'The Bodyguard', 'Rumours', 'Saturday Night Fever', 'El fantasma de la ópera', 'Come on Over']
        return random.choice(albumesTitulo)

class AlbumAnioProvider(BaseProvider):
    def albumAnio(self):
        anio = [2018, 2019, 2020, 2021]
        return random.choice(anio)

class AlbumDescripcionProvider(BaseProvider):
    def albumDescripcion(self):
        descripcion = ["Album original", "Compilación"]
        return random.choice(descripcion)

class AlbumMedioProvider(BaseProvider):
    def albumMedio(self):
        self.medios = [Medio.CD, Medio.CASETE, Medio.DISCO]
        return random.choice(self.medios)

class AlbumFechaProvider(BaseProvider):
    def AlbumFecha(self):
        new_date = datetime(2019, 2, 28, 00, 00, 00, 00000)
        fecha = [new_date, new_date + timedelta(days=-1), new_date + timedelta(days=-2)]
        return random.choice(fecha)

class CancionTituloProvider(BaseProvider):
    def CancionTitulo(self):
        CancionesTitulo = ['Copy Light', 'Unravel', 'The Kill', 'The Reason', 'Apologize', 'Talking To The Moon', 'Lost On You',
                          'Stan', 'Monster', 'My Demons']
        return random.choice(CancionesTitulo)

class CancionMinutosProvider(BaseProvider):
    def CancionMinutos(self):
        CancionesMinutos = [3, 2, 1, 4, 5, 6]
        return random.choice(CancionesMinutos)

class CancionSegundosProvider(BaseProvider):
    def CancionSegundos(self):
        CancionesSegundos = [30, 45, 58, 23, 18, 40, 12, 32]
        return random.choice(CancionesSegundos)

class CancionCompositorProvider(BaseProvider):
    def CancionCompositor(self):
        CancionesCompositor = ['Gian Marco', 'Franco de Vida', 'Leonel Garcia', 'Noel Schajris', 'Javier Artés Arlandis', 'Paul McCartney', 'John Lennon']
        return random.choice(CancionesCompositor)

class InterpreteNombreProvider(BaseProvider):
    def InterpreteNombre(self):
        InterpretesNombres = ['Majico', 'Bruno Mars', 'Toru Kitajima', 'Jose Madero', 'Alejandro Sanz', 'Omar Acedo', 'Chester Bennington']
        return random.choice(InterpretesNombres)

class InterpreteTexto_CuriosidadesProvider(BaseProvider):
    def InterpreteTexto_Curiosidades(self):
        InterpretesTexto_Curiosidades = ['Ha obtenido 450.000 seguidores en Instagram', 'No tiene cuenta de Facebook', 'Dejo la Universidad', 'Le teme a las alturas']
        return random.choice(InterpretesTexto_Curiosidades)