// Bandeau d'accord pour la mesure d'audience (pixel Meta), autonome : styles en ligne, aucune dépendance.
(function () {
  var etat = null; try { etat = localStorage.getItem('cookies_accepted'); } catch (e) {}
  if (etat) return;
  function ajoute() {
    var b = document.createElement('div');
    b.setAttribute('role', 'dialog'); b.setAttribute('aria-label', "Mesure d'audience");
    b.style.cssText = 'position:fixed;left:12px;right:12px;bottom:12px;z-index:60;max-width:440px;background:#0A1622;color:#fff;border:1px solid rgba(255,255,255,.15);border-radius:10px;padding:16px 18px;box-shadow:0 20px 50px rgba(0,0,0,.35);font:14px/1.5 inherit';
    b.innerHTML = "<p style=\"margin:0;color:#d5dde6\">Avec votre accord, nous mesurons les visites venues de nos publicités (pixel Meta). Rien n'est déposé si vous refusez. <a href=\"confidentialite.html\" style=\"color:#fff;text-decoration:underline\">En savoir plus</a></p>"
      + '<div style="margin-top:12px;display:flex;gap:8px"><button id="ck-ok" style="height:36px;padding:0 16px;border-radius:6px;background:#fff;color:#0A1622;font-weight:500;border:0;cursor:pointer">Accepter</button><button id="ck-non" style="height:36px;padding:0 16px;border-radius:6px;background:transparent;color:#fff;border:1px solid rgba(255,255,255,.4);cursor:pointer">Refuser</button></div>';
    document.body.appendChild(b);
    document.getElementById('ck-ok').onclick = function () { try { localStorage.setItem('cookies_accepted', 'true'); } catch (e) {} b.remove(); if (window.chargerPixel) window.chargerPixel(); };
    document.getElementById('ck-non').onclick = function () { try { localStorage.setItem('cookies_accepted', 'refused'); } catch (e) {} b.remove(); };
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ajoute); else ajoute();
})();
