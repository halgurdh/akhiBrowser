"""The German text of the blog and comparison pages. content.py merges it in; see build_pages.py and langs.py.

Each key in ARTICLES is an article slug from content.py. {YEAR} stands for the current year."""

UI = {
    "nav_label": "Hauptmenü",
    "blog": "Blog",
    "compare": "Vergleich",
    "download": "AkhiBrowser holen",
    "blog_title": "Ratgeber für halal surfen",
    "blog_lead": "Praktische Ratgeber, um im Web mit weniger Werbung, weniger haram Inhalten und mehr Kontrolle zu surfen, auf deinem eigenen Gerät.",
    "cta_title": "AkhiBrowser holen",
    "cta_text": "Ein privater Browser für Muslime, auf Basis von Firefox. Im Microsoft Store für Windows und bei Google Play für Android. Der Schutz ist kostenlos.",
    "footer": "AkhiBrowser basiert auf <a href=\"https://www.firefox.com/\">Firefox</a> und wird nicht von Mozilla hergestellt oder unterstützt. Filter können etwas übersehen und ersetzen nicht die Fürsorge der Eltern. <a href=\"/de/\">Start</a> · <a href=\"/de/faq/\">Häufige Fragen</a> · <a href=\"mailto:support@akhibrowser.com\">support@akhibrowser.com</a>",
}

ARTICLES = {
    "what-is-a-halal-browser": {
        "title": "Was ist ein Halal-Browser, und brauchst du einen?",
        "description": "Was ein Halal-Browser tut, was er nicht kann und wie du einen auswählst: Seitensperren, SafeSearch, unscharfe Bilder und Datenschutz erklärt.",
        "body": """<p>Ein Halal-Browser ist ein Webbrowser, der filtert, was ein normaler Browser dir überlässt. Er blockiert Seiten und Suchen nach Dingen wie Erwachsenen-Inhalten, Alkohol und Glücksspiel und hält unerwünschte Bilder von deinem Bildschirm fern.</p>
<h2>Was ein Halal-Browser meistens tut</h2>
<ul>
<li><strong>Er blockiert Seiten.</strong> Seiten mit Erwachsenen-Inhalten, Glücksspiel, Alkohol und Drogen stoppen, bevor sie laden.</li>
<li><strong>Er erzwingt SafeSearch.</strong> Suchmaschinen blenden anstößige Ergebnisse aus, ohne dass du es einrichten musst.</li>
<li><strong>Er filtert Bilder.</strong> Bilder mit Nacktheit werden unscharf.</li>
<li><strong>Er blockiert Werbung und Tracker.</strong> Viele unerwünschte Bilder kommen über Werbung, also hilft das doppelt.</li>
</ul>
<h2>Was er nicht kann</h2>
<p>Kein Filter ist perfekt. Manche Seiten kommen durch, und manche harmlose werden blockiert. Ein Browser schützt außerdem nur, was in diesem Browser passiert: Andere Apps und andere Browser auf demselben Gerät sind nicht abgedeckt. Er hilft bei Absicht und Gewohnheit, ersetzt sie aber nicht, und auch nicht die Fürsorge der Eltern.</p>
<h2>Wie du einen auswählst</h2>
<ul>
<li><strong>Wo wird geprüft?</strong> Filtern auf deinem eigenen Gerät heißt, dass deine Bilder es nicht verlassen müssen.</li>
<li><strong>Was verlässt dein Gerät?</strong> Achte auf eine klare Liste. Ein Browser, der „nichts“ sagt, sollte erklären können, wie er Seiten blockiert und sich aktualisiert.</li>
<li><strong>Kannst du ihn steuern?</strong> Du solltest jede Schutzfunktion sehen und ändern können.</li>
<li><strong>Läuft er auf deinen Geräten?</strong> Prüfe das vorher, besonders auf einem iPhone oder Mac.</li>
</ul>
<h2>Halal-Browser, Browser-Erweiterung oder DNS-Filter?</h2>
<p>Es gibt drei gängige Wege, das Web zu filtern, und sie wirken am besten zusammen:</p>
<ul>
<li><strong>Ein Halal-Browser</strong> filtert im Browser selbst: Seiten, Suchen, Bilder und Videos. Sein Schutz ist ab der ersten Seite an und lässt sich mit einer PIN sperren.</li>
<li><strong>Eine Browser-Erweiterung</strong> fügt einem Browser, den du schon nutzt, etwa Chrome, einen Filter hinzu. Sie ist schnell ausprobiert, lässt sich aber meist entfernen oder ausschalten und kann nicht ändern, wie der Browser selbst funktioniert.</li>
<li><strong>Ein DNS- oder Router-Filter</strong> sperrt ganze Seiten für jede App auf einem Gerät oder in einem Netzwerk. Er kann nicht in eine Seite hineinsehen, also kein Bild unscharf machen und keine Musik aus einem Video entfernen.</li>
</ul>
<p>Für eine Familie ist eine übliche Einrichtung ein Family-DNS am Router plus ein Halal-Browser auf jedem Gerät, mit entfernten oder gesperrten anderen Browsern. Lies <a href="/de/blog/block-haram-content/">wie du haram Inhalte auf Handy und Computer blockierst</a> für die vollständige Einrichtung.</p>
<h2>Eine Checkliste für die Wahl eines Halal-Browsers</h2>
<ul>
<li>Sind Seiten mit Erwachsenen-Inhalten, Glücksspiel, Alkohol und Drogen ab der ersten Seite blockiert, ohne Einrichtung?</li>
<li>Ist SafeSearch bei jeder Suchmaschine erzwungen, auch bei YouTube?</li>
<li>Werden Bilder auf deinem Gerät geprüft oder an einen Server geschickt?</li>
<li>Können Eltern die Einstellungen mit einer PIN sperren?</li>
<li>Steht klar da, was dein Gerät verlässt?</li>
<li>Wird er noch aktualisiert? Ein Browser ohne Updates bekommt auch keine Sicherheitskorrekturen mehr. SalamWeb, einer der ersten Halal-Browser, wurde 2021 eingestellt.</li>
</ul>
<p>Wir vergleichen die Möglichkeiten in <a href="/de/blog/best-halal-browsers/">die besten Halal-Browser {YEAR}</a>.</p>
<h2>Häufige Fragen</h2>
<h3>Ist ein Halal-Browser nur für Muslime?</h3>
<p>Nein. Jeder, der weniger Werbung, keine Erwachsenen-Inhalte und mehr Kontrolle über Bilder will, kann einen nutzen. Der Name beschreibt die Werte, auf denen er aufbaut.</p>
<h3>Ist ein Halal-Browser kostenlos?</h3>
<p>Viele sind es. Der Schutz von AkhiBrowser ist kostenlos, mit optionalem Premium für zusätzliche Bildeinstellungen und Elternwerkzeuge.</p>
<h3>Ersetzt ein Halal-Browser die Elternkontrolle?</h3>
<p>Er deckt den Browser ab. Für Apps und andere Browser kombinierst du ihn mit der Kontrolle des Geräts, etwa Google Family Link oder Microsoft Family Safety. Siehe <a href="/de/blog/parental-controls-for-muslim-families/">eine einfache Einrichtung der Elternkontrolle</a>.</p>
<h3>Kann ein Halal-Browser Musik aus Videos entfernen?</h3>
<p>Manche können das. AkhiBrowser <a href="/de/blog/remove-background-music-from-videos/">entfernt Hintergrundmusik auf deinem Gerät</a>, sodass die Stimmen bleiben und die Musik geht.</p>
<p>AkhiBrowser ist eine Möglichkeit, auf Basis von Firefox für Windows und Android. Sein Schutz ist ab der ersten Seite an, und <a href="/de/privacy/">seine Website listet, was dein Gerät verlässt</a>. Du kannst auch lesen, <a href="/de/compare/kahf-browser/">wie er sich mit Kahf Browser vergleicht</a>.</p>""",
    },
    "block-haram-content": {
        "title": "So blockierst du haram Inhalte auf Handy und Computer",
        "description": "Schritt für Schritt Erwachsenen-, Glücksspiel- und Alkohol-Inhalte blockieren: Browserfilter, SafeSearch, Family-DNS und Gerätekontrolle, und was jedes davon übersieht.",
        "body": """<p>Keine einzelne Einstellung blockiert alles. Was funktioniert, sind ein paar Schichten, die jeweils abdecken, was die anderen übersehen.</p>
<h2>1. Nutze einen Browser, der von Haus aus filtert</h2>
<p>Ein filternder Browser blockiert Seiten, filtert Suchen und macht Bilder unscharf, ohne Einrichtung. In AkhiBrowser sind Seiten mit Erwachsenen-Inhalten, Alkohol, Drogen, Vapes und Glücksspiel ab der ersten Seite blockiert.</p>
<h2>2. Erzwinge SafeSearch</h2>
<p>SafeSearch blendet anstößige Ergebnisse in Suchmaschinen aus. Du kannst es in den Einstellungen jeder Suchmaschine einschalten, aber es ist leicht wieder auszuschalten, und es gilt nur pro Browser. Ein filternder Browser kann es erzwingen: AkhiBrowser tut das bei Google, Bing, DuckDuckGo und Yahoo und schaltet den eingeschränkten Modus von YouTube ein.</p>
<h2>3. Füge ein Family-DNS hinzu</h2>
<p>Ein Family-DNS-Dienst weigert sich, Erwachsenen-Seiten nachzuschlagen, für alles in diesem Netzwerk oder auf diesem Gerät. Cloudflares 1.1.1.3 und CleanBrowsing sind bekannte Möglichkeiten. Es arbeitet mit Seitennamen, sieht also nicht, was auf einer erlaubten Seite ist, und wer es betreibt, sieht die Namen der Seiten, die du besuchst.</p>
<h2>4. Schließe die Seitentüren</h2>
<p>Ein Browserfilter deckt keine anderen Apps ab. Nutze auf dem Gerät eines Kindes Google Family Link unter Android oder Microsoft Family Safety unter Windows, um zu steuern, welche Apps und Browser installiert werden können. In AkhiBrowser kann Family Premium außerdem die Einstellungen mit einer PIN sperren und private Tabs ausschalten.</p>
<h2>5. Bleibt im Gespräch</h2>
<p>Filter übersehen etwas, und auf dem Handy eines Freundes wirken sie nicht. Für Kinder ist es wichtiger als jede Einstellung, zu wissen, was sie tun, wenn etwas auf dem Bildschirm erscheint.</p>""",
    },
    "remove-background-music-from-videos": {
        "title": "So entfernst du Hintergrundmusik aus Videos in deinem Browser",
        "description": "Wie die Stimmentrennung auf dem Gerät Hintergrundmusik aus Online-Videos entfernt und die Sprache behält, wo sie gut funktioniert und wo sie Mühe hat.",
        "body": """<p>Viele Vorträge, Dokumentationen und Nachrichtenclips haben Hintergrundmusik, die du lieber nicht hören möchtest. Stummschalten geht nicht, wenn du die Sprache hören willst. Stimmentrennung löst das: Ein kleines Sprachmodell behält die Stimmen und entfernt den Rest.</p>
<p>Gelehrte sind sich beim Thema Musik nicht einig, und dieser Artikel will das nicht entscheiden. Er erklärt nur, was die Technik kann, für alle, die sie wollen.</p>
<h2>Wie es funktioniert</h2>
<p>Ein Sprachmodell hört den Ton eines Videos in kurzen Abschnitten und schätzt, welcher Teil eine menschliche Stimme ist. Der Rest wird entfernt, bevor er deine Lautsprecher erreicht. Läuft es auf deinem Gerät, muss der Ton nirgendwohin geschickt werden.</p>
<h2>So nutzt du es in AkhiBrowser</h2>
<ol>
<li>Installiere AkhiBrowser unter Windows oder Android.</li>
<li>Spiel ein Video ab. No music ist standardmäßig an.</li>
<li>Zum Ausschalten öffne das AkhiBrowser-Schild in der Symbolleiste. Auf Android: Menü, dann Erweiterungen, dann AkhiBrowser.</li>
</ol>
<p>Handys und langsamere Computer nutzen ein leichteres Modell, damit sie mithalten.</p>
<h2>Wo es weniger gut funktioniert</h2>
<ul>
<li><strong>Gesang.</strong> Eine Singstimme ist trotzdem eine Stimme, also muss das Modell entscheiden, was es damit macht.</li>
<li><strong>Laute Musik über leiser Sprache.</strong> Etwas Musik kann bleiben, und die Stimme kann dünner klingen.</li>
<li><strong>Seiten, die den Zugriff auf ihren Ton sperren.</strong> Manche geschützte Videos lassen sich nicht bearbeiten.</li>
</ul>
<p>Die Funktion baut auf <a href="https://github.com/mohamedsadiqaguenaou/NoMusic">NoMusic von Mohamed Sadiq</a> auf.</p>""",
    },
    "parental-controls-for-muslim-families": {
        "title": "Elternkontrolle für muslimische Familien: eine einfache Einrichtung",
        "description": "Eine einfache Einrichtung für Eltern: ein filternder Browser, eine PIN, freigegebene Seiten für kleine Kinder, Schlafens- und Schulzeiten, und was kein Browser steuern kann.",
        "body": """<p>Gute Elternkontrolle passt zum Alter des Kindes. Das hier sind sinnvolle Ausgangspunkte mit der Elternkontrolle von Family Premium in AkhiBrowser. Jede ist aus, bis du sie einschaltest, und die Daten bleiben auf dem Gerät.</p>
<h2>Zuerst, für jedes Alter</h2>
<ol>
<li>Lege eine Eltern-PIN fest, damit der Schutz nicht ohne sie ausgeschaltet werden kann.</li>
<li>Schalte <strong>Keine privaten Tabs</strong> ein, damit das Surfen unter der Kontrolle bleibt.</li>
<li>Entferne andere Browser vom Gerät oder sperre sie mit Google Family Link oder Microsoft Family Safety. Ein Browser kann nicht steuern, was außerhalb von ihm passiert.</li>
</ol>
<h2>Kleine Kinder</h2>
<p>Nutze <strong>Nur freigegebene Seiten erlauben</strong> und füge die wenigen Seiten hinzu, die sie nutzen. Alles andere bleibt zu, was viel stärker ist, als zu versuchen, die schlechten Teile des Webs zu blockieren.</p>
<h2>Ältere Kinder</h2>
<p>Öffne das Web, aber setze Grenzen. <strong>Gewählte Seiten blockieren</strong> deckt bestimmte Seiten ab, die Ärger machen, und <strong>Zeitlimits</strong> setzt ein Tageslimit, Schlafens- und Schulzeiten. Das <strong>Feed-Limit</strong> blendet Kurzvideo-Feeds aus und stoppt soziale Websites nach einer festgelegten Zeit. Es wirkt auf Websites in AkhiBrowser, nicht in Social-Media-Apps.</p>
<h2>Jugendliche</h2>
<p>Vertrauen wächst mit dem Alter. Die <strong>Aktivitätsübersicht</strong> zeigt, wie viele Seiten blockiert wurden und warum, ohne ihre Adressen. Sie ist ein Anfang für ein Gespräch, keine Überwachung.</p>
<h2>Wenn du eine Pause brauchst</h2>
<p><strong>Internet pausieren</strong> stoppt das Surfen sofort, mit der PIN zum Fortsetzen. Das ist praktisch beim Essen und rund ums Gebet.</p>
<p>Sieh dir die <a href="/de/#premium">Pläne und Preise</a> an. Der kostenlose Schutz funktioniert ohne all das.</p>""",
    },
    "why-prayer-times-differ": {
        "title": "Warum Gebetszeiten sich zwischen Apps und Moscheen unterscheiden",
        "description": "Warum Fadschr und Ischa zwischen Apps um mehr als eine halbe Stunde abweichen können: Berechnungsmethoden erklärt, mit einem echten Beispiel aus Almere in den Niederlanden.",
        "body": """<p>Zwei Apps können für dasselbe Gebet in derselben Stadt verschiedene Zeiten zeigen. Meistens ist keine kaputt: Sie nutzen eine andere Berechnungsmethode.</p>
<h2>Was gleich bleibt, und was sich ändert</h2>
<p>Dhuhr und Maghrib folgen dem Stand der Sonne, darin sind sich die Methoden meist einig. Fadschr und Ischa hängen von der Dämmerung ab, wenn die Sonne einen bestimmten Winkel unter dem Horizont steht, und die Methoden wählen verschiedene Winkel. Auch Asr unterscheidet sich je nach Rechtsschule: Die hanafitische Zeit ist später als die übliche.</p>
<h2>Ein echtes Beispiel</h2>
<p>Das sind die Zeiten für Almere in den Niederlanden am 8. November 2026, vom öffentlichen <a href="https://aladhan.com/prayer-times-api">Berechnungsdienst Aladhan</a>:</p>
<div class="table"><table>
<thead><tr><th scope="col">Methode</th><th scope="col">Fadschr</th><th scope="col">Ischa</th></tr></thead>
<tbody>
<tr><th scope="row">Marokko</th><td>05:43</td><td>18:48</td></tr>
<tr><th scope="row">Muslim World League</th><td>05:50</td><td>18:48</td></tr>
<tr><th scope="row">Karatschi</th><td>05:50</td><td>18:55</td></tr>
<tr><th scope="row">Moonsighting Committee</th><td>06:09</td><td>18:26</td></tr>
<tr><th scope="row">ISNA</th><td>06:10</td><td>18:35</td></tr>
<tr><th scope="row">Frankreich (UOIF)</th><td>06:30</td><td>18:15</td></tr>
</tbody>
</table></div>
<p>Das sind 47 Minuten zwischen dem frühesten und dem spätesten Fadschr. Weit weg vom Äquator ändern sich die Abstände mit den Jahreszeiten, und im Sommer gibt es manchmal gar keine echte Dämmerung, deshalb brauchen Methoden auch Regeln für hohe Breitengrade.</p>
<h2>Welche solltest du nutzen?</h2>
<p>Bei einer Frage der Praxis frag deine örtliche Moschee oder einen Gelehrten, dem du vertraust, und folge dem, was deine Gemeinde nutzt. Eine App kann nur rechnen.</p>
<h2>Gebetszeiten in AkhiBrowser</h2>
<p>AkhiBrowser berechnet Gebetszeiten auf deinem Gerät aus der Stadt, die du wählst, ohne deinen Standort zu nutzen. Er wählt eine Methode nach dem Land, und du kannst die Methode und die Asr-Zeit in den Optionen ändern.</p>""",
    },
    "best-halal-browsers": {
        "title": "Die besten Halal-Browser {YEAR} im Vergleich",
        "description": "Ein ehrlicher Vergleich der Halal-Browser, die du {YEAR} nutzen kannst: AkhiBrowser, Kahf Browser und Tahir Browser, und was aus SalamWeb wurde. Plattformen, Preis und Funktionen.",
        "body": """<p>Ein Halal-Browser blockiert haram Seiten, erzwingt SafeSearch und hält unerwünschte Bilder von deinem Bildschirm fern. {YEAR} gibt es drei aktive Möglichkeiten, die man kennen sollte. Einen davon, AkhiBrowser, machen wir selbst, deshalb hält sich diese Seite an das, was jeder Browser auf seinen eigenen Seiten angibt, und sagt klar, wo jeder am besten passt.</p>
<h2>Die kurze Antwort</h2>
<ul>
<li><strong>Unter Windows oder für Elternkontrolle:</strong> AkhiBrowser. Kostenloser Schutz, Entfernen von Hintergrundmusik und Family Premium mit PIN, Seitenlisten und Zeitlimits.</li>
<li><strong>Auf einem Mac oder für einen komplett kostenlosen Browser auf jeder Plattform:</strong> Kahf Browser. Windows, macOS, Android und iOS, kostenlos ohne In-App-Käufe.</li>
<li><strong>Auf einem iPhone:</strong> Tahir Browser oder Kahf Browser. AkhiBrowser gibt es noch nicht für iOS.</li>
</ul>
<h2>AkhiBrowser</h2>
<p>Ein Halal-Browser auf Basis von Firefox, für Windows und Android. Seiten mit Erwachsenen-Inhalten, Alkohol, Drogen, Vapes und Glücksspiel sind ab der ersten Seite blockiert, SafeSearch ist bei Google, Bing, DuckDuckGo, Yahoo und YouTube erzwungen, und Bilder bleiben unscharf, bis sie auf deinem Gerät geprüft sind. Er ist der einzige der drei, der Hintergrundmusik aus Videos entfernt, auf deinem Gerät. Der Schutz ist kostenlos; Premium bietet die Wahl, wer unscharf wird, und Family Premium eine Eltern-PIN, Seitenlisten, Zeitlimits und eine Pausetaste.</p>
<h2>Kahf Browser</h2>
<p>Ein Browser auf Chromium-Basis für Muslime unter Windows, macOS, Android und iOS. Laut seiner Website ist er auf allen Plattformen kostenlos ohne Abos oder In-App-Käufe, blockiert Werbung, Erwachsenen- und haram Seiten mit KI-Filter und Datenbank, erzwingt SafeSearch und Safe YouTube, macht Nacktheit in Echtzeit unscharf und hat Gebetszeiten und die Qibla. Die meisten Chrome-Erweiterungen funktionieren darin.</p>
<h2>Tahir Browser</h2>
<p>Ein Browser für iPhone und iPad von Ihya Tech. Sein App-Store-Eintrag beschreibt, alle Bilder unscharf zu machen oder per KI das andere Geschlecht, Antippen zum Scharfstellen, das Blockieren von haram Seiten, Werbung und Trackern, islamische Erinnerungen, erzwungenes SafeSearch und eine Passwort- oder Biometrie-Sperre für sein Schild. Er ist kostenlos zum Herunterladen, mit optionalen Monats- und Jahresplänen.</p>
<h2>Was wurde aus SalamWeb?</h2>
<p>SalamWeb war einer der ersten Halal-Browser und bekam 2019 viel Presse. Er wurde 2021 eingestellt und seine Website ist weg, also ist er keine Möglichkeit mehr. Das ist eine gute Erinnerung, einen Browser zu wählen, der noch aktualisiert wird, denn Updates bringen Sicherheitskorrekturen.</p>
<h2>Nebeneinander</h2>
<div class="table"><table>
<thead><tr><th scope="col"></th><th scope="col">AkhiBrowser</th><th scope="col">Kahf Browser</th><th scope="col">Tahir Browser</th></tr></thead>
<tbody>
<tr><th scope="row">Plattformen</th><td>Windows, Android</td><td>Windows, macOS, Android, iOS</td><td>iPhone, iPad</td></tr>
<tr><th scope="row">Preis</th><td>Schutz kostenlos; optionales Premium</td><td>Kostenlos</td><td>Kostenlos; optionale Pläne</td></tr>
<tr><th scope="row">Basiert auf</th><td>Firefox</td><td>Chromium</td><td>iOS WebKit</td></tr>
<tr><th scope="row">Haram Seiten blockiert</th><td>Ja</td><td>Ja</td><td>Ja</td></tr>
<tr><th scope="row">SafeSearch erzwungen</th><td>Ja, inkl. YouTube</td><td>Ja, inkl. YouTube</td><td>Ja</td></tr>
<tr><th scope="row">Unscharfe Bilder</th><td>Bis geprüft, auf deinem Gerät</td><td>In Echtzeit</td><td>Alle Bilder, oder per KI nach Geschlecht</td></tr>
<tr><th scope="row">Hintergrundmusik entfernen</th><td>Ja</td><td>Nicht angegeben</td><td>Nicht angegeben</td></tr>
<tr><th scope="row">Eltern-PIN und Zeitlimits</th><td>Family Premium</td><td>Nicht angegeben</td><td>Sperre für das Schild</td></tr>
</tbody>
</table></div>
<p>&quot;Nicht angegeben&quot; heißt, dass wir es auf den eigenen Seiten des Browsers nicht gefunden haben, nicht, dass es das nicht gibt. Für eine längere Tabelle siehe <a href="/de/compare/kahf-browser/">AkhiBrowser und Kahf Browser im Vergleich</a> und <a href="/de/compare/browsers/">AkhiBrowser, Kahf, Brave, Firefox und Chrome im Vergleich</a>. Neu beim Thema? Fang an mit <a href="/de/blog/what-is-a-halal-browser/">was ein Halal-Browser ist</a>.</p>
<p>Am 10. November 2026 mit den eigenen Seiten jedes Browsers abgeglichen. Etwas veraltet? Schreib uns an <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>.</p>""",
    },
}

_NS = "Nicht angegeben"

COMPARE = {
    "seo_title": "AkhiBrowser vs. Kahf Browser: Funktionen, Preis und Plattformen im Vergleich",
    "title": "AkhiBrowser und Kahf Browser im Vergleich",
    "description": "AkhiBrowser und Kahf Browser nebeneinander: Preis, Plattformen, Filter, Bilder, Musikentfernung, Gebetszeiten und Elternkontrolle, von den eigenen Seiten jedes Browsers.",
    "lead": "Beide sind Browser für Muslime. Diese Tabelle zeigt, was jeder auf seiner eigenen Website angibt, Stand 8. November 2026 für Kahf Browser und 22. November 2026 für AkhiBrowser. Kahf Browser haben wir nicht selbst getestet. &quot;Nicht angegeben&quot; heißt, dass wir es auf den gelesenen Seiten nicht gefunden haben, nicht, dass es die Funktion nicht gibt.",
    "head": ["", "AkhiBrowser", "Kahf Browser"],
    "rows": [
        ["Preis", "Schutz kostenlos. Optionales Premium für 3,99 € im Monat, 39 € im Jahr oder 119 € einmalig; Family Premium 59,99 € im Jahr", "Kostenlos auf allen Plattformen, ohne Abos oder In-App-Käufe"],
        ["Plattformen", "Windows (Microsoft Store), Android (Google Play). iOS und macOS: <a href=\"/de/#roadmap\">auf der Roadmap</a>, noch ohne Datum", "Windows, macOS, Android, iOS. Linux: in seinen FAQ genannt, seine Download-Seite sagt bald verfügbar"],
        ["Erwachsenen- und haram Seiten", "Blockiert: Erwachsenen-Inhalte, Alkohol, Drogen, Vapes und Glücksspiel", "Blockiert, mit KI-Filter und Datenbank"],
        ["Haram Suchen", "In 11 Sprachen blockiert; Fragen dazu bleiben erlaubt", "Safe Search, auch bei Suchvorschlägen"],
        ["Nacktheit in Bildern", "Unscharf, bis auf deinem Gerät geprüft: Bilder, Hintergründe, Video und Canvas; in Videos in Echtzeit: jede neue Szene wird sofort unscharf gemacht und geprüft", "In Echtzeit unscharf"],
        ["SafeSearch", "Erzwungen bei Google, Bing, DuckDuckGo und Yahoo, dazu der eingeschränkte Modus von YouTube", "Bei großen Suchmaschinen erzwungen; Safe YouTube"],
        ["Eltern-PIN, Seitenlisten, Zeitlimits", "Family Premium: PIN, gesperrte oder nur freigegebene Seiten, Schlafens- und Schulzeiten, ein Tageslimit", _NS],
        ["Elternbericht und Aktivitätsübersicht", "Family Premium: eine E-Mail, wenn ein Schutz oder die PIN ausgeschaltet wird, eine wöchentliche Übersicht der Sperren nach Grund und eine 7-Tage-Übersicht auf dem Gerät", _NS],
        ["Internet pausieren", "Family Premium, mit der PIN; die Elternkontrolle lässt sich in einer mit der PIN gesperrten Datei auf ein anderes Gerät übertragen", _NS],
        ["Soziale Feeds und Apps", "Family Premium: Kurzvideo-Feeds ausgeblendet, ein Tageslimit für soziale Seiten, Apps auf Android gesperrt", _NS],
        ["Hintergrundmusik aus Videos entfernen", "Kostenlos, auf deinem Gerät", _NS],
        ["Werbung und Tracker", "Blockiert, mit uBlock Origin und einem eingebauten Blocker", "Eingebauter Blocker"],
        ["Phishing- und Betrugsseiten", "Blockiert", "Blockiert"],
        ["Wählen, wer unscharf wird (Frauen, Männer)", "Premium", _NS],
        ["Hidschab erkennen", "Premium", _NS],
        ["Strenger Modus", "Premium: Jedes Bild und Video bleibt unscharf, bis du es antippst", _NS],
        ["YouTube", "Eingeschränkter Modus, kostenlos. Premium: keine Empfehlungen, Shorts oder Autoplay. Family Premium: Deen Time, nur die Kanäle deiner Wahl", "Safe YouTube"],
        ["Gebetszeiten", "Kostenlos, für eine Stadt deiner Wahl, ohne deinen Standort; Erinnerungen auf Computern", "Gebetszeiten und Benachrichtigungen"],
        ["Gebetspause", "Family Premium: Soziale, Video- und Spieleseiten pausieren nach jeder Gebetszeit für einige Minuten", _NS],
        ["Halal-Check und Halal-Orte", "Family Premium: ein Hinweis auf Produktseiten mit Schwein, Alkohol, Gelatine oder zweifelhaften E-Nummern; Halal-Orte auf Google Maps und Lieferseiten", _NS],
        ["Riba-Warnung, Lootboxen", "Family Premium: eine Warnung auf Seiten für Zinskredite, Kreditkarten und „Jetzt kaufen, später zahlen“; Case-Opening- und Skin-Glücksspielseiten blockiert", _NS],
        ["Koranrezitation, vertrauenswürdige Quellen", "Family Premium: eine Rezitation auf YouTube Vers für Vers mit Bedeutung verfolgen; Quellen von Gelehrten zuerst bei der Suche über den Islam", _NS],
        ["Vers des Tages", "Kostenlos", _NS],
        ["Qibla", "Ja, auf Android: ein Kompass unter den Gebetszeiten", "Ja"],
        ["Sprachen", "12, darunter Arabisch, Urdu, Persisch, Kurdisch und Türkisch", _NS],
        ["Korrektur bei Farbenblindheit", "Kostenlos, auf deinem Gerät", _NS],
        ["Konto nötig", "Nein", "Nein; Anmeldung möglich"],
        ["Basiert auf", "Firefox", "Chromium; die meisten Chrome-Erweiterungen funktionieren"],
        ["Quellcode", "Firefox-Änderungen und MPL-Dateien sind öffentlich; die eigene Erweiterung ist privat", "Noch nicht öffentlich, laut seinen FAQ"],
    ],
    "after": """<h2>Welcher passt zu dir?</h2>
<p><strong>Kahf Browser</strong> passt, wenn du ein iPhone oder einen Mac nutzt oder alles kostenlos willst.</p>
<p><strong>AkhiBrowser</strong> passt, wenn du Hintergrundmusik entfernen, wählen willst, wer unscharf wird, oder Elternkontrolle wie PIN, Zeitlimits und einen Bericht per E-Mail brauchst, unter Windows oder Android. Family Premium bietet, was Kahf nicht nennt: einen Halal-Check beim Einkaufen, eine Riba-Warnung und eine Pause nach jedem Gebet.</p>
<p>Beide sind kostenlos zum Ausprobieren, also ist dein eigener Gebrauch der beste Test. AkhiBrowser ist nicht mit Kahf verbunden. Etwas veraltet? Schreib uns an <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>, dann korrigieren wir es.</p>""",
    "sources_label": "Die Seiten von Kahf Browser, die wir gelesen haben:",
}

_CWS = "https://chromewebstore.google.com/detail/akhibrowser/ghkpflipnhahpjdnpoclaakbecnopamk"
_AMO = "https://addons.mozilla.org/en-US/firefox/addon/akhibrowser/"
_ALL5 = "Windows, macOS, Linux, Android, iOS"

COMPARE_BROWSERS = {
    "seo_title": "Halal-Browser im Vergleich: AkhiBrowser, Kahf Browser, Brave, Firefox und Chrome",
    "title": "AkhiBrowser, Kahf Browser, Brave, Firefox und Chrome im Vergleich",
    "description": "Welcher Browser filtert haram Inhalte, macht Bilder unscharf, entfernt Hintergrundmusik und hat Elternkontrolle? AkhiBrowser, Kahf Browser, Brave, Firefox und Chrome nebeneinander.",
    "lead": "Was jeder Browser ab Werk kann, ohne zusätzliche Erweiterungen, so wie jeder es auf seinen eigenen Seiten beschreibt, Stand 9. November 2026 und 15. November 2026 für AkhiBrowser. Kahf Browser haben wir nicht selbst getestet; siehe <a href=\"/de/compare/kahf-browser/\">den ausführlichen Vergleich mit Kahf Browser</a>.",
    "head": ["", "AkhiBrowser", "Kahf Browser", "Brave", "Firefox", "Chrome"],
    "rows": [
        ["Preis", "Schutz kostenlos; optionales Premium und Family Premium", "Kostenlos", "Kostenlos", "Kostenlos", "Kostenlos"],
        ["Plattformen", f"Windows (Microsoft Store), Android (Google Play); leichtere kostenlose Erweiterungen für <a href=\"{_CWS}\">Chrome</a> und <a href=\"{_AMO}\">Firefox</a>", "Windows, macOS, Android, iOS", _ALL5, _ALL5, _ALL5],
        ["Erwachsenen- und haram Seiten", "Blockiert, ab der ersten Seite", "Blockiert", "Nein", "Nein", "Nein"],
        ["Haram Suchen blockiert", "Ja, in 11 Sprachen", "Safe Search, auch bei Vorschlägen", "Nein", "Nein", "Nein"],
        ["Nacktheit in Bildern", "Unscharf, bis auf deinem Gerät geprüft", "Unscharf", "Nein", "Nein", "Nein"],
        ["SafeSearch und eingeschränkter Modus von YouTube erzwungen", "Ja", "Ja", "Nein", "Nein", "Mit Family-Link-Aufsicht"],
        ["Elternkontrolle (PIN, Seitenlisten, Zeitlimits)", "Family Premium", _NS, "Nein", "Nein", "Mit Google Family Link"],
        ["Bericht für Eltern", "Family Premium, per E-Mail", _NS, "Nein", "Nein", "Mit Google Family Link"],
        ["Schutz kann von einem Kind ausgeschaltet werden", "Nicht mit der Eltern-PIN", _NS, "Ja", "Ja", "Hängt von Family Link ab"],
        ["Hintergrundmusik aus Videos entfernen", "Kostenlos, auf deinem Gerät", _NS, "Nein", "Nein", "Nein"],
        ["Werbung und Tracker", "Blockiert, uBlock Origin eingebaut", "Blockiert", "Blockiert (Shields)", "Tracker blockiert; Werbung braucht eine Erweiterung", "Nicht blockiert; Werbeblocker sind eingeschränkt"],
        ["Wählen, wer unscharf wird, Hidschab erkennen", "Premium", _NS, "Nein", "Nein", "Nein"],
        ["Ruhigeres YouTube", "Premium: keine Empfehlungen, Shorts oder Autoplay", "Safe YouTube", "Nein", "Nein", "Nein"],
        ["Gebetszeiten und Vers des Tages", "Kostenlos", "Gebetszeiten", "Nein", "Nein", "Nein"],
        ["Halal-Check, Riba-Warnung, Gebetspause", "Family Premium", _NS, "Nein", "Nein", "Nein"],
        ["Basiert auf", "Firefox", "Chromium", "Chromium", "Eigene Engine von Firefox", "Chromium"],
    ],
    "after": """<h2>Kurz gesagt</h2>
<p><strong>Brave, Firefox und Chrome</strong> sind gute allgemeine Browser, aber keiner von ihnen filtert haram Inhalte oder macht Bilder von sich aus unscharf. Du bräuchtest Erweiterungen, die ein Kind entfernen kann.</p>
<p><strong>Kahf Browser und AkhiBrowser</strong> sind für Muslime gemacht und filtern von Anfang an. AkhiBrowser bietet zusätzlich das Entfernen von Hintergrundmusik, die Wahl, wer unscharf wird, Elternkontrolle mit PIN und einem Bericht per E-Mail sowie einen Halal-Check, eine Riba-Warnung und eine Gebetspause.</p>
<p>Etwas veraltet? Schreib uns an <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>, dann korrigieren wir es. AkhiBrowser ist mit keinem dieser Browser verbunden.</p>""",
    "sources_label": "Seiten, die wir gelesen haben:",
}
