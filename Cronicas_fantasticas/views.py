from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from apps.cronicas.models import *
from apps.cronicas.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

#####################
#####################
##                 ##
## PÁGINAS BÁSICAS ##
##                 ##
#####################
#####################

def home(request):
        return render(request, 'cronicas/home.html')

def about(request):
        return render(request, 'cronicas/about.html')

#########################################
#########################################
##                                     ##
## REGISTRO, INICIO Y CIERRE DE SESIÓN ##
##                                     ##
#########################################
#########################################

def user_signup(request):
        context = {'bottom':True}                
        if request.method == "POST":
                if request.POST["password1"] != request.POST["password2"]:
                        context['msg'] = '<p class="text-danger">Las contraseñas no coinciden. Inténtalo de nuevo.</p>'
                        return render(request, 'cronicas/register.html', context)
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"])
                user.save()
                player = Player(user=user, country=request.POST["country"])
                player.save()
                context['msg'] = f'<p class="text-warning">El usuario se registró exitosamente: {user}.</p>'
                return render(request, "cronicas/home.html", context)
        context['msg'] = '<p class="text-warning">A continuación, ingrese los datos para registrar su cuenta.</p>'
        return render(request, 'cronicas/register.html', context)

def user_login(request):
        context = {'bottom':True}                
        if request.method == "POST":
                form = AuthenticationForm(request, data = request.POST)
                if form.is_valid():
                        this_user=form.cleaned_data.get('username')
                        this_password=form.cleaned_data.get('password')
                        user= authenticate(username=this_user, password=this_password)
                        if user:
                                login(request, user)
                                context['msg'] = '<p class="text-warning">El inicio de sesión fue exitoso.</p>'
                                context['check'] = True
                                return render(request, "cronicas/login.html", context)
                else:
                        context['msg'] = '<p class="text-danger">Hubo un error con el inicio de sesión. Por favor, inténtelo nuevamente.</p>'
                        context['form'] = form
                        return render(request, "cronicas/login.html", context)
        else: 
                form = AuthenticationForm()     
                context['form'] = form
        return render(request, 'cronicas/login.html', context)

@login_required
def user_logout(request):        
        context = {
                'bottom':True,
                "msg":"Sesión cerrada exitosamente.",
        }
        logout(request)         
        return render(request, "cronicas/logout.html", context)

#####################
#####################
##                 ##
## PERFIL Y AVATAR ##
##                 ##
#####################
#####################

@login_required
def edit_profile(request):
        context = {'bottom':True}                
        user = request.user
        jugador = Player.objects.get(user=user)
        if request.method == "POST":
                form = EditForm(request.POST)
                if form.is_valid():
                        info = form.cleaned_data
                        user.email = info["email"]
                        user.set_password(info["password1"])
                        user.first_name = info["first_name"]
                        user.last_name = info["last_name"]
                        password1 = info["password1"]
                        password2 = info["password2"]                        
                        jugador.country = info["country"]
                        if password1 == password2:
                                user.set_password(password1)
                        user.save()
                        jugador.save()
                        context['check'] = True
                        context['msg'] = '<p class="text-warning">Se pudo editar el perfil con éxito.</p>'
                        return render(request, "cronicas/edit_profile.html", context)
                else:
                        context['form'] = form
                        context['jugador'] = jugador
                        context['msg'] = '<p class="text-danger">Las contraseñas no coincidieron, inténtelo de nuevo.</p>'
                        return render(request, "cronicas/edit_profile.html", context)   
        else:
                form = EditForm(initial={
                        "email":user.email,
                        "first_name":user.first_name,
                        "last_name":user.last_name,
                        "country":jugador.country
                })
        context['form'] = form
        context['jugador'] = jugador
        context['msg'] = 'En esta página podrá actualizar los datos de su perfil.'
        return render(request, "cronicas/edit_profile.html", context)

@login_required
def edit_avatar(request):
        context = {'bottom':True}
        usuario = request.user
        try:
                avatar = Avatar.objects.get(user=usuario)
        except Avatar.DoesNotExist:
                avatar= None
        if request.method=="POST":
                form = AvatarForm(request.POST, request.FILES, instance=avatar)
                if form.is_valid():
                        avatar = form.save(commit=False)
                        avatar.user = usuario
                        avatar.save()
                        context['check'] = True
                        context['msg'] = "El cambio fue realizado con éxito."
                        return render(request, "cronicas/edit_avatar.html", context)
        else:
                form = AvatarForm()
        return render(request, "cronicas/edit_avatar.html", {"msg":"Seleccione una imagen para su perfil.", "form":form})

@login_required
def delete_avatar(request):
                context = {'bottom':True}
                usuario = request.user
                avatar = usuario.avatar
                if request.method == "POST":
                        if request.POST.get('confirm') == 'yes':
                                avatar.delete()
                                context['msg'] = f'<p class="text-warning">Su imagen de perfil ha sido borrada con éxito, {usuario}.</p>'
                                context['check'] = True
                                return render(request, 'cronicas/delete_avatar.html', context)
                        else:
                                context['msg'] = f'<p class="text-warning">Se ha conservado su imagen de perfil.</p>'
                                return render(request, 'cronicas/edit_avatar.html', context)                        
                return render(request, 'cronicas/delete_avatar.html', context)


#######################################
#######################################
##                                   ##
## LISTA DE ELEMENTOS DE CADA MODELO ##
##                                   ##
#######################################
#######################################

def players_list(request):
        context = {}
        players = Player.objects.all()
        busqueda = request.GET.get('search', '')
        if busqueda:
                players = Player.objects.filter(country=busqueda)
                users = User.objects.filter(username__icontains=busqueda)
                context['msg'] = 'Los jugadores que usted busca son estos.'
        else:
                players = Player.objects.all()
                users = User.objects.all()                
                context['msg'] = 'Los jugadores que participan en esta campaña son estos.'
        context['players'] = players        
        context['users'] = users
        return render(request, 'cronicas/players.html', context)

def characters_list(request):
        context = {'bottom':True}
        busqueda = request.GET.get('search', '')
        if busqueda:
                characters = Character.objects.filter(player__user__username__icontains=busqueda) | Character.objects.filter(name__icontains=busqueda) | Character.objects.filter(race__icontains=busqueda) | Character.objects.filter(level__icontains=busqueda) | Character.objects.filter(strength__icontains=busqueda) | Character.objects.filter(dexterity__icontains=busqueda) | Character.objects.filter(constitution__icontains=busqueda) | Character.objects.filter(intelligence__icontains=busqueda) | Character.objects.filter(attack__icontains=busqueda) | Character.objects.filter(initiative__icontains=busqueda) | Character.objects.filter(hit_points__icontains=busqueda)
                context['msg'] = 'Los personajes que usted está buscando son estos.'
        else:
                characters = Character.objects.all()
                context['msg'] = 'Estos son los personajes que forman parte de la campaña.'                  
        context['characters'] = characters     
        return render(request, 'cronicas/characters.html', context)

def enemies_list(request):
        context = {'bottom':True}
        busqueda = request.GET.get('search', '')
        if busqueda:
                enemies = Enemy.objects.filter(name__icontains=busqueda) | Enemy.objects.filter(race__icontains=busqueda) | Enemy.objects.filter(level__icontains=busqueda) | Enemy.objects.filter(strength__icontains=busqueda) | Enemy.objects.filter(dexterity__icontains=busqueda) | Enemy.objects.filter(constitution__icontains=busqueda) | Enemy.objects.filter(intelligence__icontains=busqueda) | Enemy.objects.filter(attack__icontains=busqueda) | Enemy.objects.filter(initiative__icontains=busqueda) | Enemy.objects.filter(hit_points__icontains=busqueda)
                context['msg'] = 'Los enemigos que usted está buscando son estos.'
        else:
                enemies = Enemy.objects.all()
                context['msg'] = 'Los enemigos que el grupo ha encontrado hasta ahora son estos.'
        context['enemies'] = enemies
        return render(request, 'cronicas/enemies.html', context)

def dungeons_list(request):
        context = {'bottom':True}
        busqueda = request.GET.get('search', '')
        if busqueda:
                dungeons = Dungeon.objects.filter(name__icontains=busqueda) | Dungeon.objects.filter(difficulty__icontains=busqueda) | Dungeon.objects.filter(floors__icontains=busqueda) | Dungeon.objects.filter(exp__icontains=busqueda) | Dungeon.objects.filter(gold__icontains=busqueda)
                context['msg'] = 'Los calabozos que usted está buscando son estos.'
        else:
                dungeons = Dungeon.objects.all()
                context['msg'] = 'Los calabozos que el grupo ha encontrado hasta ahora son estos.'
        context['dungeons'] = dungeons
        return render(request, 'cronicas/dungeons.html', context)

#################################################
#################################################
##                                             ##
## CREACIÓN DE ELEMENTOS DENTRO DE LOS MODELOS ##
##                                             ##
#################################################
#################################################

@login_required
def create_character(request):
        context = {'bottom':True}   
        jugador = request.user.player
        if jugador.character:
                context['hide'] = True
                context['msg'] = '<p class="text-danger">Usted ya tiene un personaje, no intente crear otro.</p>'
                return render(request, "cronicas/create_character.html", context)
        elif request.method == "POST":
                form = CharacterForm(request.POST)
                if form.is_valid():
                        character = form.save(commit=False)
                        character.user = request.user
                        character.save()
                        jugador.character = character
                        jugador.save()
                        characters = Character.objects.all()
                        context['characters'] = characters                        
                        context['msg'] = '<p class="text-warning">El personaje ha sido creado con éxito</p>'
                        return render(request, "cronicas/characters.html", context)          
        else:
                form = CharacterForm()
        context['msg'] = '<p class="text-warning">A continuación puede crear a su personaje para la campaña.</p>'
        return render(request, "cronicas/create_character.html", context)

@login_required
def create_enemy(request):
        context = {'bottom':True}              
        if request.method == "POST":
                enemy = Enemy(name=request.POST["name"], race=request.POST["race"], level=request.POST["level"], strength=request.POST["strength"], dexterity=request.POST["dexterity"], constitution=request.POST["constitution"],intelligence=request.POST["intelligence"], atk_mod=request.POST["atkmod"])
                enemy.save()
                enemies = Enemy.objects.all()
                context['enemies'] = enemies
                context['msg'] = '<p class="text-warning">El enemigo ha sido creado con éxito</p>'
                return render(request, "cronicas/enemies.html", context)
        context['msg'] = 'A continuación, puede crear un enemigo para la campaña de rol.'
        return render(request, "cronicas/create_enemy.html", context)

@login_required
def create_dungeon(request):
        context = {'bottom':True}
        if request.method == "POST":
                dungeon = Dungeon(name=request.POST["name"], difficulty=request.POST["difficulty"], floors=request.POST["floors"], exp=request.POST["exp"], gold=request.POST["gold"])
                dungeon.save()
                dungeons = Dungeon.objects.all()
                context['dungeons'] = dungeons
                context['msg'] = '<p class="text-warning">El calabozo ha sido creado con éxito</p>'
                return render(request, "cronicas/dungeons.html", context)
        context['msg'] = 'A continuación, puede crear un calabozo para la campaña de rol.'
        return render(request, "cronicas/create_dungeon.html", context)

####################################################
####################################################
##                                                ##
## ELIMINACIÓN DE ELEMENTOS DENTRO DE LOS MODELOS ##
##                                                ##
####################################################
####################################################

def delete_character(request):
        context = {'bottom':True}
        jugador = request.user.player
        personaje = jugador.character
        if jugador.character == None:
                        characters = Character.objects.all()
                        context['characters'] = characters                                
                        context['msg'] = '<p>No hay personaje para borrar.</p>'
                        return render(request, 'cronicas/characters.html', context)                
        else:     
                context['personaje'] = personaje
                if request.method == "POST":
                        if request.POST.get('confirm') == 'yes':
                                jugador.character.delete()
                                jugador.character = None
                                jugador.save()
                                context['msg'] = f'<p class="text-warning">{personaje} ha sido eliminado con éxito</p>'
                                context['check'] = True
                                return render(request, 'cronicas/delete_character.html', context)
                        else:
                                characters = Character.objects.all()
                                context['characters'] = characters                                
                                context['msg'] = f'<p class="text-warning">{personaje} ha vivido para ver otro día.</p>'
                                return render(request, 'cronicas/characters.html', context)
                context['msg'] = 'A continuación, podrá borrar a su personaje.'
                return render(request, 'cronicas/delete_character.html', context)

def delete_enemy(request, enemy_id):
        try:
                context = {'bottom':True}
                enemigo = Enemy.objects.get(pk=enemy_id)
                nombre_enemigo = enemigo.name
                context['enemigo'] = nombre_enemigo
                if request.method == "POST":
                        if request.POST.get('confirm') == 'yes':
                                enemigo.delete()
                                context['msg'] = f'<p class="text-warning">{enemigo} ha sido eliminado con éxito.</p>'
                                context['check'] = True
                                return render(request, 'cronicas/delete_enemy.html', context)
                        else:
                                enemies = Enemy.objects.all()
                                context['enemies'] = enemies
                                context['msg'] = f'<p class="text-warning">{enemigo.name} ha sobrevivido para ver otro día.</p>'
                                return render(request, 'cronicas/enemies.html', context)                        
                context['msg'] = f'¿Estás seguro de que deseas eliminar a {enemigo.name}?'
                return render(request, 'cronicas/delete_enemy.html', context)
        except Enemy.DoesNotExist:
                context['msg'] = '<p class="text-danger">El enemigo que intentas eliminar no existe.</p>'
                return render(request, 'cronicas/enemies_list.html', context)
        
def delete_dungeon(request, dungeon_id):
        try:
                context = {'bottom':True}
                calabozo = Dungeon.objects.get(pk=dungeon_id)
                nombre_calabozo = calabozo.name
                context['calabozo'] = nombre_calabozo
                if request.method == "POST":
                        if request.POST.get('confirm') == 'yes':
                                calabozo.delete()
                                context['msg'] = f'<p class="text-warning">{calabozo} ha sido eliminado con éxito.</p>'
                                context['check'] = True
                                return render(request, 'cronicas/delete_dungeon.html', context)
                        else:
                                dungeons = Dungeon.objects.all()
                                context['dungeons'] = dungeons
                                context['msg'] = f'<p class="text-warning">{calabozo.name} continuará recibiendo a los aventureros un día más.</p>'
                                return render(request, 'cronicas/dungeons.html', context)                        
                context['msg'] = f'¿Estás seguro de que deseas eliminar {calabozo.name}?'
                return render(request, 'cronicas/delete_dungeon.html', context)
        except Enemy.DoesNotExist:
                context['msg'] = '<p class="text-danger">El calabozo que intentas eliminar no existe.</p>'
                return render(request, 'cronicas/delete_dungeon.html', context)