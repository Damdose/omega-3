// POST /api/contact — envoie le détail du formulaire de contact par e-mail via Resend.
// Aucune dépendance npm : appel direct à l'API REST Resend avec fetch (Node 18+).
module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'Method not allowed' });
    return;
  }

  try {
    let body = req.body;
    if (typeof body === 'string') {
      try { body = JSON.parse(body); } catch (e) { body = {}; }
    }
    body = body || {};

    const clean = (v, max) => String(v == null ? '' : v).slice(0, max);
    const data = {
      prenom: clean(body.prenom, 120),
      nom: clean(body.nom, 120),
      email: clean(body.email, 200),
      sujet: clean(body.sujet, 160),
      message: clean(body.message, 5000),
      date: new Date().toISOString()
    };

    if (!data.email && !data.message) {
      res.status(400).json({ error: 'Message vide' });
      return;
    }

    const key = process.env.RESEND_API_KEY;
    if (!key) {
      res.status(500).json({ error: 'E-mail non configuré (RESEND_API_KEY manquant)' });
      return;
    }

    const from = process.env.LEAD_EMAIL_FROM || 'FENA x Eqology <zenco@heyfuture.fr>';
    const to = (process.env.LEAD_EMAIL_TO || 'zenco.coignard@gmail.com')
      .split(',').map(s => s.trim()).filter(Boolean);

    const esc = (s) => String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    const dateFr = new Date(data.date).toLocaleString('fr-FR', { timeZone: 'Europe/Paris' });

    const rows = [
      ['Prénom', data.prenom],
      ['Nom', data.nom],
      ['Email', data.email],
      ['Sujet', data.sujet],
      ['Date', dateFr]
    ].filter(([, v]) => v);

    const trs = rows.map(([k, v]) =>
      `<tr><td style="padding:8px 14px;border-bottom:1px solid #eceae4;color:#6b7280;font-size:13px;white-space:nowrap">${esc(k)}</td>` +
      `<td style="padding:8px 14px;border-bottom:1px solid #eceae4;color:#0B1D2E;font-size:14px;font-weight:500">${esc(v)}</td></tr>`
    ).join('');

    const html =
      `<div style="font-family:Arial,Helvetica,sans-serif;max-width:560px;margin:auto">
        <h2 style="color:#0B1D2E;font-size:18px">Nouveau message de contact — FENA × Eqology</h2>
        <table style="border-collapse:collapse;width:100%;border:1px solid #eceae4;border-radius:8px;overflow:hidden">${trs}</table>
        <p style="color:#6b7280;font-size:13px;margin:18px 0 6px">Message :</p>
        <div style="white-space:pre-wrap;background:#f5f4f0;border-radius:8px;padding:14px;color:#0B1D2E;font-size:14px;line-height:1.5">${esc(data.message)}</div>
      </div>`;

    const text = rows.map(([k, v]) => `${k}: ${v}`).join('\n') + '\n\nMessage:\n' + data.message;

    const payload = {
      from,
      to,
      subject: `Contact — ${data.sujet || (data.prenom + ' ' + data.nom).trim() || data.email}`,
      html,
      text
    };
    if (data.email) payload.reply_to = data.email;

    const resp = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { authorization: 'Bearer ' + key, 'content-type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!resp.ok) {
      const detail = await resp.text();
      res.status(502).json({ error: 'Erreur envoi e-mail', detail: detail.slice(0, 300) });
      return;
    }

    res.status(200).json({ ok: true });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
};
