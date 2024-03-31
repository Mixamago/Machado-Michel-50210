from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Cronicas_fantasticas.views import *

urlpatterns = [
    # Panel de administración.
    path('admin/', admin.site.urls),
    # Páginas principales.
    path('', home, name='Inicio'),
    path('acerca_de_mi/', about, name='Acerca'),
    # Registro, inicio y cierre de sesión.
    path('registro/', user_signup, name='Registro'),  
    path('iniciar_sesion/', user_login, name='Login'),
    path('cerrar_sesion/', user_logout, name='Logout'),
    # Edición de avatar y de perfil.,
    path('editar_perfil/', edit_profile, name='Edit'),
    path('editar_avatar/', edit_avatar, name='Avatar'),
    path('borrar_avatar/', delete_avatar, name='BorrarAvatar'),    
    # Creación de objetos dentro de los modelos.
    path('crear_personaje/', create_character, name= 'CrearPersonaje'),
    path('crear_enemigo/', create_enemy, name='CrearEnemigo'),
    path('crear_calabozo/', create_dungeon, name='CrearCalabozo'),
    # Eliminación de objetos dentro de los modelos.
    path('borrar_personaje/', delete_character, name='BorrarPersonaje'),
    path('borrar_enemigo/<int:enemy_id>', delete_enemy, name='BorrarEnemigo'),
    path('borrar_calabozo/<int:dungeon_id>', delete_dungeon, name='BorrarCalabozo'),
    # Lista de los modelos.
    path('jugadores/', players_list, name='Jugadores'),
    path('personajes/', characters_list, name='Personajes'),
    path('enemigos/', enemies_list, name='Enemigos'),
    path('calabozos/', dungeons_list, name='Calabozos'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)