"""The Spanish text of the blog and comparison pages. content.py merges it in; see build_pages.py and langs.py.

Each key in ARTICLES is an article slug from content.py. {YEAR} stands for the current year."""

UI = {
    "nav_label": "Menú principal",
    "blog": "Blog",
    "compare": "Comparar",
    "download": "Consigue AkhiBrowser",
    "blog_title": "Guías de navegación halal",
    "blog_lead": "Guías prácticas para navegar por la web con menos anuncios, menos contenido haram y más control, en tu propio dispositivo.",
    "cta_title": "Consigue AkhiBrowser",
    "cta_text": "Un navegador privado para musulmanes, basado en Firefox. En Microsoft Store para Windows y en Google Play para Android. Las protecciones son gratuitas.",
    "footer": "AkhiBrowser está basado en <a href=\"https://www.firefox.com/\">Firefox</a>, y no está hecho ni respaldado por Mozilla. Los filtros pueden dejar pasar cosas, y no sustituyen el cuidado de los padres. <a href=\"/es/\">Inicio</a> · <a href=\"/es/faq/\">Preguntas frecuentes</a> · <a href=\"mailto:support@akhibrowser.com\">support@akhibrowser.com</a>",
}

ARTICLES = {
    "what-is-a-halal-browser": {
        "title": "¿Qué es un navegador halal y lo necesitas?",
        "description": "Qué hace un navegador halal, qué no puede hacer y cómo elegir uno: bloqueo de sitios, SafeSearch, difuminado de imágenes y privacidad explicados.",
        "body": """<p>Un navegador halal es un navegador web que filtra lo que un navegador normal deja en tus manos. Bloquea sitios y búsquedas de cosas como contenido para adultos, alcohol y apuestas, y mantiene las imágenes no deseadas fuera de tu pantalla.</p>
<h2>Qué suele hacer un navegador halal</h2>
<ul>
<li><strong>Bloquea sitios.</strong> Los sitios para adultos, de apuestas, alcohol y drogas se detienen antes de cargar.</li>
<li><strong>Fuerza SafeSearch.</strong> Los buscadores ocultan los resultados explícitos, sin que tengas que configurarlo.</li>
<li><strong>Filtra imágenes.</strong> Las imágenes con desnudos se difuminan.</li>
<li><strong>Bloquea anuncios y rastreadores.</strong> Muchas imágenes no deseadas llegan a través de la publicidad, así que esto ayuda dos veces.</li>
</ul>
<h2>Qué no puede hacer</h2>
<p>Ningún filtro es perfecto. Algunas páginas se cuelan y algunas inofensivas se bloquean. Además, un navegador solo protege lo que pasa dentro de él: las otras apps y navegadores del mismo dispositivo no quedan cubiertos. Ayuda con la intención y el hábito, pero no los sustituye, ni tampoco el cuidado de los padres.</p>
<h2>Cómo elegir uno</h2>
<ul>
<li><strong>¿Dónde se hace la comprobación?</strong> Filtrar en tu propio dispositivo significa que tus imágenes no tienen que salir de él.</li>
<li><strong>¿Qué sale de tu dispositivo?</strong> Busca una lista clara. Un navegador que diga «nada» debería poder explicar cómo bloquea sitios y se actualiza.</li>
<li><strong>¿Puedes controlarlo?</strong> Deberías poder ver y cambiar cada protección.</li>
<li><strong>¿Funciona en tus dispositivos?</strong> Compruébalo antes de decidirte, sobre todo en un iPhone o un Mac.</li>
</ul>
<h2>¿Navegador halal, extensión o filtro DNS?</h2>
<p>Hay tres formas habituales de filtrar la web, y funcionan mejor juntas:</p>
<ul>
<li><strong>Un navegador halal</strong> filtra dentro del propio navegador: sitios, búsquedas, imágenes y vídeo. Sus protecciones están activas desde la primera página y se pueden bloquear con un PIN.</li>
<li><strong>Una extensión de navegador</strong> añade un filtro a un navegador que ya usas, como Chrome. Es rápida de probar, pero normalmente se puede quitar o desactivar, y no puede cambiar cómo funciona el navegador en sí.</li>
<li><strong>Un filtro DNS o del router</strong> bloquea sitios enteros para todas las apps de un dispositivo o una red. No puede mirar dentro de una página, así que no puede difuminar una imagen ni quitar la música de un vídeo.</li>
</ul>
<p>Para una familia, una configuración habitual es un DNS familiar en el router más un navegador halal en cada dispositivo, con los demás navegadores quitados o bloqueados. Lee <a href="/es/blog/block-haram-content/">cómo bloquear el contenido haram en tu teléfono y tu ordenador</a> para la configuración completa.</p>
<h2>Una lista para elegir un navegador halal</h2>
<ul>
<li>¿Se bloquean los sitios para adultos, de apuestas, alcohol y drogas desde la primera página, sin configurar nada?</li>
<li>¿Se fuerza SafeSearch en todos los buscadores, incluido YouTube?</li>
<li>¿Se comprueban las imágenes en tu dispositivo o se envían a un servidor?</li>
<li>¿Puede un padre bloquear los ajustes con un PIN?</li>
<li>¿Dice claramente qué sale de tu dispositivo?</li>
<li>¿Sigue actualizándose? Un navegador que deja de recibir actualizaciones también deja de recibir correcciones de seguridad. SalamWeb, uno de los primeros navegadores halal, se abandonó en 2021.</li>
</ul>
<p>Comparamos las opciones en <a href="/es/blog/best-halal-browsers/">los mejores navegadores halal de {YEAR}</a>.</p>
<h2>Preguntas frecuentes</h2>
<h3>¿Un navegador halal es solo para musulmanes?</h3>
<p>No. Cualquiera que quiera menos anuncios, nada de contenido para adultos y más control sobre las imágenes puede usarlo. El nombre describe los valores sobre los que está hecho.</p>
<h3>¿Un navegador halal es gratis?</h3>
<p>Muchos lo son. Las protecciones de AkhiBrowser son gratuitas, con un Premium opcional para más ajustes de imagen y herramientas para padres.</p>
<h3>¿Un navegador halal sustituye al control parental?</h3>
<p>Cubre el navegador. Para las apps y otros navegadores, combínalo con los controles del dispositivo, como Google Family Link o Microsoft Family Safety. Consulta <a href="/es/blog/parental-controls-for-muslim-families/">una configuración sencilla de control parental</a>.</p>
<h3>¿Puede un navegador halal quitar la música de los vídeos?</h3>
<p>Algunos pueden. AkhiBrowser <a href="/es/blog/remove-background-music-from-videos/">quita la música de fondo en tu dispositivo</a>, así que las voces se quedan y la música se va.</p>
<p>AkhiBrowser es una opción, basada en Firefox para Windows y Android. Sus protecciones están activas desde la primera página, y <a href="/es/privacy/">su web detalla qué sale de tu dispositivo</a>. También puedes leer <a href="/es/compare/kahf-browser/">cómo se compara con Kahf Browser</a>.</p>""",
    },
    "block-haram-content": {
        "title": "Cómo bloquear el contenido haram en tu teléfono y tu ordenador",
        "description": "Un método paso a paso para bloquear contenido para adultos, apuestas y alcohol: filtros del navegador, SafeSearch, DNS familiar y controles del dispositivo, y lo que se le escapa a cada uno.",
        "body": """<p>Ningún ajuste por sí solo lo bloquea todo. Lo que funciona son varias capas, cada una cubriendo lo que se les escapa a las demás.</p>
<h2>1. Usa un navegador que filtre por defecto</h2>
<p>Un navegador con filtro bloquea sitios, filtra búsquedas y difumina imágenes sin configuración. En AkhiBrowser, los sitios para adultos, de alcohol, drogas, vapeo y apuestas se bloquean desde la primera página.</p>
<h2>2. Fuerza SafeSearch</h2>
<p>SafeSearch oculta los resultados explícitos en los buscadores. Puedes activarlo en los ajustes de cada buscador, pero es fácil volver a desactivarlo y solo vale para un navegador. Un navegador con filtro puede forzarlo: AkhiBrowser lo hace en Google, Bing, DuckDuckGo y Yahoo, y activa el Modo restringido de YouTube.</p>
<h2>3. Añade un DNS familiar</h2>
<p>Un servicio de DNS familiar se niega a buscar sitios para adultos, para todo lo que haya en esa red o dispositivo. El 1.1.1.3 de Cloudflare y CleanBrowsing son opciones conocidas. Funciona por nombre de sitio, así que no ve lo que hay en un sitio permitido, y quien lo gestiona ve los nombres de los sitios que visitas.</p>
<h2>4. Cierra las puertas traseras</h2>
<p>Un filtro de navegador no cubre otras apps. En el dispositivo de un niño, usa Google Family Link en Android o Microsoft Family Safety en Windows para controlar qué apps y navegadores se pueden instalar. En AkhiBrowser, Family Premium también puede bloquear los ajustes con un PIN y desactivar las pestañas privadas.</p>
<h2>5. Sigue hablando</h2>
<p>Los filtros dejan pasar cosas, y no funcionan en el teléfono de un amigo. Para los niños, saber qué hacer cuando algo aparece en la pantalla importa más que cualquier ajuste.</p>""",
    },
    "remove-background-music-from-videos": {
        "title": "Cómo quitar la música de fondo de los vídeos en tu navegador",
        "description": "Cómo la separación de voces en el dispositivo quita la música de fondo de los vídeos en línea y conserva el habla, dónde funciona bien y dónde le cuesta.",
        "body": """<p>Muchas charlas, documentales y noticias tienen música de fondo que quizá prefieras no oír. Silenciar no es una opción cuando quieres el habla. La separación de voces lo resuelve: un pequeño modelo de voz conserva las voces y quita el resto.</p>
<p>Los sabios difieren sobre la música, y este artículo no intenta zanjarlo. Solo explica lo que la tecnología puede hacer, para quien lo quiera.</p>
<h2>Cómo funciona</h2>
<p>Un modelo de voz escucha el sonido de un vídeo en fragmentos cortos y estima qué parte es una voz humana. El resto se quita antes de llegar a tus altavoces. Ejecutarlo en tu dispositivo significa que el audio no tiene que enviarse a ninguna parte.</p>
<h2>Cómo usarlo en AkhiBrowser</h2>
<ol>
<li>Instala AkhiBrowser en Windows o Android.</li>
<li>Reproduce un vídeo. No music está activado por defecto.</li>
<li>Para desactivarlo, abre el escudo de AkhiBrowser en la barra de herramientas. En Android: menú, luego Extensiones y luego AkhiBrowser.</li>
</ol>
<p>Los teléfonos y ordenadores más lentos usan un modelo más ligero, para poder seguir el ritmo.</p>
<h2>Dónde funciona peor</h2>
<ul>
<li><strong>El canto.</strong> Una voz que canta sigue siendo una voz, así que el modelo tiene que decidir qué hacer con ella.</li>
<li><strong>Música alta sobre una voz baja.</strong> Puede quedar algo de música, y la voz puede sonar más fina.</li>
<li><strong>Sitios que bloquean el acceso a su audio.</strong> Algunos vídeos protegidos no se pueden procesar.</li>
</ul>
<p>La función se basa en <a href="https://github.com/mohamedsadiqaguenaou/NoMusic">NoMusic de Mohamed Sadiq</a>.</p>""",
    },
    "parental-controls-for-muslim-families": {
        "title": "Control parental para familias musulmanas: una configuración sencilla",
        "description": "Una configuración sencilla para padres: un navegador con filtro, un PIN, sitios aprobados para niños pequeños, hora de dormir y horario escolar, y lo que ningún navegador puede controlar.",
        "body": """<p>Un buen control parental se adapta a la edad del niño. Estos son puntos de partida razonables, con el control parental de Family Premium en AkhiBrowser. Cada uno está desactivado hasta que lo activas, y los datos se quedan en el dispositivo.</p>
<h2>Primero, para todas las edades</h2>
<ol>
<li>Pon un PIN parental, para que las protecciones no se puedan desactivar sin él.</li>
<li>Activa <strong>Sin pestañas privadas</strong>, para que la navegación siga bajo control.</li>
<li>Quita los demás navegadores del dispositivo, o bloquéalos con Google Family Link o Microsoft Family Safety. Un navegador no puede controlar lo que pasa fuera de él.</li>
</ol>
<h2>Niños pequeños</h2>
<p>Usa <strong>Permitir solo sitios aprobados</strong> y añade los pocos sitios que usan. Todo lo demás queda cerrado, lo que es mucho más fuerte que intentar bloquear las partes malas de la web.</p>
<h2>Niños mayores</h2>
<p>Abre la web, pero pon límites. <strong>Bloquear sitios elegidos</strong> cubre sitios concretos que dan problemas, y <strong>Límites de tiempo</strong> fija un límite diario, la hora de dormir y el horario escolar. El <strong>Límite de feeds</strong> oculta los feeds de vídeos cortos y detiene las webs sociales tras un tiempo fijado. Funciona en webs dentro de AkhiBrowser, no en apps de redes sociales.</p>
<h2>Adolescentes</h2>
<p>La confianza crece con la edad. El <strong>Resumen de actividad</strong> muestra cuántas páginas se bloquearon y por qué, sin sus direcciones. Es un punto de partida para una conversación, no vigilancia.</p>
<h2>Cuando necesitas un descanso</h2>
<p><strong>Pausar internet</strong> detiene la navegación al instante, con el PIN para reanudar. Es útil a la hora de comer y en torno a la oración.</p>
<p>Consulta los <a href="/es/#premium">planes y precios</a>. Las protecciones gratuitas funcionan sin nada de esto.</p>""",
    },
    "why-prayer-times-differ": {
        "title": "Por qué los horarios de oración difieren entre apps y mezquitas",
        "description": "Por qué el Fajr y el Isha pueden diferir más de media hora entre apps: los métodos de cálculo explicados, con un ejemplo real de Almere, en los Países Bajos.",
        "body": """<p>Dos apps pueden mostrar horas distintas para la misma oración en la misma ciudad. Normalmente ninguna está rota: usan un método de cálculo diferente.</p>
<h2>Qué se mantiene y qué cambia</h2>
<p>El Dhuhr y el Maghrib siguen la posición del sol, así que los métodos coinciden casi siempre en ellos. El Fajr y el Isha dependen del crepúsculo, cuando el sol está a cierto ángulo bajo el horizonte, y los métodos eligen ángulos distintos. El Asr también varía según la escuela: la hora hanafí es más tardía que la estándar.</p>
<h2>Un ejemplo real</h2>
<p>Estas son las horas para Almere, en los Países Bajos, el 8 de noviembre de 2026, según el <a href="https://aladhan.com/prayer-times-api">servicio público de cálculo Aladhan</a>:</p>
<div class="table"><table>
<thead><tr><th scope="col">Método</th><th scope="col">Fajr</th><th scope="col">Isha</th></tr></thead>
<tbody>
<tr><th scope="row">Marruecos</th><td>05:43</td><td>18:48</td></tr>
<tr><th scope="row">Liga Mundial Musulmana</th><td>05:50</td><td>18:48</td></tr>
<tr><th scope="row">Karachi</th><td>05:50</td><td>18:55</td></tr>
<tr><th scope="row">Moonsighting Committee</th><td>06:09</td><td>18:26</td></tr>
<tr><th scope="row">ISNA</th><td>06:10</td><td>18:35</td></tr>
<tr><th scope="row">Francia (UOIF)</th><td>06:30</td><td>18:15</td></tr>
</tbody>
</table></div>
<p>Son 47 minutos entre el Fajr más temprano y el más tardío. Lejos del ecuador, las diferencias cambian con las estaciones, y en verano puede que no haya un crepúsculo real, así que los métodos también necesitan reglas para latitudes altas.</p>
<h2>¿Cuál deberías usar?</h2>
<p>Para una cuestión de práctica, pregunta en tu mezquita local o a un sabio de confianza, y sigue lo que usa tu comunidad. Una app solo puede hacer las cuentas.</p>
<h2>Horarios de oración en AkhiBrowser</h2>
<p>AkhiBrowser calcula los horarios de oración en tu dispositivo a partir de la ciudad que eliges, sin usar tu ubicación. Elige un método según el país, y puedes cambiar el método y la hora del Asr en sus opciones.</p>""",
    },
    "best-halal-browsers": {
        "title": "Los mejores navegadores halal de {YEAR}, comparados",
        "description": "Una comparación honesta de los navegadores halal que puedes usar en {YEAR}: AkhiBrowser, Kahf Browser y Tahir Browser, y qué pasó con SalamWeb. Plataformas, precio y funciones.",
        "body": """<p>Un navegador halal bloquea sitios haram, fuerza SafeSearch y mantiene las imágenes no deseadas fuera de tu pantalla. En {YEAR} hay tres opciones activas que conviene conocer. Una de ellas, AkhiBrowser, la hacemos nosotros, así que esta página se ciñe a lo que cada navegador dice en sus propias páginas, y dice claramente dónde encaja mejor cada uno.</p>
<h2>La respuesta corta</h2>
<ul>
<li><strong>En Windows, o para control parental:</strong> AkhiBrowser. Protecciones gratuitas, eliminación de la música de fondo y Family Premium con un PIN, listas de sitios y límites de tiempo.</li>
<li><strong>En un Mac, o para un navegador totalmente gratis en todas las plataformas:</strong> Kahf Browser. Windows, macOS, Android e iOS, gratis sin compras dentro de la app.</li>
<li><strong>En un iPhone:</strong> Tahir Browser o Kahf Browser. AkhiBrowser aún no está en iOS.</li>
</ul>
<h2>AkhiBrowser</h2>
<p>Un navegador halal basado en Firefox, para Windows y Android. Los sitios para adultos, de alcohol, drogas, vapeo y apuestas se bloquean desde la primera página, SafeSearch está forzado en Google, Bing, DuckDuckGo, Yahoo y YouTube, y las imágenes siguen difuminadas hasta comprobarse en tu dispositivo. Es el único de los tres que quita la música de fondo de los vídeos, en tu dispositivo. Las protecciones son gratuitas; Premium añade la elección de a quién difuminar, y Family Premium añade un PIN parental, listas de sitios, límites de tiempo y un botón de pausa.</p>
<h2>Kahf Browser</h2>
<p>Un navegador basado en Chromium para musulmanes en Windows, macOS, Android e iOS. Su web dice que es gratis en todas las plataformas sin suscripciones ni compras dentro de la app, bloquea anuncios y sitios para adultos y haram con filtrado por IA y una base de datos, fuerza SafeSearch y Safe YouTube, difumina desnudos en tiempo real e incluye horarios de oración y la qibla. La mayoría de las extensiones de Chrome funcionan en él.</p>
<h2>Tahir Browser</h2>
<p>Un navegador para iPhone y iPad de Ihya Tech. Su ficha en la App Store describe difuminar todas las imágenes o usar IA para difuminar al sexo opuesto, tocar para ver, bloquear sitios haram, anuncios y rastreadores, recordatorios islámicos, SafeSearch forzado y un bloqueo con contraseña o biometría en su escudo. Es gratis de descargar, con planes mensuales y anuales opcionales.</p>
<h2>¿Qué pasó con SalamWeb?</h2>
<p>SalamWeb fue uno de los primeros navegadores halal y tuvo mucha cobertura en prensa en 2019. Se abandonó en 2021 y su web ya no existe, así que ya no es una opción. Es un buen recordatorio para elegir un navegador que siga actualizándose, porque las actualizaciones traen correcciones de seguridad.</p>
<h2>Lado a lado</h2>
<div class="table"><table>
<thead><tr><th scope="col"></th><th scope="col">AkhiBrowser</th><th scope="col">Kahf Browser</th><th scope="col">Tahir Browser</th></tr></thead>
<tbody>
<tr><th scope="row">Plataformas</th><td>Windows, Android</td><td>Windows, macOS, Android, iOS</td><td>iPhone, iPad</td></tr>
<tr><th scope="row">Precio</th><td>Protecciones gratis; Premium opcional</td><td>Gratis</td><td>Gratis; planes opcionales</td></tr>
<tr><th scope="row">Basado en</th><td>Firefox</td><td>Chromium</td><td>iOS WebKit</td></tr>
<tr><th scope="row">Sitios haram bloqueados</th><td>Sí</td><td>Sí</td><td>Sí</td></tr>
<tr><th scope="row">SafeSearch forzado</th><td>Sí, incl. YouTube</td><td>Sí, incl. YouTube</td><td>Sí</td></tr>
<tr><th scope="row">Difuminado de imágenes</th><td>Hasta comprobarse, en tu dispositivo</td><td>En tiempo real</td><td>Todas las imágenes, o IA por sexo</td></tr>
<tr><th scope="row">Eliminación de música de fondo</th><td>Sí</td><td>No indicado</td><td>No indicado</td></tr>
<tr><th scope="row">PIN parental y límites de tiempo</th><td>Family Premium</td><td>No indicado</td><td>Bloqueo del escudo</td></tr>
</tbody>
</table></div>
<p>&quot;No indicado&quot; significa que no lo encontramos en las propias páginas del navegador, no que no exista. Para una tabla más larga, consulta <a href="/es/compare/kahf-browser/">AkhiBrowser y Kahf Browser comparados</a> y <a href="/es/compare/browsers/">AkhiBrowser, Kahf, Brave, Firefox y Chrome comparados</a>. ¿Nuevo en el tema? Empieza por <a href="/es/blog/what-is-a-halal-browser/">qué es un navegador halal</a>.</p>
<p>Comprobado con las propias páginas de cada navegador el 10 de noviembre de 2026. ¿Ves algo desactualizado? Dínoslo en <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>.</p>""",
    },
}

_NS = "No indicado"

COMPARE = {
    "seo_title": "AkhiBrowser frente a Kahf Browser: funciones, precio y plataformas comparados",
    "title": "AkhiBrowser y Kahf Browser comparados",
    "description": "AkhiBrowser y Kahf Browser lado a lado: precio, plataformas, filtrado, imágenes, eliminación de música, horarios de oración y control parental, según las propias páginas de cada navegador.",
    "lead": "Los dos son navegadores para musulmanes. Esta tabla recoge lo que cada uno dice en su propia web, a 8 de noviembre de 2026 para Kahf Browser y a 22 de noviembre de 2026 para AkhiBrowser. No hemos probado Kahf Browser nosotros mismos. &quot;No indicado&quot; significa que no lo encontramos en las páginas que leímos, no que la función no exista.",
    "head": ["", "AkhiBrowser", "Kahf Browser"],
    "rows": [
        ["Precio", "Protecciones gratis. Premium opcional por 3,99 € al mes, 39 € al año o 119 € una vez; Family Premium por 59,99 € al año", "Gratis en todas las plataformas, sin suscripciones ni compras dentro de la app"],
        ["Plataformas", "Windows (Microsoft Store), Android (Google Play). iOS y macOS: <a href=\"/es/#roadmap\">en la hoja de ruta</a>, aún sin fecha", "Windows, macOS, Android, iOS. Linux: su FAQ lo menciona, su página de descarga dice próximamente"],
        ["Sitios para adultos y haram", "Bloqueados: adultos, alcohol, drogas, vapeo y apuestas", "Bloqueados, con filtrado por IA y una base de datos"],
        ["Búsquedas haram", "Bloqueadas en 11 idiomas; las preguntas sobre ellas siguen permitidas", "Safe Search, incluidas las sugerencias de búsqueda"],
        ["Desnudos en imágenes", "Difuminados hasta comprobarse en tu dispositivo: imágenes, fondos, vídeo y lienzos; en vídeos en tiempo real: cada escena nueva se difumina y se comprueba al instante", "Difuminados en tiempo real"],
        ["SafeSearch", "Forzado en Google, Bing, DuckDuckGo y Yahoo, más el Modo restringido de YouTube", "Aplicado en los grandes buscadores; Safe YouTube"],
        ["PIN parental, listas de sitios, límites de tiempo", "Family Premium: PIN, sitios bloqueados o solo aprobados, hora de dormir y horario escolar, un límite diario", _NS],
        ["Informe para padres y resumen de actividad", "Family Premium: un correo cuando se desactiva una protección o el PIN, un resumen semanal de bloqueos por motivo y un resumen de 7 días en el dispositivo", _NS],
        ["Pausar internet", "Family Premium, con el PIN; el control parental puede pasar a otro dispositivo en un archivo bloqueado con el PIN", _NS],
        ["Feeds sociales y apps", "Family Premium: feeds de vídeos cortos ocultos, un límite diario en webs sociales, apps bloqueadas en Android", _NS],
        ["Quitar la música de fondo de los vídeos", "Gratis, en tu dispositivo", _NS],
        ["Anuncios y rastreadores", "Bloqueados, con uBlock Origin y un bloqueador integrado", "Bloqueador integrado"],
        ["Sitios de phishing y estafas", "Bloqueados", "Bloqueados"],
        ["Elegir a quién difuminar (mujeres, hombres)", "Premium", _NS],
        ["Reconocer el hiyab", "Premium", _NS],
        ["Modo estricto", "Premium: cada imagen y vídeo sigue difuminado hasta que lo tocas", _NS],
        ["YouTube", "Modo restringido, gratis. Premium: sin recomendaciones, Shorts ni reproducción automática. Family Premium: Deen Time, solo los canales que elegiste", "Safe YouTube"],
        ["Horarios de oración", "Gratis, para una ciudad que elijas, sin tu ubicación; recordatorios en ordenadores", "Horarios de oración y notificaciones"],
        ["Pausa de oración", "Family Premium: las webs sociales, de vídeo y de juegos se pausan unos minutos después de cada hora de oración", _NS],
        ["Comprobación halal y lugares halal", "Family Premium: un aviso en páginas de productos con cerdo, alcohol, gelatina o números E dudosos; lugares halal en Google Maps y webs de reparto", _NS],
        ["Aviso de riba, cajas de botín", "Family Premium: un aviso en páginas de préstamos con interés, tarjetas de crédito y «compra ahora, paga después»; sitios de apertura de cajas y apuestas de skins bloqueados", _NS],
        ["Recitación del Corán, fuentes fiables", "Family Premium: seguir una recitación en YouTube versículo a versículo con su significado; fuentes académicas primero al buscar sobre el islam", _NS],
        ["Versículo del día", "Gratis", _NS],
        ["Qibla", "Sí, en Android: una brújula bajo los horarios de oración", "Sí"],
        ["Idiomas", "12, entre ellos árabe, urdu, persa, kurdo y turco", _NS],
        ["Corrección del daltonismo", "Gratis, en tu dispositivo", _NS],
        ["Necesita cuenta", "No", "No; se puede iniciar sesión"],
        ["Basado en", "Firefox", "Chromium; funcionan la mayoría de las extensiones de Chrome"],
        ["Código fuente", "Los cambios en Firefox y los archivos MPL son públicos; su propia extensión es privada", "Aún no es público, según su FAQ"],
    ],
    "after": """<h2>¿Cuál te conviene?</h2>
<p><strong>Kahf Browser</strong> te conviene si usas un iPhone o un Mac, o quieres todo gratis.</p>
<p><strong>AkhiBrowser</strong> te conviene si quieres quitar la música de fondo, elegir a quién difuminar o necesitas control parental como un PIN, límites de tiempo y un informe por correo, en Windows o Android. Family Premium añade lo que Kahf no menciona: una comprobación halal mientras compras, un aviso de riba y una pausa después de cada oración.</p>
<p>Los dos son gratis para probar, así que la mejor prueba es tu propio uso. AkhiBrowser no está vinculado a Kahf. ¿Ves algo desactualizado? Dínoslo en <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a> y lo corregiremos.</p>""",
    "sources_label": "Las páginas de Kahf Browser que leímos:",
}

_CWS = "https://chromewebstore.google.com/detail/akhibrowser/ghkpflipnhahpjdnpoclaakbecnopamk"
_AMO = "https://addons.mozilla.org/en-US/firefox/addon/akhibrowser/"
_ALL5 = "Windows, macOS, Linux, Android, iOS"

COMPARE_BROWSERS = {
    "seo_title": "Comparativa de navegadores halal: AkhiBrowser, Kahf Browser, Brave, Firefox y Chrome",
    "title": "AkhiBrowser, Kahf Browser, Brave, Firefox y Chrome comparados",
    "description": "¿Qué navegador filtra el contenido haram, difumina imágenes, quita la música de fondo y tiene control parental? AkhiBrowser, Kahf Browser, Brave, Firefox y Chrome lado a lado.",
    "lead": "Lo que hace cada navegador de serie, sin extensiones, tal como cada uno lo describe en sus propias páginas, a 9 de noviembre de 2026, y a 15 de noviembre de 2026 para AkhiBrowser. No hemos probado Kahf Browser nosotros mismos; consulta <a href=\"/es/compare/kahf-browser/\">la comparación detallada con Kahf Browser</a>.",
    "head": ["", "AkhiBrowser", "Kahf Browser", "Brave", "Firefox", "Chrome"],
    "rows": [
        ["Precio", "Protecciones gratis; Premium y Family Premium opcionales", "Gratis", "Gratis", "Gratis", "Gratis"],
        ["Plataformas", f"Windows (Microsoft Store), Android (Google Play); extensiones gratuitas más ligeras para <a href=\"{_CWS}\">Chrome</a> y <a href=\"{_AMO}\">Firefox</a>", "Windows, macOS, Android, iOS", _ALL5, _ALL5, _ALL5],
        ["Sitios para adultos y haram", "Bloqueados, desde la primera página", "Bloqueados", "No", "No", "No"],
        ["Búsquedas haram bloqueadas", "Sí, en 11 idiomas", "Safe Search, incluidas las sugerencias", "No", "No", "No"],
        ["Desnudos en imágenes", "Difuminados hasta comprobarse en tu dispositivo", "Difuminados", "No", "No", "No"],
        ["SafeSearch y Modo restringido de YouTube forzados", "Sí", "Sí", "No", "No", "Con supervisión de Family Link"],
        ["Control parental (PIN, listas de sitios, límites de tiempo)", "Family Premium", _NS, "No", "No", "Con Google Family Link"],
        ["Informe para padres", "Family Premium, por correo", _NS, "No", "No", "Con Google Family Link"],
        ["Un niño puede desactivar las protecciones", "No con el PIN parental", _NS, "Sí", "Sí", "Depende de Family Link"],
        ["Quitar la música de fondo de los vídeos", "Gratis, en tu dispositivo", _NS, "No", "No", "No"],
        ["Anuncios y rastreadores", "Bloqueados, uBlock Origin integrado", "Bloqueados", "Bloqueados (Shields)", "Rastreadores bloqueados; los anuncios necesitan una extensión", "No bloqueados; los bloqueadores de anuncios están limitados"],
        ["Elegir a quién difuminar, reconocer el hiyab", "Premium", _NS, "No", "No", "No"],
        ["YouTube más tranquilo", "Premium: sin recomendaciones, Shorts ni reproducción automática", "Safe YouTube", "No", "No", "No"],
        ["Horarios de oración y versículo del día", "Gratis", "Horarios de oración", "No", "No", "No"],
        ["Comprobación halal, aviso de riba, pausa de oración", "Family Premium", _NS, "No", "No", "No"],
        ["Basado en", "Firefox", "Chromium", "Chromium", "Motor propio de Firefox", "Chromium"],
    ],
    "after": """<h2>En resumen</h2>
<p><strong>Brave, Firefox y Chrome</strong> son buenos navegadores generales, pero ninguno filtra el contenido haram ni difumina imágenes por sí solo. Necesitarías extensiones, que un niño puede quitar.</p>
<p><strong>Kahf Browser y AkhiBrowser</strong> están hechos para musulmanes y filtran desde el principio. AkhiBrowser añade la eliminación de la música de fondo, elegir a quién difuminar, control parental con PIN e informe por correo, y una comprobación halal, un aviso de riba y una pausa de oración.</p>
<p>¿Ves algo desactualizado? Dínoslo en <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a> y lo corregiremos. AkhiBrowser no está vinculado a ninguno de estos navegadores.</p>""",
    "sources_label": "Páginas que leímos:",
}
