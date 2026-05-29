/**
 * Kie AI Image Generator for EQOLOGY site
 *
 * Usage:
 *   node generate-images.js                  # Generate all images
 *   node generate-images.js hero             # Generate a specific image by key
 *   node generate-images.js --list           # List available image keys
 */

// ── Définir KIE_API_KEY dans vos variables d'environnement ──
const API_KEY = process.env.KIE_API_KEY || "";
const API_BASE = "https://api.kie.ai/api/v1/gpt4o-image";
const fs = require("fs");
const path = require("path");
const https = require("https");

// ─── DA du site ──────────────────────────────────────────────
// Palette: navy (#0B1D2E), glacier (#4DA8B5), cream (#FAFAF8)
// Style: éditorial, organique, premium santé/wellness
// Typo: Space Grotesk (serif) + DM Sans (sans)
// ─────────────────────────────────────────────────────────────

const STYLE_PREFIX =
  "Editorial wellness photography, premium health brand aesthetic, " +
  "soft natural lighting, muted teal and cream tones, " +
  "clean minimalist composition, organic textures, " +
  "high-end magazine feel. ";

const IMAGES = {
  hero: {
    prompt: "Editorial wellness photograph. A female naturopath in a cream linen blouse at a light wood desk " +
      "in a modern bright consultation office, warmly presenting products to a female client sitting across. " +
      "Prominent on the desk: (1) a small dark amber-brown glass medicine bottle with a white screw cap, " +
      "white rectangular label on front with 'EQOLOGY' logo at top in dark gray, " +
      "then 'PURE ARCTIC OIL' in bold, 'Omega-3 from the Arctic | 300 ml' below, " +
      "small Norwegian flag at bottom left, 'It's in our nature' tagline at bottom. " +
      "(2) A teal/turquoise metallic resealable ziplock pouch standing upright next to the bottle, " +
      "with a white panel in the center reading 'EQOLOGY' logo at top, " +
      "'Omega-3 Test Kit' in teal text, description text below, Norwegian flag at bottom. " +
      "Office background: cream walls (#FAFAF8), green potted plants, soft natural window light. " +
      "No ice, no glacier, indoor only. Products are in sharp focus in the foreground. " +
      "Warm, professional, teal and cream color palette throughout.",
    size: "2:3",
    filename: "25_hero_naturopath.png",
  },
  arctic: {
    prompt: STYLE_PREFIX +
      "Pristine arctic Norwegian fjord landscape at golden hour, " +
      "crystal clear cold blue water, snow-capped mountains in background, " +
      "wild fish visible beneath the surface. " +
      "Emphasizes purity and natural origin. Cinematic, panoramic.",
    size: "3:2",
    filename: "arctic-source.png",
  },
  naturopath: {
    prompt: STYLE_PREFIX +
      "A female naturopath in a bright, modern consultation room, " +
      "warmly explaining results on a tablet to a client. " +
      "Plants in background, natural wood desk, warm ambient light. " +
      "Professional yet welcoming atmosphere. Candid editorial style.",
    size: "3:2",
    filename: "naturopath-consultation.png",
  },
  cells: {
    prompt: STYLE_PREFIX +
      "Scientific illustration of healthy cell membranes, " +
      "showing omega-3 fatty acids integrated into a flexible phospholipid bilayer. " +
      "Soft teal and blue color palette on cream background. " +
      "Clean, modern medical illustration style, educational yet beautiful.",
    size: "1:1",
    filename: "cell-membrane.png",
  },
  test: {
    prompt: STYLE_PREFIX +
      "Close-up of a simple finger-prick blood test kit for omega-3 levels, " +
      "displayed on a clean white marble surface with a small plant. " +
      "Medical yet approachable, soft lighting, shallow depth of field. " +
      "Clean and clinical but warm.",
    size: "1:1",
    filename: "omega3-test.png",
  },
  blog_brain: {
    prompt: STYLE_PREFIX +
      "Artistic representation of a human brain composed of flowing " +
      "omega-3 fish oil droplets and neural connections, " +
      "glowing softly in teal and gold tones on a dark navy background. " +
      "Abstract, scientific yet artistic. High-end editorial illustration.",
    size: "3:2",
    filename: "blog-brain-omega3.png",
  },
  blog_heart: {
    prompt: STYLE_PREFIX +
      "Anatomical heart illustration with flowing omega-3 molecules, " +
      "surrounded by healthy blood vessels, in teal and warm coral tones " +
      "on a soft cream background. Modern medical illustration, " +
      "artistic and editorial, not clinical.",
    size: "3:2",
    filename: "blog-heart-omega3.png",
  },
  ingredients: {
    prompt: STYLE_PREFIX +
      "Flat lay of premium omega-3 supplement ingredients: " +
      "wild caught fish, extra virgin olive oil in a glass bowl, " +
      "fresh olives, vitamin D capsules, on a natural linen cloth. " +
      "Overhead shot, soft diffused lighting, food photography style.",
    size: "1:1",
    filename: "ingredients-flatlay.png",
  },
  blog_fidelisation: {
    prompt: STYLE_PREFIX +
      "A naturopath showing a tablet with health progress charts to a smiling client, " +
      "in a warm modern wellness office. Soft natural light, potted plants, " +
      "wooden desk with an omega-3 test kit visible. Candid, editorial, " +
      "warm teal and cream tones. Trust and measurable results.",
    size: "1:1",
    filename: "blog-fidelisation.png",
  },
  blog_regimes: {
    prompt: STYLE_PREFIX +
      "Elegant flat lay of diverse dietary symbols: " +
      "halal and kosher certified omega-3 capsules alongside fresh herbs, " +
      "olive branch, and a small prayer bead on natural linen. " +
      "Inclusive, respectful, soft warm lighting, editorial food photography.",
    size: "1:1",
    filename: "blog-regimes.png",
  },
  avatar_sophie: {
    prompt: "Ultra photorealistic portrait photograph, shot on Canon EOS R5, 85mm f/1.4 lens. " +
      "French woman naturopath in her early 40s, warm natural smile showing slight crow's feet, " +
      "light brown hair in a soft updo with a few loose strands, minimal natural makeup, " +
      "wearing a simple cream linen blouse. Soft diffused window light from the left, " +
      "shallow depth of field, blurred green indoor plant background. " +
      "Skin texture and pores visible, natural skin imperfections. " +
      "Square crop, head and shoulders, professional LinkedIn-style portrait.",
    size: "1:1",
    filename: "avatar-sophie.png",
  },
  avatar_marie: {
    prompt: "Ultra photorealistic portrait photograph, shot on Sony A7IV, 85mm f/1.8 lens. " +
      "French woman naturopath in her mid-30s, gentle warm smile, " +
      "dark blonde wavy shoulder-length hair, light freckles, minimal makeup, " +
      "wearing a sage green cotton top. Soft overcast window light, " +
      "shallow depth of field, warm neutral bokeh background. " +
      "Visible skin texture, natural look, no retouching feel. " +
      "Square crop, head and shoulders, professional portrait.",
    size: "1:1",
    filename: "avatar-marie.png",
  },
  avatar_nadia: {
    prompt: "Ultra photorealistic portrait photograph, shot on Canon EOS R5, 85mm f/1.4 lens. " +
      "French-Moroccan woman naturopath in her late 30s, " +
      "confident warm smile, dark curly voluminous hair, olive skin tone, " +
      "wearing a crisp white linen shirt. Soft natural lighting from a large window, " +
      "shallow depth of field, minimalist bright office background with a green plant. " +
      "Visible skin texture, natural beauty, no heavy retouching. " +
      "Square crop, head and shoulders, professional portrait.",
    size: "1:1",
    filename: "avatar-nadia.png",
  },
  avatar_claire: {
    prompt: "Ultra photorealistic portrait photograph, shot on Nikon Z8, 85mm f/1.4 lens. " +
      "Elegant French woman naturopath in her mid-40s, " +
      "refined subtle smile, short auburn bob haircut, light eyes, " +
      "wearing a navy blue silk top. Soft studio-quality natural light, " +
      "shallow depth of field, clean cream-colored wall background. " +
      "Natural skin texture visible, fine lines, realistic and unretouched feel. " +
      "Square crop, head and shoulders, professional portrait.",
    size: "1:1",
    filename: "avatar-claire.png",
  },
  avatar_isabelle: {
    prompt: "Ultra photorealistic portrait photograph, shot on Canon EOS R5, 85mm f/1.4 lens. " +
      "French woman naturopath in her early 50s, " +
      "warm approachable smile, shoulder-length brown hair with natural silver streaks, " +
      "reading glasses pushed up on her head, wearing a soft teal wool cardigan. " +
      "Warm golden hour window light, shallow depth of field, bookshelf blurred behind. " +
      "Natural aging, visible laugh lines, authentic and warm. " +
      "Square crop, head and shoulders, professional portrait.",
    size: "1:1",
    filename: "avatar-isabelle.png",
  },
  avatar_veronique: {
    prompt: "Ultra photorealistic portrait photograph, shot on Sony A7RV, 85mm f/1.4 lens. " +
      "French woman naturopath in her late 40s, " +
      "serene calm smile, blonde chin-length bob haircut, blue-gray eyes, " +
      "wearing a light gray cashmere v-neck sweater. Soft diffused natural light, " +
      "shallow depth of field, neutral warm-toned interior background. " +
      "Natural skin with visible pores and fine lines, authentic feel. " +
      "Square crop, head and shoulders, professional portrait.",
    size: "1:1",
    filename: "avatar-veronique.png",
  },
  avatar_laure: {
    prompt: "Ultra photorealistic portrait photograph, shot on Canon EOS R5, 85mm f/1.4 lens. " +
      "French woman naturopath in her mid-30s, " +
      "bright genuine toothy smile, long chestnut brown hair falling over shoulders, " +
      "light natural makeup, wearing an off-white chunky knit top. " +
      "Soft morning window light, shallow depth of field, botanical green background. " +
      "Natural skin texture, youthful but real, no airbrushing feel. " +
      "Square crop, head and shoulders, professional portrait.",
    size: "1:1",
    filename: "avatar-laure.png",
  },
  avatar_amelie: {
    prompt: "Ultra photorealistic portrait photograph, shot on Nikon Z8, 85mm f/1.4 lens. " +
      "French woman naturopath in her early 30s, " +
      "youthful radiant smile, light brown short pixie cut hair, hazel eyes, " +
      "wearing a dusty rose silk blouse. Soft natural light from a large window, " +
      "shallow depth of field, modern minimalist white office background. " +
      "Natural skin texture visible, fresh and authentic look. " +
      "Square crop, head and shoulders, professional portrait.",
    size: "1:1",
    filename: "avatar-amelie.png",
  },
  blog_immunite: {
    prompt: STYLE_PREFIX +
      "Scientific editorial illustration of a human eye cross-section " +
      "with DHA molecules and immune cells, glowing in soft teal and gold " +
      "on a dark navy background. Modern medical illustration, " +
      "artistic and luminous, showing the connection between vision and immunity.",
    size: "1:1",
    filename: "blog-immunite.png",
  },
  blog_revenus: {
    prompt: STYLE_PREFIX +
      "A confident naturopath in a bright modern office, standing beside " +
      "a growing revenue chart on a whiteboard, with premium supplement products " +
      "displayed on shelves behind. Warm natural light, professional yet approachable, " +
      "editorial business portrait style, teal accents.",
    size: "1:1",
    filename: "blog-revenus.png",
  },
  gamme_vegan: {
    prompt: STYLE_PREFIX +
      "A premium glass bottle of vegan omega-3 supplement made from microalgae, " +
      "with vibrant green and teal liquid, placed on a bed of fresh green spirulina " +
      "and microalgae on a natural stone surface. Soft arctic-inspired background, " +
      "clean minimalist composition, plant-based and pure. Product photography, " +
      "depth of field, elegant and natural.",
    size: "3:2",
    filename: "19_gamme_vegan.png",
  },
  gamme_diagnostic: {
    prompt: STYLE_PREFIX +
      "Close-up of a premium omega-3 blood test diagnostic kit displayed on a clean " +
      "white marble surface with a small succulent plant. The kit includes a simple " +
      "finger-prick device, a sample card, and a results booklet with charts. " +
      "Medical yet approachable, soft warm lighting, shallow depth of field. " +
      "Clean, clinical but warm. Product photography.",
    size: "3:2",
    filename: "20_gamme_diagnostic.png",
  },
  gamme_complements: {
    prompt: STYLE_PREFIX +
      "Elegant flat lay of premium supplement synergy ingredients: " +
      "vitamin D capsules, CoQ10 softgels, lutein drops, and a small glass bottle " +
      "of fish oil, arranged on a natural linen cloth with olive branches. " +
      "Warm golden light, overhead shot, food and supplement photography, " +
      "clean and premium, teal and cream accents.",
    size: "3:2",
    filename: "21_gamme_complements.png",
  },
  about_banner: {
    prompt: STYLE_PREFIX +
      "Wide panoramic shot of a modern Scandinavian wellness event space, " +
      "with naturopaths and health professionals networking around a long " +
      "natural wood table. Premium omega-3 products displayed elegantly. " +
      "Soft teal and cream tones, large windows with fjord-like landscape visible, " +
      "warm golden hour light. Editorial event photography, cinematic wide angle.",
    size: "3:2",
    filename: "22_about_banner.png",
  },
  about_lab: {
    prompt: STYLE_PREFIX +
      "Modern Norwegian laboratory interior with clean white surfaces, " +
      "glass bottles of golden fish oil being quality-tested. A scientist in a white coat " +
      "examining a vial against natural light from large windows overlooking snowy mountains. " +
      "Pristine, scientific yet warm. Teal and white tones, editorial documentary photography.",
    size: "3:2",
    filename: "23_about_lab.png",
  },
  about_consultation: {
    prompt: STYLE_PREFIX +
      "A warm consultation scene: a female naturopath sitting across from a client " +
      "in a bright modern wellness office, showing omega-3 test results on a tablet. " +
      "Natural wood desk, green plants, soft diffused window light. " +
      "Bottles of premium omega-3 oil on a shelf in the background. " +
      "Candid, authentic, editorial wellness photography.",
    size: "3:2",
    filename: "24_about_consultation.png",
  },
  sante_coeur: {
    prompt: STYLE_PREFIX +
      "A fit woman in her 40s jogging at sunrise along a calm coastal path, " +
      "hand on her chest feeling her heartbeat, radiating health and vitality. " +
      "Soft golden morning light, teal ocean in the background, " +
      "editorial lifestyle photography, warm and authentic. Shallow depth of field.",
    size: "1:1",
    filename: "sante-coeur.png",
  },
  sante_cerveau: {
    prompt: STYLE_PREFIX +
      "A woman in her 30s reading a book in a bright modern living room, " +
      "looking focused and sharp, with a cup of golden omega-3 oil on the table beside her. " +
      "Soft natural window light, cream and teal tones, cozy yet minimal. " +
      "Editorial lifestyle photography, authentic and warm, celebrating mental clarity.",
    size: "1:1",
    filename: "sante-cerveau.png",
  },
  sante_immunite: {
    prompt: STYLE_PREFIX +
      "A female naturopath in a white linen shirt, smiling warmly at a client " +
      "while presenting a small omega-3 supplement bottle in a bright consultation room. " +
      "Green plants, natural wood furniture, soft diffused window light. " +
      "Editorial wellness photography, professional yet approachable, " +
      "teal and cream accents, candid authentic moment.",
    size: "1:1",
    filename: "sante-immunite.png",
  },
  avantage_produit: {
    prompt: STYLE_PREFIX +
      "Close-up of a naturopath's hands holding a premium dark glass bottle of omega-3 " +
      "fish oil, presenting it to a client across a natural wood desk. " +
      "The bottle label is elegant and minimal. Soft warm window light, " +
      "shallow depth of field, trust and quality, editorial product-in-context photography.",
    size: "3:2",
    filename: "26_avantage_produit.png",
  },
  avantage_revenu: {
    prompt: STYLE_PREFIX +
      "A smiling female naturopath in her office reviewing a growth chart on a laptop screen, " +
      "with supplement products neatly arranged on shelves behind her. " +
      "Warm natural light, modern wellness office, teal and cream tones. " +
      "Editorial business portrait, success and growth, professional and approachable.",
    size: "3:2",
    filename: "27_avantage_revenu.png",
  },
  avantage_test: {
    prompt: STYLE_PREFIX +
      "A naturopath showing omega-3 blood test results on a tablet to an impressed client, " +
      "both looking at the screen with positive expressions. A small test kit box on the desk. " +
      "Bright modern consultation room, plants, natural wood. " +
      "Editorial candid photography, trust and science, warm teal accents.",
    size: "3:2",
    filename: "28_avantage_test.png",
  },
};

// ─── HTTP helpers ────────────────────────────────────────────

function post(url, body) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(body);
    const req = https.request(url, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${API_KEY}`,
        "Content-Type": "application/json",
        "Content-Length": Buffer.byteLength(data),
      },
    }, (res) => {
      let chunks = "";
      res.on("data", (d) => chunks += d);
      res.on("end", () => {
        try { resolve(JSON.parse(chunks)); }
        catch { resolve(chunks); }
      });
    });
    req.on("error", reject);
    req.write(data);
    req.end();
  });
}

function get(url) {
  return new Promise((resolve, reject) => {
    https.get(url, {
      headers: { "Authorization": `Bearer ${API_KEY}` },
    }, (res) => {
      let chunks = "";
      res.on("data", (d) => chunks += d);
      res.on("end", () => {
        try { resolve(JSON.parse(chunks)); }
        catch { resolve(chunks); }
      });
    }).on("error", reject);
  });
}

function download(url, dest) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(dest);
    https.get(url, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        file.close();
        fs.unlinkSync(dest);
        return download(res.headers.location, dest).then(resolve).catch(reject);
      }
      res.pipe(file);
      file.on("finish", () => { file.close(); resolve(); });
    }).on("error", (e) => { fs.unlinkSync(dest); reject(e); });
  });
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

// ─── Main logic ──────────────────────────────────────────────

async function generateImage(key) {
  const img = IMAGES[key];
  if (!img) {
    console.error(`Unknown image key: "${key}". Use --list to see options.`);
    return;
  }

  const outDir = path.join(__dirname, "assets", "images", "generated");
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
  const outPath = path.join(outDir, img.filename);

  console.log(`\n[${key}] Submitting generation task...`);
  console.log(`  Prompt: ${img.prompt.slice(0, 80)}...`);
  console.log(`  Size: ${img.size}`);

  const createRes = await post(`${API_BASE}/generate`, {
    prompt: img.prompt,
    size: img.size,
  });

  if (createRes.code !== 200) {
    console.error(`  ERROR creating task:`, createRes);
    return;
  }

  const taskId = createRes.data.taskId;
  console.log(`  Task created: ${taskId}`);

  // Poll for completion
  let attempts = 0;
  const maxAttempts = 120; // 4 minutes max
  while (attempts < maxAttempts) {
    await sleep(2000);
    attempts++;

    const status = await get(`${API_BASE}/record-info?taskId=${taskId}`);

    if (status.code !== 200) {
      console.log(`  Polling error:`, status);
      continue;
    }

    const s = status.data?.status;
    const progress = status.data?.progress || "?";

    if (s === "SUCCESS") {
      const urls = status.data.response?.resultUrls;
      if (urls && urls.length > 0) {
        console.log(`  Done! Downloading...`);
        await download(urls[0], outPath);
        console.log(`  Saved: ${outPath}`);
      } else {
        console.error(`  SUCCESS but no result URLs:`, status.data);
      }
      return;
    }

    if (s === "CREATE_TASK_FAILED" || s === "GENERATE_FAILED") {
      console.error(`  FAILED: ${status.data?.errorMessage || s}`);
      return;
    }

    if (attempts % 5 === 0) {
      console.log(`  Waiting... (status: ${s}, progress: ${progress})`);
    }
  }

  console.error(`  Timeout after ${maxAttempts * 2}s.`);
}

async function main() {
  const args = process.argv.slice(2);

  if (args.includes("--list")) {
    console.log("\nAvailable image keys:\n");
    for (const [key, img] of Object.entries(IMAGES)) {
      console.log(`  ${key.padEnd(15)} -> assets/images/${img.filename} (${img.size})`);
    }
    return;
  }

  const keys = args.length > 0
    ? args.filter(a => !a.startsWith("--"))
    : Object.keys(IMAGES);

  console.log(`Generating ${keys.length} image(s) for EQOLOGY site...\n`);

  for (const key of keys) {
    await generateImage(key);
  }

  console.log("\nDone!");
}

main().catch(console.error);
