"""The text of the blog and comparison pages, in English and Dutch (Arabic is in content_ar.py). See build_pages.py.

{YEAR} stands for the current year: the build writes it as a span that a script keeps up to date."""

UI = {
    "en": {
        "nav_label": "Main",
        "blog": "Blog",
        "compare": "Compare",
        "download": "Get AkhiBrowser",
        "blog_title": "Halal browsing guides",
        "blog_lead": "Practical guides to browsing the web with fewer ads, less haram content and more control, on your own device.",
        "cta_title": "Get AkhiBrowser",
        "cta_text": "A private browser for Muslims, built on Firefox. On the Microsoft Store for Windows now; Android is coming soon. The protections are free.",
        "footer": 'AkhiBrowser is built on <a href="https://www.firefox.com/">Firefox</a>, and is not made or endorsed by Mozilla. Filters can miss things, and they don\'t replace a parent\'s care. <a href="/">Home</a> · <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>',
    },
    "nl": {
        "nav_label": "Hoofdmenu",
        "blog": "Blog",
        "compare": "Vergelijk",
        "download": "AkhiBrowser downloaden",
        "blog_title": "Gidsen voor halal browsen",
        "blog_lead": "Praktische gidsen om het web te gebruiken met minder reclame, minder haram inhoud en meer controle, op je eigen apparaat.",
        "cta_title": "AkhiBrowser downloaden",
        "cta_text": "Een browser voor moslims die je privacy respecteert, gebouwd op Firefox. Nu in de Microsoft Store voor Windows; Android komt binnenkort. De bescherming is gratis.",
        "footer": 'AkhiBrowser is gebouwd op <a href="https://www.firefox.com/">Firefox</a>, maar is niet gemaakt of goedgekeurd door Mozilla. Filters kunnen iets missen en vervangen niet de aandacht van een ouder. <a href="/">Home</a> · <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>',
    },
}

DATE = "2026-11-08"

ARTICLES = [
    {
        "slug": "what-is-a-halal-browser",
        "date": DATE,
        "en": {
            "title": "What is a halal browser, and do you need one?",
            "description": "What a halal browser does, what it can't do, and how to choose one: site blocking, SafeSearch, image blurring and privacy explained.",
            "body": """<p>A halal browser is a web browser that filters what a normal browser leaves to you. It blocks sites and searches for things like adult content, alcohol and gambling, and it keeps unwanted images off your screen.</p>
<h2>What a halal browser usually does</h2>
<ul>
<li><strong>Blocks sites.</strong> Adult, gambling, alcohol and drug sites stop before they load.</li>
<li><strong>Forces SafeSearch.</strong> Search engines hide explicit results, without you having to set it up.</li>
<li><strong>Filters images.</strong> Pictures that show nudity are blurred.</li>
<li><strong>Blocks ads and trackers.</strong> Many unwanted images arrive through advertising, so this helps twice.</li>
</ul>
<h2>What it can't do</h2>
<p>No filter is perfect. Some pages get through, and some harmless ones get blocked. A browser also only protects what happens inside that browser: other apps and other browsers on the same device aren't covered. It helps with intention and habit, but it doesn't replace them, or a parent's care.</p>
<h2>How to choose one</h2>
<ul>
<li><strong>Where does the checking happen?</strong> Filtering on your own device means your images don't have to leave it.</li>
<li><strong>What leaves your device?</strong> Look for a plain list. A browser that says "nothing" should be able to explain how it blocks sites and updates itself.</li>
<li><strong>Can you control it?</strong> You should be able to see and change every protection.</li>
<li><strong>Does it run on your devices?</strong> Check before you commit, especially on an iPhone or a Mac.</li>
</ul>
<h2>Halal browser, browser extension or DNS filter?</h2>
<p>There are three common ways to filter the web, and they work best together:</p>
<ul>
<li><strong>A halal browser</strong> filters inside the browser itself: sites, searches, images and video. Its protections are on from the first page and can be locked with a PIN.</li>
<li><strong>A browser extension</strong> adds filtering to a browser you already use, such as Chrome. It's quick to try, but it can usually be removed or switched off, and it can't change how the browser itself works.</li>
<li><strong>A DNS or router filter</strong> blocks whole sites for every app on a device or network. It can't look inside a page, so it can't blur an image or remove music from a video.</li>
</ul>
<p>For a family, a common setup is a family DNS on the router plus a halal browser on each device, with other browsers removed or blocked. Read <a href="/blog/block-haram-content/">how to block haram content on your phone and computer</a> for the full setup.</p>
<h2>A checklist for choosing a halal browser</h2>
<ul>
<li>Are adult, gambling, alcohol and drug sites blocked from the first page, without setup?</li>
<li>Is SafeSearch forced on every search engine, including YouTube?</li>
<li>Are images checked on your device, or sent to a server?</li>
<li>Can a parent lock the settings with a PIN?</li>
<li>Does it say plainly what leaves your device?</li>
<li>Is it still updated? A browser that stops getting updates also stops getting security fixes. SalamWeb, one of the first halal browsers, was discontinued in 2021.</li>
</ul>
<p>We compare the options in <a href="/blog/best-halal-browsers/">the best halal browsers in {YEAR}</a>.</p>
<h2>Frequently asked questions</h2>
<h3>Is a halal browser only for Muslims?</h3>
<p>No. Anyone who wants fewer ads, no adult content and more control over images can use one. The name describes the values it's built around.</p>
<h3>Is a halal browser free?</h3>
<p>Many are. AkhiBrowser's protections are free, with optional Premium for extra image controls and parent tools.</p>
<h3>Does a halal browser replace parental controls?</h3>
<p>It covers the browser. For apps and other browsers, combine it with the controls of the device, such as Google Family Link or Microsoft Family Safety. See <a href="/blog/parental-controls-for-muslim-families/">a simple parental-controls setup</a>.</p>
<h3>Can a halal browser remove music from videos?</h3>
<p>Some can. AkhiBrowser <a href="/blog/remove-background-music-from-videos/">removes background music on your device</a>, so the voices stay and the music goes.</p>
<p>AkhiBrowser is one option, built on Firefox for Windows and Android. Its protections are on from the first page, and <a href="/privacy/">its site lists what leaves your device</a>. You can also read <a href="/compare/kahf-browser/">how it compares with Kahf Browser</a>.</p>""",
        },
        "nl": {
            "title": "Wat is een halal browser, en heb je er een nodig?",
            "description": "Wat een halal browser doet, wat hij niet kan en hoe je er een kiest: sites blokkeren, SafeSearch, afbeeldingen wazig maken en privacy uitgelegd.",
            "body": """<p>Een halal browser is een webbrowser die filtert wat een gewone browser aan jou overlaat. Hij blokkeert sites en zoekopdrachten over bijvoorbeeld 18+-inhoud, alcohol en gokken, en houdt ongewenste afbeeldingen van je scherm.</p>
<h2>Wat een halal browser meestal doet</h2>
<ul>
<li><strong>Sites blokkeren.</strong> 18+-, gok-, alcohol- en drugssites gaan niet open.</li>
<li><strong>SafeSearch afdwingen.</strong> Zoekmachines verbergen expliciete resultaten, zonder dat je iets hoeft in te stellen.</li>
<li><strong>Afbeeldingen filteren.</strong> Afbeeldingen met naakt worden wazig.</li>
<li><strong>Reclame en trackers blokkeren.</strong> Veel ongewenste beelden komen via reclame binnen, dus dit helpt dubbel.</li>
</ul>
<h2>Wat hij niet kan</h2>
<p>Geen enkel filter is perfect. Sommige pagina's komen erdoor en sommige onschuldige pagina's worden geblokkeerd. Een browser beschermt ook alleen wat in die browser gebeurt: andere apps en browsers op hetzelfde apparaat vallen erbuiten. Hij helpt bij je intentie en gewoontes, maar vervangt die niet, en ook niet de aandacht van een ouder.</p>
<h2>Hoe je er een kiest</h2>
<ul>
<li><strong>Waar gebeurt de controle?</strong> Filteren op je eigen apparaat betekent dat je afbeeldingen dat apparaat niet hoeven te verlaten.</li>
<li><strong>Wat gaat er van je apparaat af?</strong> Zoek een duidelijke lijst. Een browser die "niets" zegt, moet kunnen uitleggen hoe hij sites blokkeert en zichzelf bijwerkt.</li>
<li><strong>Kun je het zelf regelen?</strong> Je moet elke bescherming kunnen zien en wijzigen.</li>
<li><strong>Werkt hij op jouw apparaten?</strong> Controleer dat vooraf, zeker op een iPhone of Mac.</li>
</ul>
<h2>Halal browser, browserextensie of DNS-filter?</h2>
<p>Er zijn drie gangbare manieren om het web te filteren, en ze werken het best samen:</p>
<ul>
<li><strong>Een halal browser</strong> filtert in de browser zelf: sites, zoekopdrachten, afbeeldingen en video. De bescherming staat vanaf de eerste pagina aan en kan op slot met een pincode.</li>
<li><strong>Een browserextensie</strong> voegt een filter toe aan een browser die je al gebruikt, zoals Chrome. Snel te proberen, maar meestal makkelijk te verwijderen of uit te zetten, en de browser zelf verandert niet.</li>
<li><strong>Een DNS- of routerfilter</strong> blokkeert hele sites voor elke app op een apparaat of netwerk. Het kan niet in een pagina kijken, dus geen afbeelding wazig maken of muziek uit een video halen.</li>
</ul>
<p>Voor een gezin is een gangbare opzet: een gezins-DNS op de router plus een halal browser op elk apparaat, met andere browsers verwijderd of geblokkeerd. Lees <a href="/nl/blog/block-haram-content/">hoe je haram inhoud blokkeert op je telefoon en computer</a>.</p>
<h2>Checklist voor het kiezen van een halal browser</h2>
<ul>
<li>Worden 18+-, gok-, alcohol- en drugssites vanaf de eerste pagina geblokkeerd, zonder instellen?</li>
<li>Wordt SafeSearch afgedwongen op elke zoekmachine, ook YouTube?</li>
<li>Worden afbeeldingen op je apparaat gecontroleerd, of naar een server gestuurd?</li>
<li>Kan een ouder de instellingen vergrendelen met een pincode?</li>
<li>Staat er duidelijk wat er van je apparaat af gaat?</li>
<li>Wordt hij nog bijgewerkt? Een browser zonder updates krijgt ook geen beveiligingsfixes meer. SalamWeb, een van de eerste halal browsers, is in 2021 gestopt.</li>
</ul>
<p>We vergelijken de opties in <a href="/nl/blog/best-halal-browsers/">de beste halal browsers van {YEAR}</a>.</p>
<h2>Veelgestelde vragen</h2>
<h3>Is een halal browser alleen voor moslims?</h3>
<p>Nee. Iedereen die minder reclame, geen 18+-inhoud en meer controle over afbeeldingen wil, kan er een gebruiken. De naam beschrijft de waarden waarop hij is gebouwd.</p>
<h3>Is een halal browser gratis?</h3>
<p>Vaak wel. De bescherming van AkhiBrowser is gratis, met een optionele Premium voor extra afbeeldingsopties en ouderfuncties.</p>
<h3>Vervangt een halal browser ouderlijk toezicht?</h3>
<p>Hij dekt de browser. Combineer hem voor apps en andere browsers met het toezicht van het apparaat, zoals Google Family Link of Microsoft Family Safety. Zie <a href="/nl/blog/parental-controls-for-muslim-families/">een eenvoudige opzet voor ouderlijk toezicht</a>.</p>
<h3>Kan een halal browser muziek uit video's halen?</h3>
<p>Sommige wel. AkhiBrowser <a href="/nl/blog/remove-background-music-from-videos/">haalt achtergrondmuziek weg op je apparaat</a>: de stemmen blijven, de muziek gaat.</p>
<p>AkhiBrowser is een van de opties, gebouwd op Firefox voor Windows en Android. De bescherming staat meteen aan en <a href="/nl/privacy/">de site vertelt wat er van je apparaat af gaat</a>. Lees ook <a href="/nl/compare/kahf-browser/">de vergelijking met Kahf Browser</a>.</p>""",
        },
    },
    {
        "slug": "block-haram-content",
        "date": DATE,
        "en": {
            "title": "How to block haram content on your phone and computer",
            "description": "A step-by-step way to block adult, gambling and alcohol content: browser filters, SafeSearch, family DNS and device controls, and what each one misses.",
            "body": """<p>No single setting blocks everything. What works is a few layers, each covering what the others miss.</p>
<h2>1. Use a browser that filters by default</h2>
<p>A filtering browser blocks sites, filters searches and blurs images without setup. In AkhiBrowser, adult, alcohol, drugs, vaping and gambling sites are blocked from the first page.</p>
<h2>2. Force SafeSearch</h2>
<p>SafeSearch hides explicit results in search engines. You can turn it on in each search engine's settings, but it's easy to turn off again, and it's per browser. A filtering browser can force it: AkhiBrowser does so on Google, Bing, DuckDuckGo and Yahoo, and turns on YouTube's Restricted Mode.</p>
<h2>3. Add a family DNS</h2>
<p>A family DNS service refuses to look up adult sites, for everything on that network or device. Cloudflare's 1.1.1.3 and CleanBrowsing are well-known options. It works by site name, so it can't see what's on an allowed site, and whoever runs it can see the names of the sites you visit.</p>
<h2>4. Close the side doors</h2>
<p>A browser filter doesn't cover other apps. On a child's device, use Google Family Link on Android or Microsoft Family Safety on Windows to control which apps and browsers can be installed. On AkhiBrowser, Family Premium can also lock the settings with a PIN and turn off private tabs.</p>
<h2>5. Keep the conversation going</h2>
<p>Filters miss things, and they don't work on a friend's phone. For children, knowing what to do when something appears on the screen matters more than any setting.</p>""",
        },
        "nl": {
            "title": "Zo blokkeer je haram inhoud op je telefoon en computer",
            "description": "Stap voor stap 18+-, gok- en alcoholinhoud blokkeren: browserfilters, SafeSearch, family-DNS en apparaatinstellingen, en wat elk daarvan mist.",
            "body": """<p>Geen enkele instelling blokkeert alles. Wat werkt, zijn een paar lagen die elkaars gaten dichten.</p>
<h2>1. Gebruik een browser die standaard filtert</h2>
<p>Een filterende browser blokkeert sites, filtert zoekopdrachten en maakt afbeeldingen wazig zonder dat je iets instelt. In AkhiBrowser zijn 18+-sites en sites over alcohol, drugs, vapen en gokken vanaf de eerste pagina geblokkeerd.</p>
<h2>2. Dwing SafeSearch af</h2>
<p>SafeSearch verbergt expliciete resultaten in zoekmachines. Je kunt het per zoekmachine aanzetten, maar het staat ook zo weer uit en geldt per browser. Een filterende browser kan het afdwingen: AkhiBrowser doet dat op Google, Bing, DuckDuckGo en Yahoo, en zet de beperkte modus van YouTube aan.</p>
<h2>3. Voeg een family-DNS toe</h2>
<p>Een family-DNS weigert 18+-sites op te zoeken, voor alles op dat netwerk of apparaat. Cloudflare 1.1.1.3 en CleanBrowsing zijn bekende opties. Dit werkt op sitenaam, dus het ziet niet wat er op een toegestane site staat, en de aanbieder kan de namen zien van de sites die je bezoekt.</p>
<h2>4. Sluit de zijdeuren</h2>
<p>Een browserfilter dekt geen andere apps. Gebruik op het apparaat van een kind Google Family Link op Android of Microsoft Family Safety op Windows om te bepalen welke apps en browsers geïnstalleerd mogen worden. In AkhiBrowser kan Family Premium de instellingen ook met een pincode vergrendelen en privétabbladen uitzetten.</p>
<h2>5. Blijf erover praten</h2>
<p>Filters missen dingen en werken niet op de telefoon van een vriend. Voor kinderen is weten wat ze moeten doen als er iets op het scherm verschijnt belangrijker dan welke instelling dan ook.</p>""",
        },
    },
    {
        "slug": "remove-background-music-from-videos",
        "date": DATE,
        "en": {
            "title": "How to remove background music from videos in your browser",
            "description": "How on-device voice separation takes background music out of online videos and keeps the speech, where it works well, and where it struggles.",
            "body": """<p>Many lectures, documentaries and news clips have background music you may prefer not to hear. Muting isn't an option when you want the speech. Voice separation solves this: a small speech model keeps the voices and removes the rest.</p>
<p>Scholars differ on music, and this article doesn't try to settle that. It only explains what the technology can do, for those who want it.</p>
<h2>How it works</h2>
<p>A speech model listens to a video's sound in short slices and estimates which part is a human voice. The rest is taken out before it reaches your speakers. Running it on your device means the audio doesn't have to be sent anywhere.</p>
<h2>How to use it in AkhiBrowser</h2>
<ol>
<li>Install AkhiBrowser on Windows or Android.</li>
<li>Play a video. No music is on by default.</li>
<li>To turn it off, open the AkhiBrowser shield in the toolbar. On Android: menu, then Extensions, then AkhiBrowser.</li>
</ol>
<p>Phones and slower computers use a lighter model, so they can keep up.</p>
<h2>Where it works less well</h2>
<ul>
<li><strong>Singing.</strong> A singing voice is still a voice, so the model has to decide what to do with it.</li>
<li><strong>Loud music over quiet speech.</strong> Some music can remain, and the voice can sound thinner.</li>
<li><strong>Sites that block access to their audio.</strong> Some protected videos can't be processed.</li>
</ul>
<p>The feature builds on <a href="https://github.com/mohamedsadiqaguenaou/NoMusic">NoMusic by Mohamed Sadiq</a>.</p>""",
        },
        "nl": {
            "title": "Zo haal je achtergrondmuziek uit video's in je browser",
            "description": "Hoe stemscheiding op je eigen apparaat de achtergrondmuziek uit online video's haalt en de spraak bewaart, waar het goed werkt en waar het lastig is.",
            "body": """<p>Veel lezingen, documentaires en nieuwsfragmenten hebben achtergrondmuziek die je misschien liever niet hoort. Het geluid uitzetten kan niet als je de spraak wilt volgen. Stemscheiding lost dit op: een klein spraakmodel bewaart de stemmen en haalt de rest weg.</p>
<p>Geleerden verschillen van mening over muziek, en dit artikel probeert dat niet te beslechten. Het legt alleen uit wat de techniek kan, voor wie dat wil.</p>
<h2>Hoe het werkt</h2>
<p>Een spraakmodel luistert in korte stukjes naar het geluid van een video en schat welk deel een menselijke stem is. De rest wordt eruit gehaald voordat het je speakers bereikt. Omdat dit op je apparaat gebeurt, hoeft het geluid nergens naartoe.</p>
<h2>Zo gebruik je het in AkhiBrowser</h2>
<ol>
<li>Installeer AkhiBrowser op Windows of Android.</li>
<li>Speel een video af. Geen muziek staat standaard aan.</li>
<li>Uitzetten doe je via het AkhiBrowser-schild in de werkbalk. Op Android: menu, dan Extensies, dan AkhiBrowser.</li>
</ol>
<p>Telefoons en tragere computers gebruiken een lichter model, zodat ze het aankunnen.</p>
<h2>Waar het minder goed werkt</h2>
<ul>
<li><strong>Zang.</strong> Een zingende stem is nog steeds een stem, dus het model moet bepalen wat het ermee doet.</li>
<li><strong>Harde muziek onder zachte spraak.</strong> Er kan muziek overblijven en de stem kan dunner klinken.</li>
<li><strong>Sites die hun geluid afschermen.</strong> Sommige beveiligde video's kunnen niet worden bewerkt.</li>
</ul>
<p>De functie bouwt voort op <a href="https://github.com/mohamedsadiqaguenaou/NoMusic">NoMusic van Mohamed Sadiq</a>.</p>""",
        },
    },
    {
        "slug": "parental-controls-for-muslim-families",
        "date": DATE,
        "en": {
            "title": "Parental controls for Muslim families: a simple setup",
            "description": "A simple setup for parents: a filtering browser, a PIN, approved sites for young children, bedtime and school hours, and what no browser can control.",
            "body": """<p>Good parental controls match a child's age. These are sensible starting points, using the Family Premium controls in AkhiBrowser. Each one is off until you turn it on, and the data stays on the device.</p>
<h2>First, for every age</h2>
<ol>
<li>Set a parental PIN, so the protections can't be turned off without it.</li>
<li>Turn on <strong>No private tabs</strong>, so browsing stays under the controls.</li>
<li>Remove other browsers from the device, or block them with Google Family Link or Microsoft Family Safety. A browser can't control what happens outside it.</li>
</ol>
<h2>Young children</h2>
<p>Use <strong>Allow only approved sites</strong> and add the few sites they use. Everything else stays closed, which is much stronger than trying to block the bad parts of the web.</p>
<h2>Older children</h2>
<p>Open the web, but set limits. <strong>Block chosen sites</strong> covers specific sites that cause trouble, and <strong>Time limits</strong> sets a daily limit, bedtime and school hours. The <strong>Feed limit</strong> hides short-video feeds and stops social websites after a set time. It works on websites in AkhiBrowser, not in social-media apps.</p>
<h2>Teenagers</h2>
<p>Trust grows with age. The <strong>Activity summary</strong> shows how many pages were blocked and why, without their addresses. It's a start for a conversation, not surveillance.</p>
<h2>When you need a break</h2>
<p><strong>Pause the internet</strong> stops browsing right away, with the PIN to resume. It's useful at mealtimes and around prayer.</p>
<p>See the <a href="/#premium">plans and prices</a>. The free protections work without any of this.</p>""",
        },
        "nl": {
            "title": "Ouderlijk toezicht voor moslimgezinnen: een eenvoudige opzet",
            "description": "Een eenvoudige opzet voor ouders: een filterende browser, een pincode, goedgekeurde sites voor jonge kinderen, bedtijd en schooluren, en wat geen browser kan regelen.",
            "body": """<p>Goed ouderlijk toezicht past bij de leeftijd van een kind. Dit zijn verstandige beginpunten, met de Family Premium-functies van AkhiBrowser. Elke functie staat uit tot je hem aanzet en de gegevens blijven op het apparaat.</p>
<h2>Eerst, voor elke leeftijd</h2>
<ol>
<li>Stel een ouderpincode in, zodat de bescherming niet zonder pincode uit kan.</li>
<li>Zet <strong>Geen privétabbladen</strong> aan, zodat het surfen onder het toezicht blijft.</li>
<li>Verwijder andere browsers van het apparaat, of blokkeer ze met Google Family Link of Microsoft Family Safety. Een browser kan niet regelen wat erbuiten gebeurt.</li>
</ol>
<h2>Jonge kinderen</h2>
<p>Gebruik <strong>Alleen goedgekeurde sites toestaan</strong> en voeg de paar sites toe die ze gebruiken. De rest blijft dicht, wat veel sterker is dan proberen de slechte delen van het web te blokkeren.</p>
<h2>Oudere kinderen</h2>
<p>Laat het web open, maar stel grenzen. <strong>Gekozen sites blokkeren</strong> is voor sites die problemen geven, en <strong>Tijdslimieten</strong> regelt een dagelijkse limiet, bedtijd en schooluren. De <strong>Feedlimiet</strong> verbergt korte video's en stopt sociale websites na een ingestelde tijd. Dat werkt op websites in AkhiBrowser, niet in sociale apps.</p>
<h2>Tieners</h2>
<p>Vertrouwen groeit met de leeftijd. Het <strong>Activiteitenoverzicht</strong> laat zien hoeveel pagina's zijn geblokkeerd en waarom, zonder adressen. Het is een begin van een gesprek, geen controlemiddel.</p>
<h2>Als je even pauze nodig hebt</h2>
<p><strong>Internet pauzeren</strong> stopt het surfen meteen, en met de pincode ga je verder. Handig bij het eten en rond het gebed.</p>
<p>Bekijk de <a href="/#premium">abonnementen en prijzen</a>. De gratis bescherming werkt ook zonder dit alles.</p>""",
        },
    },
    {
        "slug": "why-prayer-times-differ",
        "date": DATE,
        "en": {
            "title": "Why prayer times differ between apps and mosques",
            "description": "Why Fajr and Isha can differ by more than half an hour between apps: calculation methods explained, with a real example from Almere in the Netherlands.",
            "body": """<p>Two apps can show different times for the same prayer in the same city. Usually neither is broken: they use a different calculation method.</p>
<h2>What stays the same, and what changes</h2>
<p>Dhuhr and Maghrib follow the sun's position, so methods mostly agree on them. Fajr and Isha depend on twilight, when the sun is a certain angle below the horizon, and methods choose different angles. Asr also differs by school: the Hanafi time is later than the standard one.</p>
<h2>A real example</h2>
<p>These are the times for Almere, the Netherlands, on 8 November 2026, from the public <a href="https://aladhan.com/prayer-times-api">Aladhan calculation service</a>:</p>
<div class="table"><table>
<thead><tr><th scope="col">Method</th><th scope="col">Fajr</th><th scope="col">Isha</th></tr></thead>
<tbody>
<tr><th scope="row">Morocco</th><td>05:43</td><td>18:48</td></tr>
<tr><th scope="row">Muslim World League</th><td>05:50</td><td>18:48</td></tr>
<tr><th scope="row">Karachi</th><td>05:50</td><td>18:55</td></tr>
<tr><th scope="row">Moonsighting Committee</th><td>06:09</td><td>18:26</td></tr>
<tr><th scope="row">ISNA</th><td>06:10</td><td>18:35</td></tr>
<tr><th scope="row">France (UOIF)</th><td>06:30</td><td>18:15</td></tr>
</tbody>
</table></div>
<p>That's 47 minutes between the earliest and latest Fajr. Far from the equator the gaps change with the seasons, and in summer true twilight may not happen at all, so methods also need rules for high latitudes.</p>
<h2>Which one should you use?</h2>
<p>For a question of practice, ask your local mosque or a scholar you trust, and follow what your community uses. An app can only do the sums.</p>
<h2>Prayer times in AkhiBrowser</h2>
<p>AkhiBrowser works out prayer times on your device from the city you choose, without using your location. It picks a method from the country, and you can change the method and the Asr time in its options.</p>""",
        },
        "nl": {
            "title": "Waarom gebedstijden verschillen tussen apps en moskeeën",
            "description": "Waarom Fajr en Isha meer dan een halfuur kunnen verschillen tussen apps: rekenmethoden uitgelegd, met een echt voorbeeld uit Almere.",
            "body": """<p>Twee apps kunnen in dezelfde stad verschillende tijden tonen voor hetzelfde gebed. Meestal is geen van beide kapot: ze gebruiken een andere rekenmethode.</p>
<h2>Wat gelijk blijft en wat verandert</h2>
<p>Dhuhr en Maghrib volgen de stand van de zon, dus daar zijn methoden het meestal over eens. Fajr en Isha hangen af van de schemering, wanneer de zon een bepaalde hoek onder de horizon staat, en methoden kiezen verschillende hoeken. Ook Asr verschilt per school: de Hanafi-tijd is later dan de standaardtijd.</p>
<h2>Een echt voorbeeld</h2>
<p>Dit zijn de tijden voor Almere op 8 november 2026, van de openbare <a href="https://aladhan.com/prayer-times-api">rekendienst Aladhan</a>:</p>
<div class="table"><table>
<thead><tr><th scope="col">Methode</th><th scope="col">Fajr</th><th scope="col">Isha</th></tr></thead>
<tbody>
<tr><th scope="row">Marokko</th><td>05:43</td><td>18:48</td></tr>
<tr><th scope="row">Muslim World League</th><td>05:50</td><td>18:48</td></tr>
<tr><th scope="row">Karachi</th><td>05:50</td><td>18:55</td></tr>
<tr><th scope="row">Moonsighting Committee</th><td>06:09</td><td>18:26</td></tr>
<tr><th scope="row">ISNA</th><td>06:10</td><td>18:35</td></tr>
<tr><th scope="row">Frankrijk (UOIF)</th><td>06:30</td><td>18:15</td></tr>
</tbody>
</table></div>
<p>Dat is 47 minuten tussen de vroegste en de laatste Fajr. Ver van de evenaar veranderen de verschillen met de seizoenen, en in de zomer is er soms geen echte schemering, dus methoden hebben ook regels nodig voor noordelijke gebieden.</p>
<h2>Welke moet je gebruiken?</h2>
<p>Dit is een vraag over de praktijk: vraag het je moskee of een geleerde die je vertrouwt, en volg wat je gemeenschap gebruikt. Een app kan alleen rekenen.</p>
<h2>Gebedstijden in AkhiBrowser</h2>
<p>AkhiBrowser berekent de gebedstijden op je apparaat voor de stad die je kiest, zonder je locatie te gebruiken. Hij kiest een methode op basis van het land, en je kunt de methode en de Asr-tijd wijzigen in de opties.</p>""",
        },
    },
    {
        "slug": "best-halal-browsers",
        "date": "2026-11-10",
        "en": {
            "title": "The best halal browsers in {YEAR}, compared",
            "description": "An honest comparison of the halal browsers you can use in {YEAR}: AkhiBrowser, Kahf Browser and Tahir Browser, plus what happened to SalamWeb. Platforms, price and features.",
            "body": """<p>A halal browser blocks haram sites, forces SafeSearch and keeps unwanted images off your screen. In {YEAR} there are three active options worth knowing. We make one of them, AkhiBrowser, so this page sticks to what each browser states on its own pages, and says plainly where each one fits best.</p>
<h2>The short answer</h2>
<ul>
<li><strong>On Windows, or for parent controls:</strong> AkhiBrowser. Free protections, background music removal, and Family Premium with a PIN, site lists and time limits.</li>
<li><strong>On a Mac, or for an all-free browser on every platform:</strong> Kahf Browser. Windows, macOS, Android and iOS, free with no in-app purchases.</li>
<li><strong>On an iPhone:</strong> Tahir Browser or Kahf Browser. AkhiBrowser isn't on iOS yet.</li>
</ul>
<h2>AkhiBrowser</h2>
<p>A halal browser built on Firefox, for Windows now and Android soon. Adult, alcohol, drug, vaping and gambling sites are blocked from the first page, SafeSearch is forced on Google, Bing, DuckDuckGo, Yahoo and YouTube, and images stay blurred until they're checked on your device. It's the only one of the three that removes background music from videos, on your device. The protections are free; Premium adds the choice of who is blurred, and Family Premium adds a parental PIN, site lists, time limits and a pause button.</p>
<h2>Kahf Browser</h2>
<p>A Chromium-based browser for Muslims on Windows, macOS, Android and iOS. Its site says it is free on all platforms with no subscriptions or in-app purchases, blocks ads, adult and haram sites with AI filtering and a database, enforces SafeSearch and Safe YouTube, blurs nudity in real time, and includes prayer times and the qibla. Most Chrome extensions work in it.</p>
<h2>Tahir Browser</h2>
<p>An iPhone and iPad browser by Ihya Tech. Its App Store listing describes blurring all images or using AI to blur the opposite gender, tap-to-unblur, blocking haram sites, ads and trackers, Islamic reminders, forced SafeSearch and a password or biometric lock on its shield. It's free to download, with optional monthly and yearly plans.</p>
<h2>What happened to SalamWeb?</h2>
<p>SalamWeb was one of the first halal browsers and got wide press coverage in 2019. It was discontinued in 2021 and its website is gone, so it's no longer an option. It's a good reminder to choose a browser that's still updated, because updates bring security fixes.</p>
<h2>Side by side</h2>
<div class="table"><table>
<thead><tr><th scope="col"></th><th scope="col">AkhiBrowser</th><th scope="col">Kahf Browser</th><th scope="col">Tahir Browser</th></tr></thead>
<tbody>
<tr><th scope="row">Platforms</th><td>Windows; Android soon</td><td>Windows, macOS, Android, iOS</td><td>iPhone, iPad</td></tr>
<tr><th scope="row">Price</th><td>Protections free; optional Premium</td><td>Free</td><td>Free; optional plans</td></tr>
<tr><th scope="row">Built on</th><td>Firefox</td><td>Chromium</td><td>iOS WebKit</td></tr>
<tr><th scope="row">Haram sites blocked</th><td>Yes</td><td>Yes</td><td>Yes</td></tr>
<tr><th scope="row">SafeSearch forced</th><td>Yes, incl. YouTube</td><td>Yes, incl. YouTube</td><td>Yes</td></tr>
<tr><th scope="row">Image blurring</th><td>Until checked, on your device</td><td>Real time</td><td>All images, or AI by gender</td></tr>
<tr><th scope="row">Background music removal</th><td>Yes</td><td>Not stated</td><td>Not stated</td></tr>
<tr><th scope="row">Parental PIN and time limits</th><td>Family Premium</td><td>Not stated</td><td>Lock on shield</td></tr>
</tbody>
</table></div>
<p>&quot;Not stated&quot; means we didn't find it on the browser's own pages, not that it doesn't exist. For a longer table, see <a href="/compare/kahf-browser/">AkhiBrowser and Kahf Browser compared</a> and <a href="/compare/browsers/">AkhiBrowser, Kahf, Brave, Firefox and Chrome compared</a>. New to the idea? Start with <a href="/blog/what-is-a-halal-browser/">what a halal browser is</a>.</p>
<p>Checked against each browser's own pages on 10 November 2026. Spotted something out of date? Tell us at <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>.</p>""",
        },
        "nl": {
            "title": "De beste halal browsers van {YEAR}, vergeleken",
            "description": "Een eerlijke vergelijking van de halal browsers die je in {YEAR} kunt gebruiken: AkhiBrowser, Kahf Browser en Tahir Browser, plus wat er met SalamWeb gebeurde.",
            "body": """<p>Een halal browser blokkeert haram sites, dwingt SafeSearch af en houdt ongewenste afbeeldingen van je scherm. In {YEAR} zijn er drie actieve opties die de moeite waard zijn. Wij maken er een van, AkhiBrowser, dus deze pagina houdt zich aan wat elke browser op de eigen pagina's vermeldt, en zegt eerlijk waar elke browser het best past.</p>
<h2>Het korte antwoord</h2>
<ul>
<li><strong>Op Windows, of voor ouderlijk toezicht:</strong> AkhiBrowser. Gratis bescherming, muziek weghalen uit video's, en Family Premium met pincode, sitelijsten en tijdslimieten.</li>
<li><strong>Op een Mac, of voor een volledig gratis browser op elk platform:</strong> Kahf Browser. Windows, macOS, Android en iOS, gratis zonder in-app-aankopen.</li>
<li><strong>Op een iPhone:</strong> Tahir Browser of Kahf Browser. AkhiBrowser is nog niet op iOS.</li>
</ul>
<h2>AkhiBrowser</h2>
<p>Een halal browser op basis van Firefox, nu voor Windows en binnenkort voor Android. 18+-, alcohol-, drugs-, vape- en goksites zijn vanaf de eerste pagina geblokkeerd, SafeSearch wordt afgedwongen op Google, Bing, DuckDuckGo, Yahoo en YouTube, en afbeeldingen blijven wazig tot ze op je apparaat zijn gecontroleerd. Het is de enige van de drie die achtergrondmuziek uit video's haalt, op je apparaat. De bescherming is gratis; Premium laat je kiezen wie wazig wordt, en Family Premium voegt een ouderpincode, sitelijsten, tijdslimieten en een pauzeknop toe.</p>
<h2>Kahf Browser</h2>
<p>Een browser voor moslims op basis van Chromium, voor Windows, macOS, Android en iOS. Volgens de eigen site is hij gratis op alle platforms zonder abonnementen of in-app-aankopen, blokkeert hij reclame, 18+- en haram sites met AI en een database, dwingt hij SafeSearch en Safe YouTube af, maakt hij naakt direct wazig, en heeft hij gebedstijden en de qibla. De meeste Chrome-extensies werken erin.</p>
<h2>Tahir Browser</h2>
<p>Een browser voor iPhone en iPad van Ihya Tech. De App Store-pagina noemt het wazig maken van alle afbeeldingen of met AI van het andere geslacht, tikken om te tonen, haram sites, reclame en trackers blokkeren, islamitische herinneringen, afgedwongen SafeSearch en een wachtwoord- of biometrisch slot op het schild. Gratis te downloaden, met optionele maand- en jaarabonnementen.</p>
<h2>Wat is er met SalamWeb gebeurd?</h2>
<p>SalamWeb was een van de eerste halal browsers en kreeg in 2019 veel aandacht in de pers. De browser is in 2021 gestopt en de website bestaat niet meer. Een goede reden om een browser te kiezen die nog wordt bijgewerkt, want updates brengen beveiligingsfixes.</p>
<h2>Naast elkaar</h2>
<div class="table"><table>
<thead><tr><th scope="col"></th><th scope="col">AkhiBrowser</th><th scope="col">Kahf Browser</th><th scope="col">Tahir Browser</th></tr></thead>
<tbody>
<tr><th scope="row">Platforms</th><td>Windows; Android binnenkort</td><td>Windows, macOS, Android, iOS</td><td>iPhone, iPad</td></tr>
<tr><th scope="row">Prijs</th><td>Bescherming gratis; optioneel Premium</td><td>Gratis</td><td>Gratis; optionele abonnementen</td></tr>
<tr><th scope="row">Gebouwd op</th><td>Firefox</td><td>Chromium</td><td>iOS WebKit</td></tr>
<tr><th scope="row">Haram sites geblokkeerd</th><td>Ja</td><td>Ja</td><td>Ja</td></tr>
<tr><th scope="row">SafeSearch afgedwongen</th><td>Ja, ook YouTube</td><td>Ja, ook YouTube</td><td>Ja</td></tr>
<tr><th scope="row">Afbeeldingen wazig</th><td>Tot gecontroleerd, op je apparaat</td><td>Direct</td><td>Alle, of met AI per geslacht</td></tr>
<tr><th scope="row">Achtergrondmuziek weghalen</th><td>Ja</td><td>Niet vermeld</td><td>Niet vermeld</td></tr>
<tr><th scope="row">Ouderpincode en tijdslimieten</th><td>Family Premium</td><td>Niet vermeld</td><td>Slot op het schild</td></tr>
</tbody>
</table></div>
<p>&quot;Niet vermeld&quot; betekent dat we het niet vonden op de eigen pagina's van de browser, niet dat het niet bestaat. Zie voor een uitgebreidere tabel <a href="/nl/compare/kahf-browser/">AkhiBrowser en Kahf Browser vergeleken</a> en <a href="/nl/compare/browsers/">AkhiBrowser, Kahf, Brave, Firefox en Chrome vergeleken</a>. Nieuw met het idee? Begin bij <a href="/nl/blog/what-is-a-halal-browser/">wat een halal browser is</a>.</p>
<p>Gecontroleerd op de eigen pagina's van elke browser op 10 november 2026. Iets verouderd? Laat het ons weten via <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>.</p>""",
        },
    },
]
_NS_EN = "Not stated"
_NS_NL = "Niet vermeld"

COMPARE = {
    "sources": [
        ("kahfbrowser.com", "https://kahfbrowser.com/"),
        ("FAQ", "https://kahfbrowser.com/faq/"),
        ("Download", "https://kahfbrowser.com/download/"),
        ("Best halal browsers", "https://kahfbrowser.com/best-halal-browsers/"),
    ],
    "en": {
        "seo_title": "AkhiBrowser vs Kahf Browser: features, price and platforms compared",
        "title": "AkhiBrowser and Kahf Browser compared",
        "description": "A side-by-side look at AkhiBrowser and Kahf Browser: price, platforms, filtering, images, music removal, prayer times and parental controls, from each browser's own pages.",
        "lead": "Both are browsers for Muslims. This table lists what each one states on its own website, as of 8 November 2026. We haven't tested Kahf Browser ourselves. &quot;Not stated&quot; means we didn't find it on the pages we read, not that the feature doesn't exist.",
        "head": ["", "AkhiBrowser", "Kahf Browser"],
        "rows": [
            ["Price", "Protections free. Optional Premium €3.99 a month, €39 a year or €119 once; Family Premium €59.99 a year", "Free on all platforms, with no subscriptions or in-app purchases"],
            ["Platforms", 'Windows, Android. iOS and macOS: <a href="/#roadmap">on the roadmap</a>, no date yet', "Windows, macOS, Android, iOS. Linux: its FAQ lists it, its download page says coming soon"],
            ["Built on", "Firefox", "Chromium; most Chrome extensions work"],
            ["Source code", "Firefox changes and MPL files are public; its own extension is private", "Not public yet, per its FAQ"],
            ["Account needed", "No", "No; sign-in is available"],
            ["Ads and trackers", "Blocked, with uBlock Origin and a built-in blocker", "Built-in blocker"],
            ["Adult and haram sites", "Blocked: adult, alcohol, drugs, vaping and gambling", "Blocked, with AI-powered filtering and a database"],
            ["Phishing and scam sites", "Blocked", "Blocked"],
            ["SafeSearch", "Forced on Google, Bing, DuckDuckGo and Yahoo, plus YouTube Restricted Mode", "Enforced across major search engines; Safe YouTube"],
            ["Nudity in images", "Blurred until checked on your device: images, backgrounds, video and canvases", "Blurred in real time"],
            ["Choose who to blur (women, men)", "Premium", _NS_EN],
            ["Recognize hijab", "Premium", _NS_EN],
            ["Remove background music from videos", "Free, on your device", _NS_EN],
            ["Prayer times", "Free, for a city you choose, without your location; reminders on computers", "Prayer times and notifications"],
            ["Qibla", "No", "Yes"],
            ["Verse of the day", "Free", _NS_EN],
            ["Parental PIN, site lists, time limits", "Family Premium", _NS_EN],
            ["Pause the internet", "Family Premium", _NS_EN],
            ["Languages", "12, including Arabic, Urdu, Persian, Kurdish and Turkish", _NS_EN],
        ],
        "after": """<h2>Which one fits you?</h2>
<p><strong>Kahf Browser</strong> fits if you use an iPhone or a Mac, or want everything free.</p>
<p><strong>AkhiBrowser</strong> fits if you want background music removed, want to choose who is blurred, or need parent controls such as a PIN and time limits, on Windows or Android.</p>
<p>Both are free to try, so the best test is your own use. AkhiBrowser isn't affiliated with Kahf. Spotted something out of date? Tell us at <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a> and we'll correct it.</p>""",
        "sources_label": "Kahf Browser's pages we read:",
    },
    "nl": {
        "seo_title": "AkhiBrowser vs Kahf Browser: functies, prijs en platforms vergeleken",
        "title": "AkhiBrowser en Kahf Browser vergeleken",
        "description": "AkhiBrowser en Kahf Browser naast elkaar: prijs, platforms, filters, afbeeldingen, muziek weghalen, gebedstijden en ouderlijk toezicht, volgens de eigen pagina's van elke browser.",
        "lead": "Beide zijn browsers voor moslims. Deze tabel laat zien wat elk op de eigen website vermeldt, op 8 november 2026. We hebben Kahf Browser niet zelf getest. &quot;Niet vermeld&quot; betekent dat we het niet vonden op de pagina's die we lazen, niet dat de functie niet bestaat.",
        "head": ["", "AkhiBrowser", "Kahf Browser"],
        "rows": [
            ["Prijs", "Bescherming gratis. Optioneel Premium €3,99 per maand, €39 per jaar of €119 eenmalig; Family Premium €59,99 per jaar", "Gratis op alle platforms, zonder abonnementen of in-app-aankopen"],
            ["Platforms", 'Windows, Android. iOS en macOS: <a href="/#roadmap">op de roadmap</a>, nog zonder datum', "Windows, macOS, Android, iOS. Linux: de FAQ noemt het, de downloadpagina zegt binnenkort"],
            ["Gebouwd op", "Firefox", "Chromium; de meeste Chrome-extensies werken"],
            ["Broncode", "Firefox-wijzigingen en MPL-bestanden zijn openbaar; de eigen extensie is privé", "Nog niet openbaar, volgens de FAQ"],
            ["Account nodig", "Nee", "Nee; inloggen kan wel"],
            ["Reclame en trackers", "Geblokkeerd, met uBlock Origin en een eigen blokkering", "Ingebouwde blokkering"],
            ["18+- en haram sites", "Geblokkeerd: 18+, alcohol, drugs, vapen en gokken", "Geblokkeerd, met AI-filtering en een database"],
            ["Phishing- en oplichtingssites", "Geblokkeerd", "Geblokkeerd"],
            ["SafeSearch", "Afgedwongen op Google, Bing, DuckDuckGo en Yahoo, plus de beperkte modus van YouTube", "Afgedwongen op grote zoekmachines; Safe YouTube"],
            ["Naakt in afbeeldingen", "Wazig tot de controle op je apparaat: afbeeldingen, achtergronden, video en canvas", "In realtime wazig"],
            ["Kiezen wie wazig wordt (vrouwen, mannen)", "Premium", _NS_NL],
            ["Hijab herkennen", "Premium", _NS_NL],
            ["Achtergrondmuziek uit video's halen", "Gratis, op je apparaat", _NS_NL],
            ["Gebedstijden", "Gratis, voor een stad die je kiest, zonder je locatie; herinneringen op computers", "Gebedstijden en meldingen"],
            ["Qibla", "Nee", "Ja"],
            ["Vers van de dag", "Gratis", _NS_NL],
            ["Ouderpincode, sitelijsten, tijdslimieten", "Family Premium", _NS_NL],
            ["Internet pauzeren", "Family Premium", _NS_NL],
            ["Talen", "12, waaronder Arabisch, Urdu, Perzisch, Koerdisch en Turks", _NS_NL],
        ],
        "after": """<h2>Welke past bij jou?</h2>
<p><strong>Kahf Browser</strong> past als je een iPhone of Mac gebruikt, of alles gratis wilt.</p>
<p><strong>AkhiBrowser</strong> past als je achtergrondmuziek wilt weghalen, wilt kiezen wie wazig wordt, of ouderlijk toezicht nodig hebt zoals een pincode en tijdslimieten, op Windows of Android.</p>
<p>Beide kun je gratis proberen, dus de beste test is je eigen gebruik. AkhiBrowser is niet verbonden aan Kahf. Staat er iets verouderds? Laat het weten via <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>, dan passen we het aan.</p>""",
        "sources_label": "De pagina's van Kahf Browser die we lazen:",
    },
}

_CWS = "https://chromewebstore.google.com/detail/akhibrowser/ghkpflipnhahpjdnpoclaakbecnopamk"
_AMO = "https://addons.mozilla.org/en-US/firefox/addon/akhibrowser/"

COMPARE_BROWSERS = {
    "sources": [
        ("kahfbrowser.com", "https://kahfbrowser.com/"),
        ("Brave Shields", "https://brave.com/shields/"),
        ("Firefox tracking protection", "https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop"),
        ("Google Family Link", "https://families.google/familylink/"),
    ],
    "en": {
        "seo_title": "Halal browser comparison: AkhiBrowser, Kahf Browser, Brave, Firefox and Chrome",
        "title": "AkhiBrowser, Kahf Browser, Brave, Firefox and Chrome compared",
        "description": "Which browser filters haram content, blurs images, removes background music and has parent controls? AkhiBrowser, Kahf Browser, Brave, Firefox and Chrome side by side.",
        "lead": "What each browser does out of the box, without extra extensions, as each one describes it on its own pages, as of 9 November 2026. We haven't tested Kahf Browser ourselves; see <a href=\"/compare/kahf-browser/\">the detailed comparison with Kahf Browser</a>.",
        "head": ["", "AkhiBrowser", "Kahf Browser", "Brave", "Firefox", "Chrome"],
        "rows": [
            ["Price", "Protections free; optional Premium and Family Premium", "Free", "Free", "Free", "Free"],
            ["Platforms", f'Windows (Microsoft Store), Android (coming soon); lighter free extensions for <a href="{_CWS}">Chrome</a> and <a href="{_AMO}">Firefox</a>', "Windows, macOS, Android, iOS", "Windows, macOS, Linux, Android, iOS", "Windows, macOS, Linux, Android, iOS", "Windows, macOS, Linux, Android, iOS"],
            ["Built on", "Firefox", "Chromium", "Chromium", "Firefox's own engine", "Chromium"],
            ["Ads and trackers", "Blocked, uBlock Origin built in", "Blocked", "Blocked (Shields)", "Trackers blocked; ads need an extension", "Not blocked; ad blockers are limited"],
            ["Adult and haram sites", "Blocked, from the first page", "Blocked", "No", "No", "No"],
            ["SafeSearch and YouTube Restricted Mode forced", "Yes", "Yes", "No", "No", "With Family Link supervision"],
            ["Nudity in images", "Blurred until checked on your device", "Blurred", "No", "No", "No"],
            ["Choose who to blur, recognize hijab", "Premium", "Not stated", "No", "No", "No"],
            ["Remove background music from videos", "Free, on your device", "Not stated", "No", "No", "No"],
            ["Prayer times and verse of the day", "Free", "Prayer times", "No", "No", "No"],
            ["Parent controls (PIN, site lists, time limits)", "Family Premium", "Not stated", "No", "No", "With Google Family Link"],
            ["Protections can be turned off by a child", "Not with the parental PIN", "Not stated", "Yes", "Yes", "Depends on Family Link"],
        ],
        "after": """<h2>In short</h2>
<p><strong>Brave, Firefox and Chrome</strong> are good general browsers, but none of them filters haram content or blurs images by itself. You would need extensions, which a child can remove.</p>
<p><strong>Kahf Browser and AkhiBrowser</strong> are made for Muslims and filter from the start. AkhiBrowser adds background music removal, choosing who to blur, and parent controls with a PIN.</p>
<p>Spotted something out of date? Tell us at <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a> and we'll correct it. AkhiBrowser isn't affiliated with any of these browsers.</p>""",
        "sources_label": "Pages we read:",
    },
    "nl": {
        "seo_title": "Halal browsers vergeleken: AkhiBrowser, Kahf Browser, Brave, Firefox en Chrome",
        "title": "AkhiBrowser, Kahf Browser, Brave, Firefox en Chrome vergeleken",
        "description": "Welke browser filtert haram inhoud, maakt afbeeldingen wazig, haalt achtergrondmuziek weg en heeft ouderlijk toezicht? AkhiBrowser, Kahf Browser, Brave, Firefox en Chrome naast elkaar.",
        "lead": "Wat elke browser standaard doet, zonder extra extensies, zoals elk het op de eigen pagina's beschrijft, op 9 november 2026. We hebben Kahf Browser niet zelf getest; zie <a href=\"/nl/compare/kahf-browser/\">de uitgebreide vergelijking met Kahf Browser</a>.",
        "head": ["", "AkhiBrowser", "Kahf Browser", "Brave", "Firefox", "Chrome"],
        "rows": [
            ["Prijs", "Bescherming gratis; optioneel Premium en Family Premium", "Gratis", "Gratis", "Gratis", "Gratis"],
            ["Platforms", f'Windows (Microsoft Store), Android (binnenkort); lichtere gratis extensies voor <a href="{_CWS}">Chrome</a> en <a href="{_AMO}">Firefox</a>', "Windows, macOS, Android, iOS", "Windows, macOS, Linux, Android, iOS", "Windows, macOS, Linux, Android, iOS", "Windows, macOS, Linux, Android, iOS"],
            ["Gebouwd op", "Firefox", "Chromium", "Chromium", "De eigen engine van Firefox", "Chromium"],
            ["Reclame en trackers", "Geblokkeerd, uBlock Origin ingebouwd", "Geblokkeerd", "Geblokkeerd (Shields)", "Trackers geblokkeerd; reclame vraagt een extensie", "Niet geblokkeerd; reclameblokkers zijn beperkt"],
            ["18+- en haram sites", "Geblokkeerd, vanaf de eerste pagina", "Geblokkeerd", "Nee", "Nee", "Nee"],
            ["SafeSearch en beperkte modus van YouTube afgedwongen", "Ja", "Ja", "Nee", "Nee", "Met toezicht via Family Link"],
            ["Naakt in afbeeldingen", "Wazig tot de controle op je apparaat", "Wazig", "Nee", "Nee", "Nee"],
            ["Kiezen wie wazig wordt, hijab herkennen", "Premium", "Niet vermeld", "Nee", "Nee", "Nee"],
            ["Achtergrondmuziek uit video's halen", "Gratis, op je apparaat", "Niet vermeld", "Nee", "Nee", "Nee"],
            ["Gebedstijden en vers van de dag", "Gratis", "Gebedstijden", "Nee", "Nee", "Nee"],
            ["Ouderlijk toezicht (pincode, sitelijsten, tijdslimieten)", "Family Premium", "Niet vermeld", "Nee", "Nee", "Met Google Family Link"],
            ["Kan een kind de bescherming uitzetten?", "Niet met de ouderpincode", "Niet vermeld", "Ja", "Ja", "Hangt af van Family Link"],
        ],
        "after": """<h2>Kort gezegd</h2>
<p><strong>Brave, Firefox en Chrome</strong> zijn goede algemene browsers, maar geen van drieën filtert zelf haram inhoud of maakt afbeeldingen wazig. Daarvoor heb je extensies nodig, en die kan een kind verwijderen.</p>
<p><strong>Kahf Browser en AkhiBrowser</strong> zijn gemaakt voor moslims en filteren vanaf het begin. AkhiBrowser voegt daar achtergrondmuziek weghalen, kiezen wie wazig wordt en ouderlijk toezicht met een pincode aan toe.</p>
<p>Staat er iets verouderds? Laat het weten via <a href="mailto:support@akhibrowser.com">support@akhibrowser.com</a>, dan passen we het aan. AkhiBrowser is niet verbonden aan een van deze browsers.</p>""",
        "sources_label": "Pagina's die we lazen:",
    },
}

# Arabic
import content_ar  # noqa: E402

UI["ar"] = content_ar.UI
for _article in ARTICLES:
    _article["ar"] = content_ar.ARTICLES[_article["slug"]]
COMPARE["ar"] = content_ar.COMPARE
COMPARE_BROWSERS["ar"] = content_ar.COMPARE_BROWSERS
