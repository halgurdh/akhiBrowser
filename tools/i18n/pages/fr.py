"""French texts of /fr/faq/, /fr/newsletter/ and /fr/delete-account/ (tools/build_hand.py)."""

FAQ = {
    "h1": "Questions fréquentes",
    "description": "Réponses sur AkhiBrowser : ce qu'il bloque, les prix, les appareils, Premium et Family Premium, les clés, la résiliation, la confidentialité et l'aide.",
    "search_label": "Chercher dans les questions",
    "search_placeholder": "Par exemple : clé, résilier, mosquée",
    "none": "Aucune question ne correspond. Écris à <a href=\"mailto:support@akhibrowser.com\">support@akhibrowser.com</a>, et nous t'aiderons.",
    "items": [
        ("Qu'est-ce qu'AkhiBrowser ?", "Un navigateur gratuit pour les musulmans et les familles, basé sur Firefox. Il floute les images et les vidéos jusqu'à leur vérification, bloque les sites et recherches haram, et retire la musique de fond des vidéos. Le filtrage se fait sur ton propre appareil."),
        ("AkhiBrowser est-il gratuit ?", "Oui. Le navigateur et ses protections sont gratuits. Premium et Family Premium ajoutent des fonctions ; vois les <a href=\"/#premium\">prix</a>."),
        ("Sur quels appareils fonctionne-t-il ?", "Windows (Microsoft Store ou l'installateur), les téléphones et tablettes Android (Google Play), et en extension pour Chrome et Firefox. Il n'y a pas encore de version iPhone ou Mac."),
        ("Voyez-vous ce que je consulte ?", "Non. Les images et les pages sont vérifiées sur ton appareil, et nous ne gardons aucun historique. Pour bloquer les sites pour adultes, les noms de sites sont vérifiés avec le filtre familial de Cloudflare. Vois la <a href=\"/privacy/\">page confidentialité</a>."),
        ("Quelle est la différence entre Premium et Family Premium ?", "Premium te laisse choisir qui est flouté (avec reconnaissance du hijab) et ajoute le mode strict, la pause prière et YouTube sans Shorts. Family Premium ajoute le contrôle parental : un PIN parental, le blocage de sites et de mots, des limites de temps et des horaires, le blocage d'applications sur Android et un rapport hebdomadaire pour les parents, sur jusqu'à 10 appareils."),
        ("Comment activer Premium ?", "Dans AkhiBrowser, ouvre le menu, Extensions, AkhiBrowser, puis Premium. Colle ta clé et appuie sur Activer. Acheté sur Google Play ? Premium s'active alors tout seul."),
        ("Que se passe-t-il après le paiement ?", "Tu vois ta clé de licence à l'écran, et tu la reçois aussitôt par e-mail. Colle-la dans AkhiBrowser sous Premium. Family Premium par carte commence par 3 jours gratuits, et une formule annuelle reçoit un e-mail quelques jours avant son renouvellement. Quand ta clé commence à fonctionner sur un autre appareil, nous t'écrivons, pour que tu remarques si quelqu'un d'autre l'utilise."),
        ("J'ai acheté sur Android. Puis-je l'utiliser aussi sur mon ordinateur ?", "Oui. Dans les réglages Premium d'AkhiBrowser, récupère ta clé ou fais-la-toi envoyer par e-mail, et colle-la dans AkhiBrowser sous Windows."),
        ("Sur combien d'appareils fonctionne une clé ?", "Une clé fonctionne sur 3 appareils, une clé Family sur 10. Quand une clé est pleine, un nouvel appareil prend la place de celui utilisé il y a le plus longtemps."),
        ("Comment résilier ?", "Acheté sur ce site : sous Premium, appuie sur Gérer l'abonnement. Acheté sur Google Play : dans le Play Store, touche ta photo de profil, puis Paiements et abonnements, Abonnements, AkhiBrowser."),
        ("J'ai perdu ma clé. Que faire ?", "Cherche l'e-mail « Your AkhiBrowser Premium license key ». Introuvable ? Écris à <a href=\"mailto:support@akhibrowser.com\">support@akhibrowser.com</a> depuis l'adresse avec laquelle tu as payé, et nous te la renverrons. Acheté sur Google Play ? Ton téléphone n'a pas besoin de clé, et les réglages Premium d'AkhiBrowser t'en donnent une pour ton ordinateur."),
        ("Mon enfant peut-il désactiver les protections ?", "Avec un PIN parental, les réglages ne peuvent être modifiés qu'avec le PIN. Avec le rapport aux parents activé, tu reçois un e-mail quand une protection est désactivée. AkhiBrowser ne peut pas empêcher quelqu'un de le désinstaller ; si un appareil ne se manifeste plus, tu reçois un e-mail après 8 jours."),
        ("Puis-je bloquer des applications comme Instagram ou TikTok ?", "Sur Android, avec Family Premium : sous Applications bloquées, coche les applications et enregistre avec ton PIN. Une application bloquée affiche un message à la place, et reste bloquée après une réinstallation."),
        ("Comment fonctionne le rapport aux parents ?", "Avec Family Premium ou une clé École / Mosquée, active Rapport aux parents par e-mail dans les réglages d'AkhiBrowser et confirme l'e-mail que nous envoyons. Tu reçois alors un e-mail quand une protection ou le PIN est désactivé, et un résumé hebdomadaire des pages bloquées par motif, sans adresses de pages. Si un appareil ne se manifeste plus pendant 8 jours, nous te prévenons. Chaque e-mail contient un lien pour arrêter."),
        ("Y a-t-il une formule pour les écoles et les mosquées ?", "Oui : la formule École / Mosquée contient tout Family Premium, pour jusqu'à 500 appareils, à offrir gratuitement à leurs familles. Vois <a href=\"/affiliate/\">recommander à ton école ou ta mosquée</a>."),
        ("Comment les familles de notre école ou mosquée l'obtiennent-elles ?", "Après le paiement, tu reçois ta clé à l'écran et par e-mail. 1. Essaie d'abord AkhiBrowser toi-même. 2. Partage la clé dans ton groupe WhatsApp ou ta newsletter : les familles la collent dans AkhiBrowser, sur ordinateur ou depuis Google Play, sur jusqu'à 500 appareils au total. 3. Le <a href=\"/kit/\">kit</a> prépare un message et une affiche. Ne partage la clé qu'avec tes membres, jamais publiquement."),
        ("Puis-je offrir AkhiBrowser ?", "Oui, un an de Family Premium, sans renouvellement. Sur ce site, la clé est envoyée par e-mail à la personne à qui tu l'offres, avec une copie pour toi. Dans AkhiBrowser, tu reçois la clé pour la transmettre toi-même. Elle fonctionne sous Windows et Android."),
        ("Les filtres sont-ils parfaits ?", "Aucun filtre n'attrape tout. AkhiBrowser rend internet bien plus sûr, mais ne remplace pas l'attention des parents."),
        ("Comment recommander AkhiBrowser et en être rémunéré ?", "Remplis le formulaire sur <a href=\"/affiliate/\">recommander à ton école ou ta mosquée</a>. Une fois approuvé, tu reçois ton code et tes liens par e-mail, et un formulaire pour ton IBAN. Une école ou une mosquée qui s'abonne par ton lien te rapporte 20 % de chaque paiement, tant qu'elle reste. Les influenceurs de notre <a href=\"/affiliate/#vip\">programme VIP</a> reçoivent 10 % de chaque paiement Family, et leurs abonnés 10 % de réduction. Chaque mois, nous t'écrivons ce que tu as gagné, et nous le virons."),
        ("Comment devenir sponsor ou partenaire ?", "Remplis le formulaire sur <a href=\"/money/#partner\">comment nous gagnons de l'argent</a>. Nous lisons chaque demande et répondons sous quelques jours. Une fois approuvé, tu reçois un e-mail de bienvenue avec un court formulaire pour ton logo, ton lien et tes informations de facturation. Tu as coché la case pour être listé ? Ton organisation apparaît alors sur notre page des sponsors. Un partenaire n'obtient jamais les données de nos utilisateurs, ni son mot à dire sur ce qui est bloqué."),
        ("Qu'est-ce que la newsletter m'apporte ?", "Un verset du Coran et les nouveautés, chaque vendredi. Tu confirmes d'abord ton adresse. Une semaine plus tard, tu reçois une fois 10 % de réduction sur Family Premium, si tu ne l'as pas encore acheté. Chaque e-mail contient un lien pour arrêter. <a href=\"/newsletter/\">S'inscrire</a>."),
        ("Comment supprimer mes données ?", "AkhiBrowser n'a pas de compte, donc il n'y a rien sur toi à supprimer chez nous. Ton historique et tes réglages restent sur ton appareil. Pour un compte Mozilla, les achats sur Google Play et le rapport aux parents, vois <a href=\"/delete-account/\">supprimer tes données</a>."),
        ("Le paiement est-il sûr ?", "Les paiements sur ce site passent par Stripe : tes données de carte vont à Stripe, jamais à nous, et tu peux aussi payer une fois par iDEAL ou PayPal. Pas besoin de compte. Dans AkhiBrowser de Google Play, Google prend le paiement. AkhiBrowser est inscrit à la Chambre de commerce néerlandaise (KvK 82581509)."),
        ("Où puis-je laisser un avis ?", "Merci ! Un avis aide d'autres familles à trouver AkhiBrowser : sur <a href=\"https://play.google.com/store/apps/details?id=org.akhibrowser&amp;showAllReviews=true\">Google Play</a>, le <a href=\"https://apps.microsoft.com/detail/9n8kmf22z6k4\">Microsoft Store</a>, ou pour l'extension sur le <a href=\"https://chromewebstore.google.com/detail/akhibrowser/ghkpflipnhahpjdnpoclaakbecnopamk/reviews\">Chrome Web Store</a> ou les <a href=\"https://addons.mozilla.org/en-US/firefox/addon/akhibrowser/reviews/\">modules Firefox</a>. Quelque chose ne va pas ? Écris-nous d'abord, et nous le corrigerons."),
        ("Comment vous contacter ?", "Écris à <a href=\"mailto:support@akhibrowser.com\">support@akhibrowser.com</a>. Nous répondons en anglais, en néerlandais et en arabe."),
    ],
}

NEWSLETTER = {
    "title": "La newsletter d'AkhiBrowser : un verset du Coran chaque semaine | AkhiBrowser",
    "description": "Un verset du Coran et les nouveautés d'AkhiBrowser, une fois par semaine par e-mail. Gratuite, et tu peux arrêter en un clic.",
    "h1": "Un verset du Coran chaque semaine",
    "lead": "Une fois par semaine par e-mail : un verset du Coran avec son sens, et les nouveautés d'AkhiBrowser. Une semaine après l'inscription, tu reçois aussi une fois 10 % de réduction sur Family Premium.",
    "email": "Adresse e-mail",
    "consent": "Oui, envoyez-moi la newsletter d'AkhiBrowser. Je peux arrêter à tout moment.",
    "button": "S'inscrire",
    "note": "Nous t'envoyons d'abord un lien de confirmation. Ton adresse ne sert qu'à cette newsletter, n'est jamais partagée, et chaque e-mail contient un lien pour arrêter. Pour éloigner les robots, le formulaire charge Cloudflare Turnstile dès que tu commences à le remplir. <a href=\"/privacy/\">Confidentialité</a>",
    "confirmed_h1": "Tu es inscrit",
    "confirmed_lead": "Merci. La newsletter arrive une fois par semaine, in sha Allah. Chaque e-mail contient un lien pour arrêter.",
}

DELETE = {
    "title": "Supprimer ton compte ou tes données | AkhiBrowser",
    "description": "AkhiBrowser n'a pas de compte et son développeur ne garde aucune donnée personnelle. Comment supprimer un compte Mozilla créé pour Sync, et tes données sur ton appareil.",
    "main": """      <h1>Supprimer ton compte ou tes données</h1>
      <p class="intro">Cette page concerne <strong>AkhiBrowser</strong>, le navigateur halal pour Windows et Android, fait par Halgurd Hussein (AkhiBrowser). AkhiBrowser n'a pas de compte : tu ne t'inscris jamais chez nous, et nous ne gardons aucune donnée personnelle sur toi à supprimer.</p>
      <h2>Un compte Mozilla, créé pour Sync</h2>
      <p>AkhiBrowser est basé sur Firefox et garde Firefox Sync. Si tu as créé un compte Mozilla dans AkhiBrowser pour synchroniser tes marque-pages et mots de passe, ce compte est géré par Mozilla, pas par nous. Pour le supprimer avec ses données synchronisées :</p>
      <ol>
        <li>Va sur <a href="https://accounts.firefox.com">accounts.firefox.com</a> et connecte-toi.</li>
        <li>Descends tout en bas et appuie sur <strong>Supprimer le compte</strong>.</li>
        <li>Confirme, et saisis ton mot de passe. Le compte et ses données synchronisées sont supprimés définitivement.</li>
      </ol>
      <p class="note">Les étapes de Mozilla : <a href="https://support.mozilla.org/kb/how-do-i-delete-my-firefox-account">Comment supprimer mon compte Mozilla ?</a> Pour seulement arrêter la synchronisation, déconnecte-toi de Sync dans les réglages d'AkhiBrowser.</p>
      <h2>Premium, clés de licence et achats</h2>
      <ul>
        <li><strong>Acheté sur Google Play :</strong> Google gère l'achat. Résilie-le dans le Play Store, sous ta photo de profil, Paiements et abonnements.</li>
        <li><strong>Une clé de licence :</strong> ce n'est pas un compte. Notre serveur de licences ne garde que des empreintes de la clé et d'un identifiant d'installation aléatoire, ni nom ni e-mail. Un appareil que tu n'utilises plus libère sa place après 30 jours, et son empreinte est supprimée.</li>
        <li><strong>E-mails aux parents (Family) :</strong> désactive le rapport dans les réglages d'AkhiBrowser, ou utilise le lien d'arrêt dans l'un de ses e-mails. Ton adresse est alors supprimée.</li>
      </ul>
      <h2>Les données sur ton appareil</h2>
      <p>Ton historique, tes réglages et le résumé d'activité restent sur ton appareil. Désinstaller AkhiBrowser les supprime, ou efface-les dans les réglages du navigateur.</p>
      <p class="note">Des questions, ou quelque chose à supprimer ? Écris à <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>. Plus d'infos dans la <a href="https://github.com/halgurdh/akhiBrowser/blob/main/PRIVACY.md">politique de confidentialité</a>.</p>""",
}
