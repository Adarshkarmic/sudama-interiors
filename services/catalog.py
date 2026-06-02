from django.templatetags.static import static

import os

def image(path):
    return static(f"images/services/{path}")

def gallery_images(folder):
    from django.conf import settings
    # Try static first (source folder), fallback to staticfiles (collected static folder)
    folder_path = settings.BASE_DIR / "static" / "images" / "services" / folder
    if not folder_path.exists():
        folder_path = settings.BASE_DIR / "staticfiles" / "images" / "services" / folder

    if not folder_path.exists():
        return []

    import os
    files = sorted(os.listdir(folder_path))

    return [
        static(f"images/services/{folder}/{file}")
        for file in files
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    ]

SERVICE_CATALOG = {
    "doors-windows-casement-louver-systems": {
        "eyebrow": "Doors, Windows, Casement and Louvers",
        "local_intro": "Premium uPVC windows in Darbhanga, aluminium casements, steel frames, WPC doors, and plywood shutter systems for homes and commercial interiors across Bihar.",
        "overview": {
            "what": "A complete opening-system service for doors, windows, casement shutters, partitions, and louvered ventilation features.",
            "where": "Used in bedrooms, balconies, kitchens, storefronts, living rooms, utility zones, wardrobes, and semi-outdoor openings.",
            "why": "Clients choose this service when they want better durability, cleaner edges, weather resistance, privacy, ventilation, and a finish that fits the larger interior language.",
        },
        "materials": [
            {
                "name": "uPVC",
                "what": "A weather-resistant polymer frame system used mostly for windows and balcony openings.",
                "used": "Bedrooms, balconies, kitchens, sound-sensitive rooms, and exterior-facing windows.",
                "benefits": "Low maintenance, clean appearance, good sealing, thermal comfort, and noise reduction.",
                "durability": "High in normal residential use; resistant to termites and moisture.",
                "maintenance": "Very low. Occasional cleaning keeps the finish fresh.",
                "visual": "Modern, neat, and minimal with a refined European feel.",
                "pricing": "Premium practical",
            },
            {
                "name": "Aluminium",
                "what": "Slim metal framing for doors, windows, sliding systems, and modern casements.",
                "used": "Large openings, balconies, shops, office partitions, and contemporary homes.",
                "benefits": "Slim sightlines, strong profiles, broad color options, and elegant modern detailing.",
                "durability": "Excellent when powder-coated or anodized properly.",
                "maintenance": "Low; periodic track cleaning and hardware checks are enough.",
                "visual": "Sleek, architectural, and premium.",
                "pricing": "Premium",
            },
            {
                "name": "Steel",
                "what": "A strong metal option for security-focused frames, railings, and durable access points.",
                "used": "Main gates, utility doors, service areas, balconies, and commercial openings.",
                "benefits": "Strength, security, long life, and strong structural confidence.",
                "durability": "Very high with proper anti-rust treatment and paint.",
                "maintenance": "Moderate; repainting may be needed over time.",
                "visual": "Bold, strong, and industrial-modern.",
                "pricing": "Budget to premium",
            },
            {
                "name": "WPC",
                "what": "Wood polymer composite used for moisture-safe doors and interior panels.",
                "used": "Bathrooms, kitchens, utility spaces, wardrobes, and damp-prone interiors.",
                "benefits": "Termite resistance, moisture resistance, stable finish, and easy shaping.",
                "durability": "High for interior and semi-wet applications.",
                "maintenance": "Low; no polishing required.",
                "visual": "Clean wood-like warmth with modern practicality.",
                "pricing": "Mid-premium",
            },
            {
                "name": "Plywood",
                "what": "Engineered wood sheet material used for custom doors, shutters, and built-in interiors.",
                "used": "Room doors, wardrobes, storage shutters, panelled doors, and furniture-integrated openings.",
                "benefits": "Design flexibility, broad laminate compatibility, and cost control.",
                "durability": "Good when the grade matches the use case and edges are sealed well.",
                "maintenance": "Moderate; depends on laminate, polish, and exposure.",
                "visual": "Warm, customizable, and interior-friendly.",
                "pricing": "Budget to premium",
            },
        ],
        "gallery": gallery_images("doors-windows"),
        "faqs": [
            ("Which is better for windows in Darbhanga, uPVC or aluminium?", "uPVC is excellent for low-maintenance residential comfort, while aluminium feels slimmer and more premium for larger openings and modern facades."),
            ("Can WPC doors be used in bathrooms?", "Yes. WPC is a strong option for bathroom and utility doors because it handles moisture better than many traditional wood-based shutters."),
            ("Do you provide installation in Bihar?", "Yes. Sudama Interiors handles material guidance and execution for interior and opening systems across Darbhanga and nearby Bihar locations."),
        ],
    },
    "acp-cladding": {
        "eyebrow": "ACP Cladding in Darbhanga",
        "local_intro": "Modern ACP cladding for residential facades, shop fronts, signage bands, and premium exterior identity in Darbhanga and Bihar.",
        "overview": {
            "what": "ACP cladding uses aluminium composite panels to create a clean, modern, durable exterior surface.",
            "where": "Applied on home elevations, shop fronts, commercial facades, signage areas, porch zones, and feature surfaces.",
            "why": "Clients choose ACP for a sharper exterior look, faster installation, weather protection, and strong visual branding.",
        },
        "materials": [
            {"name": "Residential ACP Cladding", "what": "A modern facade treatment for homes.", "used": "Balconies, porch faces, elevation bands, and exterior highlights.", "benefits": "Clean facade lines, weather resistance, and a premium first impression.", "durability": "High with correct grade and installation.", "maintenance": "Low; periodic washing is usually enough.", "visual": "Modern, polished, and architectural.", "pricing": "Mid-premium"},
            {"name": "Shop ACP Cladding", "what": "A commercial frontage system for visual identity.", "used": "Retail shops, signboards, counters, entrance bands, and exterior facades.", "benefits": "Strong branding, quick transformation, durable finish, and high street visibility.", "durability": "High for commercial frontage when fixed correctly.", "maintenance": "Low to moderate depending on road dust exposure.", "visual": "Sharp, modern, and business-ready.", "pricing": "Premium practical"},
        ],
        "gallery": gallery_images("acp-cladding"),
        "faqs": [
            ("Is ACP cladding suitable for shop fronts in Darbhanga?", "Yes. ACP is widely used for modern shop facades because it gives a clean commercial finish and supports strong brand visibility."),
            ("Does ACP require heavy maintenance?", "No. Good ACP cladding is easy to clean and maintains its exterior appearance with periodic washing."),
            ("Can ACP be used for residential elevations?", "Yes. Residential ACP cladding can create elegant bands, balcony highlights, and modern exterior details."),
        ],
    },
    "false-ceiling": {
        "eyebrow": "False Ceiling Services in Bihar",
        "local_intro": "Premium PVC, WPC, POP, and gypsum false ceiling services in Bihar for layered lighting, cleaner room depth, and elegant interior atmosphere.",
        "overview": {
            "what": "False ceiling design creates a secondary ceiling plane for lighting, service concealment, acoustics, and visual depth.",
            "where": "Living rooms, bedrooms, kitchens, shops, offices, halls, and premium residential interiors.",
            "why": "Clients choose it to create soft lighting, hide wiring, control proportions, and make interiors feel complete.",
        },
        "materials": [
            {"name": "PVC Ceiling", "what": "A lightweight ceiling panel system.", "used": "Kitchens, bathrooms, utility spaces, and budget-sensitive rooms.", "benefits": "Moisture resistance, quick installation, and easy cleaning.", "durability": "Good in wet and utility zones.", "maintenance": "Very low.", "visual": "Clean and practical.", "pricing": "Budget practical", "images": [image("false-ceiling/false-ceiling_pvc_1.jpeg"), image("false-ceiling/false-ceiling_pvc_2.jpeg")]},
            {"name": "WPC Ceiling", "what": "A wood-composite ceiling finish.", "used": "Balconies, feature ceilings, warm interior zones, and semi-moist areas.", "benefits": "Wood-like warmth, better moisture handling, and termite resistance.", "durability": "High for interior use.", "maintenance": "Low.", "visual": "Warm, premium, and textured.", "pricing": "Mid-premium", "images": [image("false-ceiling/false-ceiling_wooden_3.jpeg"), image("false-ceiling/photo_2026-05-12_23-50-05.jpg")]},
            {"name": "POP Ceiling", "what": "A molded plaster ceiling system.", "used": "Decorative rooms, classical profiles, coves, and custom ceiling curves.", "benefits": "Flexible shaping, elegant detailing, and smooth finish.", "durability": "Good in dry spaces.", "maintenance": "Moderate.", "visual": "Decorative and refined.", "pricing": "Mid-range", "images": [image("false-ceiling/false-ceiling_pop_1.jpeg"), image("false-ceiling/photo_2026-05-12_23-40-28.jpg")]},
            {"name": "Gypsum Ceiling", "what": "A precise board-based ceiling system.", "used": "Modern homes, offices, living rooms, bedrooms, and lighting-led interiors.", "benefits": "Clean lines, fast execution, crisp edges, and premium lighting integration.", "durability": "High in dry interiors.", "maintenance": "Low to moderate.", "visual": "Minimal, elegant, and premium.", "pricing": "Premium practical", "images": [image("false-ceiling/photo_2026-05-12_23-40-37.jpg"), image("false-ceiling/photo_2026-05-12_23-40-39.jpg")]},
        ],
        "gallery": gallery_images("false-ceiling"),
        "faqs": [
            ("Which false ceiling is best for a living room?", "Gypsum is often preferred for modern living rooms because it gives clean edges and supports layered lighting beautifully."),
            ("Is PVC ceiling good for kitchens?", "Yes. PVC works well in kitchens and utility zones because it is lightweight, moisture-resistant, and easy to clean."),
            ("Do you provide false ceiling services in Bihar?", "Yes. Sudama Interiors provides false ceiling planning and execution for homes and commercial spaces in Darbhanga and Bihar."),
        ],
    },
    "steel-ss-railing": {
        "eyebrow": "Steel and SS Railing",
        "local_intro": "Modern steel and stainless steel railing for staircases, balconies, terraces, and premium interior-edge detailing in Bihar.",
        "overview": {
            "what": "Railing systems combine safety, edge definition, and architectural styling for stairs and balconies.",
            "where": "Staircases, balconies, terraces, duplex homes, shops, showrooms, and entrance zones.",
            "why": "Clients choose steel and SS railing for strength, long life, modern finishing, and low visual clutter.",
        },
        "materials": [
            {"name": "Staircase Railing", "what": "A safety and design system for stair edges.", "used": "Duplex homes, commercial stairs, and interior staircases.", "benefits": "Safety, polish, and strong line definition.", "durability": "Very high.", "maintenance": "Low with proper finish.", "visual": "Modern and structured.", "pricing": "Mid to premium"},
            {"name": "Balcony Railing", "what": "Exterior railing for balcony and terrace edges.", "used": "Homes, apartments, terraces, and commercial fronts.", "benefits": "Safety, weather resistance, and clean elevation impact.", "durability": "High with correct grade.", "maintenance": "Low to moderate.", "visual": "Open, refined, and contemporary.", "pricing": "Premium practical"},
            {"name": "Modern SS Finishes", "what": "Stainless steel railing with polished or matte treatment.", "used": "Premium homes, staircases, and balcony edges.", "benefits": "Corrosion resistance, elegant shine, and long-term value.", "durability": "Excellent.", "maintenance": "Low.", "visual": "Premium, clean, and bright.", "pricing": "Premium"},
        ],
        "gallery": gallery_images("steel-ss-railing"),
        "faqs": [
            ("Is SS railing better than painted steel railing?", "SS railing generally offers a more premium finish and better corrosion resistance, while painted steel can be more budget-flexible."),
            ("Can railing design look modern without feeling heavy?", "Yes. Slim profiles, matte finishes, and balanced spacing can make railings feel refined and contemporary."),
            ("Do you handle balcony railing in Bihar?", "Yes. Sudama Interiors supports balcony and staircase railing execution for residential and commercial projects."),
        ],
    },
    "panels": {
        "eyebrow": "Decorative Wall Panels",
        "local_intro": "Luxury PVC panels, fluted panels, WPC louvers, and PU panels for modern wall styling in Darbhanga interiors.",
        "overview": {
            "what": "Decorative panels turn plain walls into finished interior features with texture, depth, and material rhythm.",
            "where": "TV walls, bedroom headboards, entrance walls, shops, office cabins, passages, and living room features.",
            "why": "Clients choose panels when they want quick visual transformation, controlled cost, and a premium wall finish.",
        },
        "materials": [
            {"name": "PVC Panels", "what": "Lightweight decorative wall panels.", "used": "Feature walls, utility walls, commercial interiors.", "benefits": "Easy installation, moisture resistance, and budget-friendly styling.", "durability": "Good for interior use.", "maintenance": "Very low.", "visual": "Clean and versatile.", "pricing": "Budget practical"},
            {"name": "Fluted Panels", "what": "Vertical ribbed panels for depth and shadow.", "used": "TV walls, entry walls, partitions, and bedrooms.", "benefits": "Luxury texture, vertical height effect, and strong modern styling.", "durability": "Good to high by material grade.", "maintenance": "Low.", "visual": "Premium and architectural.", "pricing": "Mid-premium"},
            {"name": "WPC Louvers", "what": "Wood-polymer louver strips.", "used": "Partitions, wall accents, ceiling features, and living room details.", "benefits": "Warm look, termite resistance, and dimensional rhythm.", "durability": "High indoors.", "maintenance": "Low.", "visual": "Warm, modern, and rich.", "pricing": "Mid-premium"},
            {"name": "PU Panels", "what": "Decorative polyurethane panels with stone or molded looks.", "used": "Accent walls, boutique spaces, bedrooms, and statement zones.", "benefits": "Lightweight, dramatic texture, and fast transformation.", "durability": "Good for interior decorative use.", "maintenance": "Low.", "visual": "Bold and luxurious.", "pricing": "Premium feel"},
        ],
        "gallery": gallery_images("panels"),
        "faqs": [
            ("Which panel is best for a TV wall?", "Fluted panels and WPC louvers are popular for TV walls because they add depth without making the wall feel heavy."),
            ("Are PVC panels easy to maintain?", "Yes. PVC panels are lightweight, easy to clean, and practical for budget-conscious wall styling."),
            ("Can wall panels make a small room feel premium?", "Yes. The right vertical rhythm, lighting, and panel proportion can make compact rooms feel taller and more finished."),
        ],
    },
    "uv-marble-sheets": {
        "eyebrow": "UV Marble Sheets",
        "local_intro": "Premium UV marble sheet installation for wall applications, moisture-resistant luxury finishes, and polished interiors across Darbhanga and Bihar.",
        "overview": {
            "what": "UV marble sheets are glossy decorative wall sheets that recreate a polished marble look with lighter installation.",
            "where": "TV walls, bedroom walls, commercial counters, puja backdrops, lobbies, and moisture-prone wall zones.",
            "why": "Clients choose them for luxury visual impact, easier maintenance, and a premium marble-like finish without heavy stone work.",
        },
        "materials": [
            {"name": "Wall Applications", "what": "Large-format sheets applied to vertical surfaces.", "used": "TV units, lobby walls, headboards, and shop interiors.", "benefits": "Fast transformation, fewer joints, and strong reflective polish.", "durability": "Good in interior use.", "maintenance": "Low.", "visual": "Glossy, dramatic, and premium.", "pricing": "Mid-premium"},
            {"name": "Moisture Resistant Finish", "what": "A surface finish that performs better than many painted walls in splash-prone areas.", "used": "Wash areas, commercial counters, and selected kitchen walls.", "benefits": "Easy wipe-down, stain resistance, and clean shine.", "durability": "Good with correct installation.", "maintenance": "Very low.", "visual": "Clean and polished.", "pricing": "Premium practical"},
        ],
        "gallery": gallery_images("uv-marble-sheets"),
        "faqs": [
            ("Are UV marble sheets suitable for TV walls?", "Yes. They create a premium, glossy backdrop and pair well with warm lighting and slim cabinetry."),
            ("Are UV sheets waterproof?", "They are moisture-resistant for wall applications, but correct installation and edge finishing are important."),
            ("Do UV marble sheets look premium?", "Yes. With good lighting and clean joints, UV marble sheets can create a strong luxury wall effect."),
        ],
    },
    "laminates": {
        "eyebrow": "Premium Laminates",
        "local_intro": "Mica, acrylic, and PVC laminates for wardrobes, kitchens, doors, panels, and premium interior surfaces in Darbhanga.",
        "overview": {
            "what": "Laminates are decorative surface layers used to finish furniture, shutters, doors, wall panels, and modular interiors.",
            "where": "Kitchens, wardrobes, TV units, storage, office furniture, doors, and display counters.",
            "why": "Clients choose laminates for finish variety, durability, budget control, and the ability to create a cohesive interior palette.",
        },
        "materials": [
            {"name": "Mica Laminates", "what": "Durable decorative sheets for everyday interior surfaces.", "used": "Cabinets, wardrobes, doors, counters, and furniture.", "benefits": "Wide variety, strong practicality, and good cost control.", "durability": "High for daily interior use.", "maintenance": "Low.", "visual": "Versatile, matte to textured.", "pricing": "Budget to mid-premium"},
            {"name": "Acrylic Laminates", "what": "High-gloss premium laminates with a reflective finish.", "used": "Kitchens, wardrobes, premium shutters, and statement furniture.", "benefits": "Luxury gloss, rich color depth, and a showroom-like finish.", "durability": "Good with careful handling.", "maintenance": "Moderate; fingerprints need wiping.", "visual": "Glossy and expensive.", "pricing": "Premium"},
            {"name": "PVC Laminates", "what": "Flexible surface laminates used for curved and practical surfaces.", "used": "Wardrobes, kitchens, shutters, and decorative furniture edges.", "benefits": "Moisture handling, flexible application, and modern finishes.", "durability": "Good by grade.", "maintenance": "Low.", "visual": "Modern and clean.", "pricing": "Mid-range"},
        ],
       "gallery": gallery_images("laminates"),
        "faqs": [
            ("Which laminate is best for kitchens?", "Mica is practical and durable, while acrylic gives a more premium glossy finish for show kitchens and statement shutters."),
            ("Are acrylic laminates worth the price?", "They are worth it when a client wants high gloss, rich color, and a more premium showroom-like appearance."),
            ("Can laminates be used on doors and wardrobes?", "Yes. Laminates are widely used for doors, wardrobes, modular shutters, and built-in furniture surfaces."),
        ],
    },
}


def catalog_for(slug):
    return SERVICE_CATALOG.get(slug, {})
