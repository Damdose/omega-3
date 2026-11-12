// GET /api/leads — renvoie tous les leads (protégé par ADMIN_PASSWORD).
// Liste les blobs sous leads/ (avec le token, côté serveur) puis lit chaque fichier JSON.
// Le mot de passe est transmis via l'en-tête `x-admin-key` ou `?key=`.
module.exports = async (req, res) => {
  const expected = process.env.ADMIN_PASSWORD;
  if (!expected) {
    res.status(500).json({ error: 'ADMIN_PASSWORD non configuré sur Vercel' });
    return;
  }

  const provided = req.headers['x-admin-key'] || (req.query && req.query.key) || '';
  if (provided !== expected) {
    res.status(401).json({ error: 'Mot de passe incorrect' });
    return;
  }

  const token = process.env.BLOB_READ_WRITE_TOKEN;
  if (!token) {
    res.status(500).json({ error: 'Stockage non configuré (Blob manquant)' });
    return;
  }

  try {
    // 1) Lister toutes les URLs de leads (avec pagination).
    const urls = [];
    let cursor = null;
    do {
      const u = new URL('https://blob.vercel-storage.com');
      u.searchParams.set('prefix', 'leads/');
      u.searchParams.set('limit', '1000');
      if (cursor) u.searchParams.set('cursor', cursor);
      const r = await fetch(u, {
        headers: { authorization: 'Bearer ' + token, 'x-api-version': '7' }
      });
      const data = await r.json();
      (data.blobs || []).forEach((b) => urls.push(b.url));
      cursor = data.hasMore ? data.cursor : null;
    } while (cursor);

    // 2) Lire le contenu de chaque lead.
    const leads = (await Promise.all(urls.map(async (url) => {
      try {
        const r = await fetch(url, { cache: 'no-store' });
        if (!r.ok) return null;
        return await r.json();
      } catch (e) { return null; }
    }))).filter(Boolean);

    // 3) Plus récents en premier.
    leads.sort((a, b) => String(b.date || '').localeCompare(String(a.date || '')));

    res.setHeader('Cache-Control', 'no-store');
    res.status(200).json({ count: leads.length, leads });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
};
