"""The French text of the blog and comparison pages. content.py merges it in; see build_pages.py and langs.py.

Each key in ARTICLES is an article slug from content.py. {YEAR} stands for the current year."""

UI = {
    "nav_label": "Menu principal",
    "blog": "Blog",
    "compare": "Comparer",
    "download": "Obtenir AkhiBrowser",
    "blog_title": "Guides de navigation halal",
    "blog_lead": "Des guides pratiques pour naviguer sur le web avec moins de publicités, moins de contenu haram et plus de contrôle, sur ton propre appareil.",
    "cta_title": "Obtenir AkhiBrowser",
    "cta_text": "Un navigateur privé pour les musulmans, basé sur Firefox. Sur le Microsoft Store pour Windows et sur Google Play pour Android. Les protections sont gratuites.",
    "footer": "AkhiBrowser est basé sur <a href=\"https://www.firefox.com/\">Firefox</a>, et n'est ni fait ni soutenu par Mozilla. Les filtres peuvent laisser passer des choses, et ils ne remplacent pas l'attention des parents. <a href=\"/fr/\">Accueil</a> · <a href=\"/fr/faq/\">Questions fréquentes</a> · <a href=\"mailto:support@akhibrowser.com\">support@akhibrowser.com</a>",
}

ARTICLES = {
    "what-is-a-halal-browser": {
        "title": "Qu'est-ce qu'un navigateur halal, et en as-tu besoin ?",
        "description": "Ce que fait un navigateur halal, ce qu'il ne peut pas faire et comment en choisir un : blocage de sites, SafeSearch, floutage des images et confidentialité expliqués.",
        "body": """<p>Un navigateur halal est un navigateur web qui filtre ce qu'un navigateur normal te laisse gérer. Il bloque les sites et les recherches de choses comme le contenu pour adultes, l'alcool et les jeux d'argent, et il garde les images indésirables loin de ton écran.</p>
<h2>Ce que fait généralement un navigateur halal</h2>
<ul>
<li><strong>Il bloque des sites.</strong> Les sites pour adultes, de jeux d'argent, d'alcool et de drogues s'arrêtent avant de se charger.</li>
<li><strong>Il impose SafeSearch.</strong> Les moteurs de recherche masquent les résultats explicites, sans que tu aies à le configurer.</li>
<li><strong>Il filtre les images.</strong> Les images montrant de la nudité sont floutées.</li>
<li><strong>Il bloque publicités et traqueurs.</strong> Beaucoup d'images indésirables arrivent par la publicité, donc cela aide deux fois.</li>
</ul>
<h2>Ce qu'il ne peut pas faire</h2>
<p>Aucun filtre n'est parfait. Certaines pages passent, et certaines pages inoffensives sont bloquées. Un navigateur ne protège aussi que ce qui se passe dans ce navigateur : les autres applications et navigateurs du même appareil ne sont pas couverts. Il aide l'intention et l'habitude, mais ne les remplace pas, ni l'attention des parents.</p>
<h2>Comment en choisir un</h2>
<ul>
<li><strong>Où se fait la vérification ?</strong> Filtrer sur ton propre appareil signifie que tes images n'ont pas à le quitter.</li>
<li><strong>Qu'est-ce qui quitte ton appareil ?</strong> Cherche une liste claire. Un navigateur qui dit « rien » doit pouvoir expliquer comment il bloque les sites et se met à jour.</li>
<li><strong>Peux-tu le contrôler ?</strong> Tu dois pouvoir voir et modifier chaque protection.</li>
<li><strong>Fonctionne-t-il sur tes appareils ?</strong> Vérifie avant de t'engager, surtout sur un iPhone ou un Mac.</li>
</ul>
<h2>Navigateur halal, extension ou filtre DNS ?</h2>
<p>Il existe trois façons courantes de filtrer le web, et elles fonctionnent mieux ensemble :</p>
<ul>
<li><strong>Un navigateur halal</strong> filtre dans le navigateur lui-même : sites, recherches, images et vidéos. Ses protections sont actives dès la première page et peuvent être verrouillées par un PIN.</li>
<li><strong>Une extension de navigateur</strong> ajoute un filtre à un navigateur que tu utilises déjà, comme Chrome. C'est rapide à essayer, mais on peut généralement la supprimer ou la désactiver, et elle ne peut pas changer le fonctionnement du navigateur lui-même.</li>
<li><strong>Un filtre DNS ou sur le routeur</strong> bloque des sites entiers pour toutes les applications d'un appareil ou d'un réseau. Il ne peut pas regarder à l'intérieur d'une page, donc il ne peut ni flouter une image ni retirer la musique d'une vidéo.</li>
</ul>
<p>Pour une famille, une configuration courante est un DNS familial sur le routeur plus un navigateur halal sur chaque appareil, avec les autres navigateurs supprimés ou bloqués. Lis <a href="/fr/blog/block-haram-content/">comment bloquer le contenu haram sur ton téléphone et ton ordinateur</a> pour la configuration complète.</p>
<h2>Une liste pour choisir un navigateur halal</h2>
<ul>
<li>Les sites pour adultes, de jeux d'argent, d'alcool et de drogues sont-ils bloqués dès la première page, sans configuration ?</li>
<li>SafeSearch est-il imposé sur chaque moteur de recherche, YouTube compris ?</li>
<li>Les images sont-elles vérifiées sur ton appareil, ou envoyées à un serveur ?</li>
<li>Un parent peut-il verrouiller les réglages avec un PIN ?</li>
<li>Dit-il clairement ce qui quitte ton appareil ?</li>
<li>Est-il encore mis à jour ? Un navigateur qui ne reçoit plus de mises à jour ne reçoit plus non plus de correctifs de sécurité. SalamWeb, l'un des premiers navigateurs halal, a été arrêté en 2021.</li>
</ul>
<p>Nous comparons les options dans <a href="/fr/blog/best-halal-browsers/">les meilleurs navigateurs halal en {YEAR}</a>.</p>
<h2>Questions fréquentes</h2>
<h3>Un navigateur halal est-il seulement pour les musulmans ?</h3>
<p>Non. Toute personne qui veut moins de publicités, pas de contenu pour adultes et plus de contrôle sur les images peut en utiliser un. Le nom décrit les valeurs sur lesquelles il est construit.</p>
<h3>Un navigateur halal est-il gratuit ?</h3>
<p>Beaucoup le sont. Les protections d'AkhiBrowser sont gratuites, avec un Premium facultatif pour plus de réglages d'image et des outils pour les parents.</p>
<h3>Un navigateur halal remplace-t-il le contrôle parental ?</h3>
<p>Il couvre le navigateur. Pour les applications et les autres navigateurs, combine-le avec les contrôles de l'appareil, comme Google Family Link ou Microsoft Family Safety. Vois <a href="/fr/blog/parental-controls-for-muslim-families/">une configuration simple du contrôle parental</a>.</p>
<h3>Un navigateur halal peut-il retirer la musique des vidéos ?</h3>
<p>Certains le peuvent. AkhiBrowser <a href="/fr/blog/remove-background-music-from-videos/">retire la musique de fond sur ton appareil</a>, pour que les voix restent et que la musique parte.</p>
<p>AkhiBrowser est une option, basée sur Firefox pour Windows et Android. Ses protections sont actives dès la première page, et <a href="/fr/privacy/">son site liste ce qui quitte ton appareil</a>. Tu peux aussi lire <a href="/fr/compare/kahf-browser/">comment il se compare à Kahf Browser</a>.</p>""",
    },
    "block-haram-content": {
        "title": "Comment bloquer le contenu haram sur ton téléphone et ton ordinateur",
        "description": "Une méthode pas à pas pour bloquer le contenu pour adultes, les jeux d'argent et l'alcool : filtres de navigateur, SafeSearch, DNS familial et contrôles de l'appareil, et ce que chacun laisse passer.",
        "body": """<p>Aucun réglage seul ne bloque tout. Ce qui marche, ce sont quelques couches, chacune couvrant ce que les autres laissent passer.</p>
<h2>1. Utilise un navigateur qui filtre par défaut</h2>
<p>Un navigateur filtrant bloque les sites, filtre les recherches et floute les images sans configuration. Dans AkhiBrowser, les sites pour adultes, d'alcool, de drogues, de vapotage et de jeux d'argent sont bloqués dès la première page.</p>
<h2>2. Impose SafeSearch</h2>
<p>SafeSearch masque les résultats explicites dans les moteurs de recherche. Tu peux l'activer dans les réglages de chaque moteur, mais il se désactive facilement, et il ne vaut que pour un navigateur. Un navigateur filtrant peut l'imposer : AkhiBrowser le fait sur Google, Bing, DuckDuckGo et Yahoo, et active le mode restreint de YouTube.</p>
<h2>3. Ajoute un DNS familial</h2>
<p>Un service de DNS familial refuse de chercher les sites pour adultes, pour tout ce qui se trouve sur ce réseau ou cet appareil. Le 1.1.1.3 de Cloudflare et CleanBrowsing sont des options connues. Il fonctionne par nom de site, donc il ne voit pas ce qu'il y a sur un site autorisé, et celui qui le gère voit les noms des sites que tu visites.</p>
<h2>4. Ferme les portes dérobées</h2>
<p>Un filtre de navigateur ne couvre pas les autres applications. Sur l'appareil d'un enfant, utilise Google Family Link sur Android ou Microsoft Family Safety sur Windows pour contrôler quelles applications et quels navigateurs peuvent être installés. Dans AkhiBrowser, Family Premium peut aussi verrouiller les réglages avec un PIN et désactiver les onglets privés.</p>
<h2>5. Continue la conversation</h2>
<p>Les filtres laissent passer des choses, et ils ne fonctionnent pas sur le téléphone d'un ami. Pour les enfants, savoir quoi faire quand quelque chose apparaît à l'écran compte plus que n'importe quel réglage.</p>""",
    },
    "remove-background-music-from-videos": {
        "title": "Comment retirer la musique de fond des vidéos dans ton navigateur",
        "description": "Comment la séparation des voix sur l'appareil retire la musique de fond des vidéos en ligne et garde la parole, où elle fonctionne bien, et où elle a du mal.",
        "body": """<p>Beaucoup de conférences, de documentaires et de reportages ont une musique de fond que tu préfères peut-être ne pas entendre. Couper le son n'est pas une option quand tu veux entendre la parole. La séparation des voix règle cela : un petit modèle vocal garde les voix et retire le reste.</p>
<p>Les savants divergent sur la musique, et cet article ne cherche pas à trancher. Il explique seulement ce que la technologie peut faire, pour ceux qui le veulent.</p>
<h2>Comment ça marche</h2>
<p>Un modèle vocal écoute le son d'une vidéo par courtes tranches et estime quelle partie est une voix humaine. Le reste est retiré avant d'atteindre tes haut-parleurs. Le faire tourner sur ton appareil signifie que le son n'a besoin d'être envoyé nulle part.</p>
<h2>Comment l'utiliser dans AkhiBrowser</h2>
<ol>
<li>Installe AkhiBrowser sur Windows ou Android.</li>
<li>Lance une vidéo. No music est activé par défaut.</li>
<li>Pour le désactiver, ouvre le bouclier AkhiBrowser dans la barre d'outils. Sur Android : menu, puis Extensions, puis AkhiBrowser.</li>
</ol>
<p>Les téléphones et les ordinateurs plus lents utilisent un modèle plus léger, pour suivre le rythme.</p>
<h2>Où ça marche moins bien</h2>
<ul>
<li><strong>Le chant.</strong> Une voix qui chante reste une voix, donc le modèle doit décider quoi en faire.</li>
<li><strong>Une musique forte sur une parole douce.</strong> Un peu de musique peut rester, et la voix peut sembler plus fine.</li>
<li><strong>Les sites qui bloquent l'accès à leur son.</strong> Certaines vidéos protégées ne peuvent pas être traitées.</li>
</ul>
<p>La fonction s'appuie sur <a href="https://github.com/mohamedsadiqaguenaou/NoMusic">NoMusic de Mohamed Sadiq</a>.</p>""",
    },
    "parental-controls-for-muslim-families": {
        "title": "Contrôle parental pour les familles musulmanes : une configuration simple",
        "description": "Une configuration simple pour les parents : un navigateur filtrant, un PIN, des sites approuvés pour les jeunes enfants, le coucher et les heures d'école, et ce qu'aucun navigateur ne peut contrôler.",
        "body": """<p>Un bon contrôle parental s'adapte à l'âge de l'enfant. Voici des points de départ raisonnables, avec le contrôle parental de Family Premium dans AkhiBrowser. Chacun est désactivé jusqu'à ce que tu l'actives, et les données restent sur l'appareil.</p>
<h2>D'abord, pour tous les âges</h2>
<ol>
<li>Définis un PIN parental, pour que les protections ne puissent pas être désactivées sans lui.</li>
<li>Active <strong>Pas d'onglets privés</strong>, pour que la navigation reste sous contrôle.</li>
<li>Supprime les autres navigateurs de l'appareil, ou bloque-les avec Google Family Link ou Microsoft Family Safety. Un navigateur ne peut pas contrôler ce qui se passe en dehors de lui.</li>
</ol>
<h2>Jeunes enfants</h2>
<p>Utilise <strong>Autoriser seulement les sites approuvés</strong> et ajoute les quelques sites qu'ils utilisent. Tout le reste reste fermé, ce qui est bien plus solide que d'essayer de bloquer les mauvais coins du web.</p>
<h2>Enfants plus grands</h2>
<p>Ouvre le web, mais fixe des limites. <strong>Bloquer des sites choisis</strong> couvre des sites précis qui posent problème, et <strong>Limites de temps</strong> fixe une limite quotidienne, le coucher et les heures d'école. La <strong>Limite des fils</strong> masque les fils de vidéos courtes et arrête les sites sociaux après un temps fixé. Elle fonctionne sur les sites web dans AkhiBrowser, pas dans les applications de réseaux sociaux.</p>
<h2>Adolescents</h2>
<p>La confiance grandit avec l'âge. Le <strong>Résumé d'activité</strong> montre combien de pages ont été bloquées et pourquoi, sans leurs adresses. C'est un point de départ pour une conversation, pas de la surveillance.</p>
<h2>Quand tu as besoin d'une pause</h2>
<p><strong>Mettre internet en pause</strong> arrête la navigation tout de suite, avec le PIN pour reprendre. C'est utile aux repas et autour de la prière.</p>
<p>Vois les <a href="/fr/#premium">formules et prix</a>. Les protections gratuites fonctionnent sans tout cela.</p>""",
    },
    "why-prayer-times-differ": {
        "title": "Pourquoi les heures de prière diffèrent entre applications et mosquées",
        "description": "Pourquoi Fajr et Isha peuvent différer de plus d'une demi-heure entre applications : les méthodes de calcul expliquées, avec un exemple réel à Almere, aux Pays-Bas.",
        "body": """<p>Deux applications peuvent afficher des heures différentes pour la même prière dans la même ville. En général, aucune n'est cassée : elles utilisent une méthode de calcul différente.</p>
<h2>Ce qui reste pareil, et ce qui change</h2>
<p>Dhuhr et Maghrib suivent la position du soleil, donc les méthodes s'accordent surtout sur elles. Fajr et Isha dépendent du crépuscule, quand le soleil est à un certain angle sous l'horizon, et les méthodes choisissent des angles différents. Asr diffère aussi selon l'école : l'heure hanafite est plus tardive que l'heure standard.</p>
<h2>Un exemple réel</h2>
<p>Voici les heures pour Almere, aux Pays-Bas, le 8 novembre 2026, d'après le <a href="https://aladhan.com/prayer-times-api">service de calcul public Aladhan</a> :</p>
<div class="table"><table>
<thead><tr><th scope="col">Méthode</th><th scope="col">Fajr</th><th scope="col">Isha</th></tr></thead>
<tbody>
<tr><th scope="row">Maroc</th><td>05:43</td><td>18:48</td></tr>
<tr><th scope="row">Ligue islamique mondiale</th><td>05:50</td><td>18:48</td></tr>
<tr><th scope="row">Karachi</th><td>05:50</td><td>18:55</td></tr>
<tr><th scope="row">Moonsighting Committee</th><td>06:09</td><td>18:26</td></tr>
<tr><th scope="row">ISNA</th><td>06:10</td><td>18:35</td></tr>
<tr><th scope="row">France (UOIF)</th><td>06:30</td><td>18:15</td></tr>
</tbody>
</table></div>
<p>Cela fait 47 minutes entre le Fajr le plus tôt et le plus tard. Loin de l'équateur, les écarts changent avec les saisons, et en été le vrai crépuscule peut ne pas avoir lieu du tout, donc les méthodes ont aussi besoin de règles pour les hautes latitudes.</p>
<h2>Laquelle utiliser ?</h2>
<p>Pour une question de pratique, demande à ta mosquée locale ou à un savant de confiance, et suis ce qu'utilise ta communauté. Une application ne peut que faire les calculs.</p>
<h2>Les heures de prière dans AkhiBrowser</h2>
<p>AkhiBrowser calcule les heures de prière sur ton appareil à partir de la ville que tu choisis, sans utiliser ta position. Il choisit une méthode selon le pays, et tu peux changer la méthode et l'heure d'Asr dans ses options.</p>""",
    },
    "best-halal-browsers": {
        "title": "Les meilleurs navigateurs halal en {YEAR}, comparés",
        "description": "Une comparaison honnête des navigateurs halal utilisables en {YEAR} : AkhiBrowser, Kahf Browser et Tahir Browser, et ce qu'est devenu SalamWeb. Plateformes, prix et fonctions.",
        "body": """<p>Un navigateur halal bloque les sites haram, impose SafeSearch et garde les images indésirables loin de ton écran. En {YEAR}, il y a trois options actives à connaître. Nous faisons l'une d'elles, AkhiBrowser, donc cette page s'en tient à ce que chaque navigateur indique sur ses propres pages, et dit clairement où chacun convient le mieux.</p>
<h2>La réponse courte</h2>
<ul>
<li><strong>Sous Windows, ou pour le contrôle parental :</strong> AkhiBrowser. Protections gratuites, suppression de la musique de fond, et Family Premium avec un PIN, des listes de sites et des limites de temps.</li>
<li><strong>Sur un Mac, ou pour un navigateur entièrement gratuit sur toutes les plateformes :</strong> Kahf Browser. Windows, macOS, Android et iOS, gratuit sans achats intégrés.</li>
<li><strong>Sur un iPhone :</strong> Tahir Browser ou Kahf Browser. AkhiBrowser n'est pas encore sur iOS.</li>
</ul>
<h2>AkhiBrowser</h2>
<p>Un navigateur halal basé sur Firefox, pour Windows et Android. Les sites pour adultes, d'alcool, de drogues, de vapotage et de jeux d'argent sont bloqués dès la première page, SafeSearch est imposé sur Google, Bing, DuckDuckGo, Yahoo et YouTube, et les images restent floues jusqu'à leur vérification sur ton appareil. C'est le seul des trois qui retire la musique de fond des vidéos, sur ton appareil. Les protections sont gratuites ; Premium ajoute le choix de qui est flouté, et Family Premium ajoute un PIN parental, des listes de sites, des limites de temps et un bouton de pause.</p>
<h2>Kahf Browser</h2>
<p>Un navigateur basé sur Chromium pour les musulmans, sous Windows, macOS, Android et iOS. Son site dit qu'il est gratuit sur toutes les plateformes sans abonnements ni achats intégrés, qu'il bloque les publicités et les sites pour adultes et haram avec un filtrage par IA et une base de données, impose SafeSearch et Safe YouTube, floute la nudité en temps réel, et inclut les heures de prière et la qibla. La plupart des extensions Chrome y fonctionnent.</p>
<h2>Tahir Browser</h2>
<p>Un navigateur pour iPhone et iPad d'Ihya Tech. Sa fiche sur l'App Store décrit le floutage de toutes les images ou, par IA, du sexe opposé, un toucher pour déflouter, le blocage des sites haram, des publicités et des traqueurs, des rappels islamiques, SafeSearch imposé et un verrou par mot de passe ou biométrie sur son bouclier. Il est gratuit à télécharger, avec des formules mensuelles et annuelles facultatives.</p>
<h2>Qu'est devenu SalamWeb ?</h2>
<p>SalamWeb a été l'un des premiers navigateurs halal et a eu une large couverture de presse en 2019. Il a été arrêté en 2021 et son site a disparu, donc ce n'est plus une option. C'est un bon rappel de choisir un navigateur encore mis à jour, car les mises à jour apportent des correctifs de sécurité.</p>
<h2>Côte à côte</h2>
<div class="table"><table>
<thead><tr><th scope="col"></th><th scope="col">AkhiBrowser</th><th scope="col">Kahf Browser</th><th scope="col">Tahir Browser</th></tr></thead>
<tbody>
<tr><th scope="row">Plateformes</th><td>Windows, Android</td><td>Windows, macOS, Android, iOS</td><td>iPhone, iPad</td></tr>
<tr><th scope="row">Prix</th><td>Protections gratuites ; Premium facultatif</td><td>Gratuit</td><td>Gratuit ; formules facultatives</td></tr>
<tr><th scope="row">Basé sur</th><td>Firefox</td><td>Chromium</td><td>iOS WebKit</td></tr>
<tr><th scope="row">Sites haram bloqués</th><td>Oui</td><td>Oui</td><td>Oui</td></tr>
<tr><th scope="row">SafeSearch imposé</th><td>Oui, YouTube compris</td><td>Oui, YouTube compris</td><td>Oui</td></tr>
<tr><th scope="row">Floutage des images</th><td>Jusqu'à vérification, sur ton appareil</td><td>En temps réel</td><td>Toutes les images, ou IA selon le sexe</td></tr>
<tr><th scope="row">Suppression de la musique de fond</th><td>Oui</td><td>Non indiqué</td><td>Non indiqué</td></tr>
<tr><th scope="row">PIN parental et limites de temps</th><td>Family Premium</td><td>Non indiqué</td><td>Verrou du bouclier</td></tr>
</tbody>
</table></div>
<p>&quot;Non indiqué&quot; signifie que nous ne l'avons pas trouvé sur les propres pages du navigateur, pas que cela n'existe pas. Pour un tableau plus long, vois <a href="/fr/compare/kahf-browser/">AkhiBrowser et Kahf Browser comparés</a> et <a href="/fr/compare/browsers/">AkhiBrowser, Kahf, Brave, Firefox et Chrome comparés</a>. Nouveau sur le sujet ? Commence par <a href="/fr/blog/what-is-a-halal-browser/">ce qu'est un navigateur halal</a>.</p>
<p>Vérifié sur les propres pages de chaque navigateur le 10 novembre 2026. Tu as repéré quelque chose de dépassé ? Dis-le-nous à <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>.</p>""",
    },
}

_NS = "Non indiqué"

COMPARE = {
    "seo_title": "AkhiBrowser ou Kahf Browser : fonctions, prix et plateformes comparés",
    "title": "AkhiBrowser et Kahf Browser comparés",
    "description": "AkhiBrowser et Kahf Browser côte à côte : prix, plateformes, filtrage, images, suppression de la musique, heures de prière et contrôle parental, d'après les propres pages de chaque navigateur.",
    "lead": "Les deux sont des navigateurs pour les musulmans. Ce tableau liste ce que chacun indique sur son propre site, au 8 novembre 2026 pour Kahf Browser et au 22 novembre 2026 pour AkhiBrowser. Nous n'avons pas testé Kahf Browser nous-mêmes. &quot;Non indiqué&quot; signifie que nous ne l'avons pas trouvé sur les pages lues, pas que la fonction n'existe pas.",
    "head": ["", "AkhiBrowser", "Kahf Browser"],
    "rows": [
        ["Prix", "Protections gratuites. Premium facultatif à 3,99 € par mois, 39 € par an ou 119 € une fois ; Family Premium à 59,99 € par an", "Gratuit sur toutes les plateformes, sans abonnements ni achats intégrés"],
        ["Plateformes", "Windows (Microsoft Store), Android (Google Play). iOS et macOS : <a href=\"/fr/#roadmap\">sur la feuille de route</a>, sans date pour l'instant", "Windows, macOS, Android, iOS. Linux : sa FAQ le mentionne, sa page de téléchargement dit bientôt"],
        ["Sites pour adultes et haram", "Bloqués : adultes, alcool, drogues, vapotage et jeux d'argent", "Bloqués, avec un filtrage par IA et une base de données"],
        ["Recherches haram", "Bloquées dans 11 langues ; les questions à leur sujet restent permises", "Safe Search, suggestions de recherche comprises"],
        ["Nudité dans les images", "Floutée jusqu'à vérification sur ton appareil : images, arrière-plans, vidéos et canevas ; dans les vidéos en temps réel : chaque nouvelle scène est floutée et vérifiée aussitôt", "Floutée en temps réel"],
        ["SafeSearch", "Imposé sur Google, Bing, DuckDuckGo et Yahoo, plus le mode restreint de YouTube", "Imposé sur les grands moteurs de recherche ; Safe YouTube"],
        ["PIN parental, listes de sites, limites de temps", "Family Premium : PIN, sites bloqués ou seulement approuvés, coucher et heures d'école, une limite quotidienne", _NS],
        ["Rapport aux parents et résumé d'activité", "Family Premium : un e-mail quand une protection ou le PIN est désactivé, un résumé hebdomadaire des blocages par motif, et un résumé sur 7 jours sur l'appareil", _NS],
        ["Mettre internet en pause", "Family Premium, avec le PIN ; le contrôle parental peut passer à un autre appareil dans un fichier verrouillé par le PIN", _NS],
        ["Réseaux sociaux et applications", "Family Premium : fils de vidéos courtes masqués, une limite quotidienne sur les sites sociaux, applications bloquées sur Android", _NS],
        ["Retirer la musique de fond des vidéos", "Gratuit, sur ton appareil", _NS],
        ["Publicités et traqueurs", "Bloqués, avec uBlock Origin et un bloqueur intégré", "Bloqueur intégré"],
        ["Sites d'hameçonnage et d'arnaque", "Bloqués", "Bloqués"],
        ["Choisir qui flouter (femmes, hommes)", "Premium", _NS],
        ["Reconnaître le hijab", "Premium", _NS],
        ["Mode strict", "Premium : chaque image et vidéo reste floue jusqu'à ce que tu la touches", _NS],
        ["YouTube", "Mode restreint, gratuit. Premium : pas de recommandations, de Shorts ni de lecture automatique. Family Premium : Deen Time, seulement les chaînes choisies", "Safe YouTube"],
        ["Heures de prière", "Gratuit, pour une ville de ton choix, sans ta position ; rappels sur ordinateur", "Heures de prière et notifications"],
        ["Pause prière", "Family Premium : les sites sociaux, de vidéos et de jeux se mettent en pause quelques minutes après chaque heure de prière", _NS],
        ["Vérification halal et lieux halal", "Family Premium : un avertissement sur les pages de produits avec porc, alcool, gélatine ou additifs E douteux ; lieux halal sur Google Maps et les sites de livraison", _NS],
        ["Alerte riba, loot boxes", "Family Premium : un avertissement sur les pages de prêts à intérêt, de cartes de crédit et de paiement fractionné ; sites d'ouverture de caisses et de paris sur skins bloqués", _NS],
        ["Récitation du Coran, sources fiables", "Family Premium : suivre une récitation sur YouTube verset par verset avec son sens ; sources savantes en premier quand tu cherches sur l'islam", _NS],
        ["Verset du jour", "Gratuit", _NS],
        ["Qibla", "Oui, sur Android : une boussole sous les heures de prière", "Oui"],
        ["Langues", "12, dont l'arabe, l'ourdou, le persan, le kurde et le turc", _NS],
        ["Correction du daltonisme", "Gratuite, sur ton appareil", _NS],
        ["Compte nécessaire", "Non", "Non ; connexion possible"],
        ["Basé sur", "Firefox", "Chromium ; la plupart des extensions Chrome fonctionnent"],
        ["Code source", "Les modifications de Firefox et les fichiers MPL sont publics ; sa propre extension est privée", "Pas encore public, selon sa FAQ"],
    ],
    "after": """<h2>Lequel te convient ?</h2>
<p><strong>Kahf Browser</strong> te convient si tu utilises un iPhone ou un Mac, ou si tu veux tout gratuitement.</p>
<p><strong>AkhiBrowser</strong> te convient si tu veux retirer la musique de fond, choisir qui est flouté, ou si tu as besoin d'un contrôle parental comme un PIN, des limites de temps et un rapport par e-mail, sous Windows ou Android. Family Premium ajoute ce que Kahf ne mentionne pas : une vérification halal pendant tes achats, une alerte riba et une pause après chaque prière.</p>
<p>Les deux sont gratuits à essayer, donc le meilleur test est ton propre usage. AkhiBrowser n'est pas affilié à Kahf. Tu as repéré quelque chose de dépassé ? Dis-le-nous à <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a> et nous le corrigerons.</p>""",
    "sources_label": "Les pages de Kahf Browser que nous avons lues :",
}

_CWS = "https://chromewebstore.google.com/detail/akhibrowser/ghkpflipnhahpjdnpoclaakbecnopamk"
_AMO = "https://addons.mozilla.org/en-US/firefox/addon/akhibrowser/"
_ALL5 = "Windows, macOS, Linux, Android, iOS"

COMPARE_BROWSERS = {
    "seo_title": "Comparatif des navigateurs halal : AkhiBrowser, Kahf Browser, Brave, Firefox et Chrome",
    "title": "AkhiBrowser, Kahf Browser, Brave, Firefox et Chrome comparés",
    "description": "Quel navigateur filtre le contenu haram, floute les images, retire la musique de fond et offre un contrôle parental ? AkhiBrowser, Kahf Browser, Brave, Firefox et Chrome côte à côte.",
    "lead": "Ce que fait chaque navigateur d'origine, sans extensions, tel que chacun le décrit sur ses propres pages, au 9 novembre 2026, et au 15 novembre 2026 pour AkhiBrowser. Nous n'avons pas testé Kahf Browser nous-mêmes ; vois <a href=\"/fr/compare/kahf-browser/\">la comparaison détaillée avec Kahf Browser</a>.",
    "head": ["", "AkhiBrowser", "Kahf Browser", "Brave", "Firefox", "Chrome"],
    "rows": [
        ["Prix", "Protections gratuites ; Premium et Family Premium facultatifs", "Gratuit", "Gratuit", "Gratuit", "Gratuit"],
        ["Plateformes", f"Windows (Microsoft Store), Android (Google Play) ; extensions gratuites plus légères pour <a href=\"{_CWS}\">Chrome</a> et <a href=\"{_AMO}\">Firefox</a>", "Windows, macOS, Android, iOS", _ALL5, _ALL5, _ALL5],
        ["Sites pour adultes et haram", "Bloqués, dès la première page", "Bloqués", "Non", "Non", "Non"],
        ["Recherches haram bloquées", "Oui, dans 11 langues", "Safe Search, suggestions comprises", "Non", "Non", "Non"],
        ["Nudité dans les images", "Floutée jusqu'à vérification sur ton appareil", "Floutée", "Non", "Non", "Non"],
        ["SafeSearch et mode restreint de YouTube imposés", "Oui", "Oui", "Non", "Non", "Avec la supervision Family Link"],
        ["Contrôle parental (PIN, listes de sites, limites de temps)", "Family Premium", _NS, "Non", "Non", "Avec Google Family Link"],
        ["Rapport aux parents", "Family Premium, par e-mail", _NS, "Non", "Non", "Avec Google Family Link"],
        ["Un enfant peut désactiver les protections", "Pas avec le PIN parental", _NS, "Oui", "Oui", "Selon Family Link"],
        ["Retirer la musique de fond des vidéos", "Gratuit, sur ton appareil", _NS, "Non", "Non", "Non"],
        ["Publicités et traqueurs", "Bloqués, uBlock Origin intégré", "Bloqués", "Bloqués (Shields)", "Traqueurs bloqués ; les publicités demandent une extension", "Non bloqués ; les bloqueurs de publicités sont limités"],
        ["Choisir qui flouter, reconnaître le hijab", "Premium", _NS, "Non", "Non", "Non"],
        ["YouTube plus calme", "Premium : pas de recommandations, de Shorts ni de lecture automatique", "Safe YouTube", "Non", "Non", "Non"],
        ["Heures de prière et verset du jour", "Gratuit", "Heures de prière", "Non", "Non", "Non"],
        ["Vérification halal, alerte riba, pause prière", "Family Premium", _NS, "Non", "Non", "Non"],
        ["Basé sur", "Firefox", "Chromium", "Chromium", "Moteur propre à Firefox", "Chromium"],
    ],
    "after": """<h2>En bref</h2>
<p><strong>Brave, Firefox et Chrome</strong> sont de bons navigateurs généraux, mais aucun ne filtre le contenu haram ni ne floute les images de lui-même. Il te faudrait des extensions, qu'un enfant peut supprimer.</p>
<p><strong>Kahf Browser et AkhiBrowser</strong> sont faits pour les musulmans et filtrent dès le départ. AkhiBrowser ajoute la suppression de la musique de fond, le choix de qui flouter, un contrôle parental avec PIN et rapport par e-mail, ainsi qu'une vérification halal, une alerte riba et une pause prière.</p>
<p>Tu as repéré quelque chose de dépassé ? Dis-le-nous à <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a> et nous le corrigerons. AkhiBrowser n'est affilié à aucun de ces navigateurs.</p>""",
    "sources_label": "Pages que nous avons lues :",
}
