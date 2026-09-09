import Adapt from 'core/js/adapt';

/**
 * Kopieerknop bij een commandoblok.
 *
 * De knop staat in de HTML van een text-component (zie bouwstenen.py,
 * methode commando). Adapt rendert die componenten pas na het laden en
 * hergebruikt de DOM tussen pagina's, dus we luisteren gedelegeerd op body
 * in plaats van per knop een handler te binden.
 *
 * navigator.clipboard werkt alleen op https en op localhost. Op een gewoon
 * http-adres valt hij terug op de oude execCommand-route, want anders zou de
 * knop op een testserver stil niets doen.
 */

const MELDING_MS = 2000;

function tekstVanBlok(knop) {
  const blok = knop.closest('.commando__blok');
  const code = blok && blok.querySelector('code');
  return code ? code.textContent : '';
}

function terugmelden(knop, gelukt) {
  const origineel = knop.dataset.origineel || knop.textContent;
  knop.dataset.origineel = origineel;
  knop.textContent = gelukt ? 'Gekopieerd' : 'Kopiëren mislukt';
  knop.classList.toggle('is-gekopieerd', gelukt);
  window.setTimeout(() => {
    knop.textContent = origineel;
    knop.classList.remove('is-gekopieerd');
  }, MELDING_MS);
}

function ouderwetsKopieren(tekst) {
  const veld = document.createElement('textarea');
  veld.value = tekst;
  veld.setAttribute('readonly', '');
  veld.style.position = 'fixed';
  veld.style.top = '-1000px';
  document.body.appendChild(veld);
  veld.select();
  let gelukt = false;
  try {
    gelukt = document.execCommand('copy');
  } catch (e) {
    gelukt = false;
  }
  document.body.removeChild(veld);
  return gelukt;
}

function opKlik(event) {
  const knop = event.target.closest('.js-commando-kopieren');
  if (!knop) return;
  const tekst = tekstVanBlok(knop);
  if (!tekst) return;

  // Eerst de oude route, en wel synchroon in deze klik. Beide manieren van
  // kopiëren eisen een verse gebruikersactie, en die is verlopen zodra we een
  // promise hebben afgewacht — een terugval ná .catch() mislukt dus altijd.
  if (ouderwetsKopieren(tekst)) {
    terugmelden(knop, true);
    return;
  }

  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(tekst)
      .then(() => terugmelden(knop, true))
      .catch(() => terugmelden(knop, false));
    return;
  }
  terugmelden(knop, false);
}

class KopieerKnop extends Backbone.Controller {

  initialize() {
    this.listenTo(Adapt, 'app:dataReady', this.onDataReady);
  }

  onDataReady() {
    document.body.addEventListener('click', opKlik);
  }

}

export default new KopieerKnop();
