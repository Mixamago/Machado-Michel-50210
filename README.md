**Proyecto final para curso de Python: Crónicas fantásticas**

**Objetivo del proyecto**
Dado que he tenido la oportunidad de cursar la carrera de Desarrollo web en Coderhouse, quise aunar estos conocimientos a los adquiridos en el curso de Python para así poner todo en práctica.

Debido a eso, Crónicas fantásticas cuenta no solo con **Python**, sino también con **HTML** (uso más elaborado de etiquetas), **CSS** (un poco de estilo personalizado) y **Bootstrap** (sin el uso de un template prefabricado).

**¿En qué consiste Crónicas Fantásticas?**
Crónicas fantásticas simula ser un sitio en el que múltiples jugadores de rol de mesa se reúnen para disfrutar de una campaña de rol a distancia, de manera digital. Partiendo de esa premisa, este proyecto le brinda a los usuarios las siguientes opciones:

  1. Registrar un usuario.
  2. Iniciar sesión.
    - Editar la información de su perfil.
    - Agregar una imagen de perfil.
    - Eliminar su imagen de perfil.
    - Cerrar sesión
  3.  Ver la lista de personajes, calabozos y enemigos, así como también la lista de jugadores que participan.
      - Si el usuario tiene la característica de ser Dungeon Master (algo que solo puede atribuir el superusuario a través del panel de administración), entonces este también podrá crear y eliminar calabozos y enemigos.
  5.  El jugador podrá crearse un personaje.

**Modelos**

Jugadores: Tiene una relación uno a uno con el modelo usuario y el modelo avatar. Del usuario posee la información sobre su nombre de usuario, fecha de registro, último inicio de sesión y contraseña, y a eso se le adjuntó la información sobre el país del usuario.
Personajes: Tiene una relación uno a uno con los jugadores, de tal modo que cada jugador puede tener un solo personaje y cada personaje le puede pertenecer a un solo jugador. Tiene ciertos atributos (fuerza, destreza, inteligencia) que se asignan al ser creado y otros (como iniciativa o puntos de vida) que se calculan mediante una fórmula matemática en base a los atributos anteriores (puntos de vida = constitución * 10).
Enemigos: Tienne ciertos atributos (fuerza, destreza, inteligencia) que se asignan al ser creado y otros (como iniciativa o puntos de vida) que se calculan mediante una fórmula matemática en base a los atributos anteriores (puntos de vida = constitución * 10).
Calabozos: Un modelo más sencillo con solo cuatro campos de información.

**CRUD**
1. Modelo nº 1: Jugadores
      1. Crear jugador (registrarse).
      2. Editar información del jugador.
      3. Cambiar imagen de perfil del jugador.
      4. Ver la lista de jugadores.
      5. Buscar a un jugador en particular o filtrar jugadores.
2. Modelo nº2: Personajes
      1. Crear personaje (un personaje por jugador). Solo usuarios registrados.
      2. Ciertos valores del personaje (como los puntos de vida) se calculan automáticamente en base a otros.
      3. Borrar personaje, solo si el jugador ya tiene uno.
      4. Ver la lista de personajes.
      5. Buscar a un personaje en particular o filtrar personajes.
3. Modelo nº3: Enemigos
      1. Ver la lista de enemigos (todos).
      2. Crear enemigos (solo quien sea Dungeon Master).
      3. Borrar enemigos (solo quien sea Dungeon Master).
      4. Ciertos valores del personaje (como los puntos de vida) se calculan automáticamente en base a otros.
      5. Buscar a un enemigo en particular o filtrar enemigos.
4. Modelo nº4: Calabozos.
      1. Ver la lista de calabozos (todos).
      2. Crear calabozos (solo quien sea Dungeon Master).
      3. Borrar calabozos (solo quien sea Dungeon Master).
      4. Buscar un calabozo en particular o filtrar calabozos.

  **Superusuario**
- **Usuario:** GameMaster
- **Contraseña:** python1234
