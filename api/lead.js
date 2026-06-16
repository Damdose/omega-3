// POST /api/lead — enregistre un lead du formulaire de candidature dans Vercel Blob.
// Aucune dépendance npm : appel direct à l'API REST Blob avec fetch (Node 18+).
// Chaque lead = un petit fichier JSON sous le préfixe leads/ (suffixe aléatoire = URL non devinable).
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

    res.status(200).json({ ok: true, id });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
};
