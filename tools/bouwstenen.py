# -*- coding: utf-8 -*-
"""Bouwstenen voor een pagina.

Elke pagina in tools/content/ krijgt een Pagina-object binnen en roept daarop
methodes aan. De id's van blokken en componenten worden automatisch genummerd,
zodat je die nooit zelf hoeft te verzinnen of uniek te houden.
"""


class Pagina:

    def __init__(self, nummer, artikel_id):
        self._n = nummer
        self._artikel = artikel_id
        self._teller = 0
        self.blokken = []
        self.componenten = []

    # ---------------------------------------------------------------- intern
    def _nieuw_blok(self, naam, klassen=''):
        self._teller += 1
        bid = 'b-%d%02d' % (self._n, self._teller)
        # het eerste blok krijgt geen scheidingslijn, de rest wel
        if klassen == '' and self._teller > 1:
            klassen = 'separator'
        self.blokken.append({
            '_id': bid, '_parentId': self._artikel, '_type': 'block',
            '_classes': klassen, 'title': naam,
            # bewust leeg: anders staat de kop dubbel, op het blok en op de component
            'displayTitle': '', 'body': '', 'instruction': ''
        })
        return bid, 'c-%d%02d' % (self._n, self._teller)

    def _component(self, basis, blok_naam, klassen=''):
        bid, cid = self._nieuw_blok(blok_naam, klassen)
        basis.update({'_id': cid, '_parentId': bid, '_type': 'component'})
        self.componenten.append(basis)
        return basis

    # ------------------------------------------------------------- publiek
    def tekst(self, kop, body, klassen=''):
        """Gewone tekstblok. body is HTML."""
        return self._component({
            '_component': 'text', '_classes': klassen, '_layout': 'full',
            'title': kop or 'Tekst', 'displayTitle': kop, 'body': body, 'instruction': ''
        }, kop or 'Tekst')

    def aandacht(self, kop, body):
        """Tekstblok met accentrand. Voor waarschuwingen en kanttekeningen."""
        return self.tekst(kop, body, klassen='attention')

    def beeld(self, bestand, alt, onderschrift='', kop=''):
        """Afbeelding uit src/course/nl/images/.

        alt is verplicht: zonder alternatieve tekst is de pagina niet toegankelijk.
        """
        assert alt and alt.strip(), 'beeld() zonder alt-tekst: %s' % bestand
        src = 'course/nl/images/' + bestand
        return self._component({
            '_component': 'graphic', '_classes': '', '_layout': 'full',
            'title': kop or 'Afbeelding', 'displayTitle': kop, 'body': '', 'instruction': '',
            '_graphic': {'large': src, 'small': src, 'alt': alt,
                         'attribution': onderschrift, '_url': '', '_target': ''}
        }, kop or 'Afbeelding')

    def accordeon(self, kop, body, items):
        """Uitklapbare items. items = [{'title': ..., 'body': ...}, ...]"""
        return self._component({
            '_component': 'accordion', '_classes': '', '_layout': 'full',
            'title': kop, 'displayTitle': kop, 'body': body,
            'instruction': 'Klik op een kop om die open te klappen.',
            '_shouldCollapseItems': False, '_items': items
        }, kop)

    def vraag(self, kop, vraagtekst, antwoorden, feedback, meerkeuze=False):
        """Meerkeuzevraag. antwoorden = [(tekst, juist), ...]

        De opties worden geschud: anders staat het juiste antwoord vaak vooraan
        en is de vraag te raden.
        """
        items = [{'text': t, '_shouldBeSelected': bool(j)} for t, j in antwoorden]
        aantal_juist = sum(1 for _, j in antwoorden if j)
        return self._component({
            '_component': 'mcq', '_classes': '', '_layout': 'full',
            'title': kop, 'displayTitle': kop, 'body': vraagtekst,
            'instruction': ('Kies %d antwoorden en klik op Nakijken.' % aantal_juist
                            if meerkeuze else 'Kies één antwoord en klik op Nakijken.'),
            'ariaQuestion': vraagtekst,
            '_attempts': 1, '_shouldDisplayAttempts': False,
            '_isRandom': True, '_hasItemScoring': False, '_questionWeight': 1,
            '_selectable': aantal_juist if meerkeuze else 1,
            '_canShowModelAnswer': True, '_canShowFeedback': True,
            '_canShowMarking': True, '_recordInteraction': True,
            '_items': items, '_feedback': feedback
        }, kop)

    def koppelvraag(self, kop, vraagtekst, rijen, opties, feedback):
        """Koppelvraag. rijen = [(uitspraak, juiste optie), ...]; opties = alle keuzes."""
        items = [{'text': tekst,
                  '_options': [{'text': o, '_isCorrect': (o == juist)} for o in opties]}
                 for tekst, juist in rijen]
        return self._component({
            '_component': 'matching', '_classes': '', '_layout': 'full',
            'title': kop, 'displayTitle': kop, 'body': vraagtekst,
            'instruction': 'Kies bij elke regel het juiste antwoord en klik op Nakijken.',
            '_attempts': 1, '_shouldDisplayAttempts': False,
            '_isRandom': True, '_hasItemScoring': False, '_questionWeight': 1,
            '_canShowModelAnswer': True, '_canShowFeedback': True,
            '_canShowMarking': True, '_recordInteraction': True,
            '_items': items, '_feedback': feedback
        }, kop)

    def invulvelden(self, kop, body, velden):
        """Vrije invulvelden die de student zelf bewaart.

        velden = [(id, label, hint), ...] — id moet uniek zijn in de hele cursus.

        Bewust gewone textarea's en geen vraagcomponent: die bewaart alleen een
        antwoord-index en geeft vrije tekst na herladen terug als ******, en zou
        het antwoord bovendien als fout markeren. De opslag zit in
        src/theme/adapt-contrib-vanilla/js/canvasOpslag.js.
        """
        rijen = ''.join(
            '<div class="canvas-rij">'
            '<label class="canvas-label" for="%s">%s</label>'
            '<textarea class="canvas-invoer js-canvas-veld" id="%s" name="%s" rows="2" '
            'placeholder="%s"></textarea>'
            '</div>' % (vid, label, vid, vid, hint) for vid, label, hint in velden)
        return self._component({
            '_component': 'text', '_classes': 'canvas-veld', '_layout': 'full',
            'title': kop, 'displayTitle': kop,
            'body': body + '<div class="canvas-groep" data-laag="%s">' % kop + rijen + '</div>',
            'instruction': ''
        }, kop)

    def commando(self, kop, body, windows=None, mac=None, beide=None, na=''):
        """Een of meer commando's om over te tikken, met een kopieerknop.

        Geef windows= en mac= als de commando's verschillen, of beide= als ze
        hetzelfde zijn. Meerdere regels mogen: geef dan een lijst van strings.
        na= is een zin die onder het blok komt, bijvoorbeeld wat je zou moeten
        zien als het gelukt is.
        """
        assert beide or (windows and mac), 'commando() zonder commando: %s' % kop

        def blok(label, regels):
            if isinstance(regels, str):
                regels = [regels]
            code = '\n'.join(regels)
            veilig = (code.replace('&', '&amp;').replace('<', '&lt;')
                          .replace('>', '&gt;').replace('"', '&quot;'))
            return ('<div class="commando__blok">'
                    '<div class="commando__balk">'
                    '<span class="commando__label">%s</span>'
                    '<button type="button" class="commando__kopieer js-commando-kopieren" '
                    'data-doel="%s" aria-label="Kopi&euml;ren: %s">'
                    'Kopi&euml;ren</button>'
                    '</div>'
                    '<pre class="commando__code"><code>%s</code></pre>'
                    '</div>' % (label, label, label, veilig))

        if beide:
            blokken = blok('Windows en macOS', beide)
        else:
            blokken = blok('Windows &middot; PowerShell', windows) + blok('macOS &middot; Terminal', mac)

        staart = '<p class="commando__na">%s</p>' % na if na else ''
        return self.tekst(kop, body + '<div class="commando">' + blokken + '</div>' + staart)

    def knoppenrij(self, kop, body):
        """Kopieer- en wisknop onder een reeks invulvelden."""
        return self.tekst(kop, body +
                          '<div class="canvas-acties">'
                          '<button type="button" class="btn-canvas js-canvas-kopieren">Kopieer als tekst</button> '
                          '<button type="button" class="btn-canvas btn-canvas--stil js-canvas-wissen">Wis mijn antwoorden</button>'
                          '<span class="canvas-melding js-canvas-melding" role="status" aria-live="polite"></span>'
                          '</div>')

    def uitslag(self, toets_id, kop='Je resultaat', drempel=75,
                voldoende='', onvoldoende=''):
        """Uitslag van een toets. Verschijnt pas als alle vragen zijn ingestuurd."""
        return self._component({
            '_component': 'assessmentResults', '_classes': '', '_layout': 'full',
            'title': kop, 'displayTitle': kop,
            'body': 'Je uitslag verschijnt hier zodra je alle vragen hebt ingestuurd.',
            'instruction': '',
            '_assessmentId': toets_id,
            '_setCompletionOn': 'inview',
            '_isVisibleBeforeCompletion': False,
            '_resetType': 'inherit',
            '_completionBody': 'Je score: <b>{{{score}}} van de {{{maxScore}}}</b> ({{{scoreAsPercent}}}%).<br>{{{feedback}}}',
            '_retry': {'button': 'Opnieuw proberen',
                       'feedback': 'Je mag het zo vaak proberen als je wilt.',
                       '_routeToAssessment': True},
            '_bands': [
                {'_score': 0, 'feedback': onvoldoende or
                 'Dat is nog niet voldoende. Loop de stof nog eens door en probeer het daarna opnieuw.',
                 '_allowRetry': True},
                {'_score': drempel, 'feedback': voldoende or
                 'Voldoende. Je hebt de stof te pakken.', '_allowRetry': True}
            ]
        }, kop)
