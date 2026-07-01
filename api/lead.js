// POST /api/lead — enregistre un lead du formulaire de candidature dans Vercel Blob
// PUIS envoie le détail complet par e-mail via Resend.
// Aucune dépendance npm : appels directs aux API REST (Blob + Resend) avec fetch (Node 18+).
module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }

  const token = process.env.BLOB_READ_WRITE_TOKEN;
  if (!token) {
    res.status(500).json({ error: 'Stockage non configuré (Blob manquant)' });
    return;
  }

  try {
    let body = req.body;
    if (typeof body === 'string') {
      try { body = JSON.parse(body); } catch (e) { body = {}; }
    }
    body = body || {};

    const clean = (v, max) => String(v == null ? '' : v).slice(0, max);
    const id = Date.now().toString(36) + Math.random().toString(36).slice(2, 8);

    const record = {
      id,
      date: new Date().toISOString(),
      name: clean(body.name, 200),
      email: clean(body.email, 200),
      phone: clean(body.phone, 60),
      city: clean(body.city, 120),
      anciennete: clean(body.step1, 40),
      consultants: clean(body.step2, 40),
      defi: clean(body.step3, 60),
      complements: clean(body.step4, 60)
    };

    if (!record.name && !record.email && !record.phone) {
      res.status(400).json({ error: 'Lead vide' });
      return;
    }

    const put = await fetch('https://blob.vercel-storage.com/leads/' + id + '.json', {
      method: 'PUT',
      headers: {
        authorization: 'Bearer ' + token,
        'x-api-version': '7',
        'x-content-type': 'application/json',
        'x-add-random-suffix': '1'
      },
      body: JSON.stringify(record)
    });

    if (!put.ok) {
      const detail = await put.text();
      res.status(502).json({ error: 'Erreur de stockage', detail });
      return;
    }

    // Envoi e-mail (best-effort : n'échoue pas la requête si l'e-mail plante)
    let emailStatus = 'skipped';
    try {
      emailStatus = await sendLeadEmail(record);
    } catch (e) {
      emailStatus = 'error: ' + e.message;
    }

    res.status(200).json({ ok: true, id, email: emailStatus });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
};

// Envoie le détail complet de la candidature par e-mail via Resend.
async function sendLeadEmail(r) {
  const key = process.env.RESEND_API_KEY;
  if (!key) return 'skipped (no RESEND_API_KEY)';

  const from = process.env.LEAD_EMAIL_FROM || 'FENA x Eqology <zenco@a-future.fr>';
  const to = (process.env.LEAD_EMAIL_TO || 'zenco@a-future.fr')
    .split(',').map(s => s.trim()).filter(Boolean);

  const esc = (s) => String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

  const dateFr = new Date(r.date).toLocaleString('fr-FR', { timeZone: 'Europe/Paris' });

  const rows = [
    ['Nom', r.name],
    ['Email', r.email],
    ['Téléphone', r.phone],
    ['Ville', r.city],
    ['Ancienneté', r.anciennete],
    ['Consultants / mois', r.consultants],
    ['Défi principal', r.defi],
    ['Compléments', r.complements],
    ['Date', dateFr],
    ['Réf.', r.id]
  ].filter(([, v]) => v);

  const trs = rows.map(([k, v]) =>
    `<tr><td style="padding:8px 14px;border-bottom:1px solid #eceae4;color:#6b7280;font-size:13px;white-space:nowrap">${esc(k)}</td>` +
    `<td style="padding:8px 14px;border-bottom:1px solid #eceae4;color:#0B1D2E;font-size:14px;font-weight:500">${esc(v)}</td></tr>`
  ).join('');

  const html =
    `<div style="font-family:Arial,Helvetica,sans-serif;max-width:560px;margin:auto">
      <h2 style="color:#0B1D2E;font-size:18px">Nouvelle candidature — FENA × Eqology</h2>
      <p style="color:#6b7280;font-size:14px">Un naturopathe a rempli le formulaire de rendez-vous sur le site.</p>
      <table style="border-collapse:collapse;width:100%;border:1px solid #eceae4;border-radius:8px;overflow:hidden">${trs}</table>
    </div>`;

  const text = rows.map(([k, v]) => `${k}: ${v}`).join('\n');

  const payload = {
    from,
    to,
    subject: `Nouvelle candidature — ${r.name || r.email || 'sans nom'}`,
    html,
    text
  };
  if (r.email) payload.reply_to = r.email;

  const resp = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { authorization: 'Bearer ' + key, 'content-type': 'application/json' },
    body: JSON.stringify(payload)
  });

  if (!resp.ok) {
    const detail = await resp.text();
    return 'error: ' + resp.status + ' ' + detail.slice(0, 300);
  }
  return 'sent';
}
