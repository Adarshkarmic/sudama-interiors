from django.db import migrations


REAL_SERVICES = [
    {
        "title": "Doors, Windows, Casement & Louver Systems",
        "slug": "doors-windows-casement-louver-systems",
        "short_description": "uPVC, aluminium, steel, WPC, and plywood systems for premium windows, doors, casements, and louvers in Darbhanga and Bihar.",
        "description": "A complete opening-system service for homes and commercial interiors, helping clients choose the right material for comfort, durability, ventilation, security, and visual finish.",
        "image": "services/doors-windows/doors-windows_sliding-casement_3.jpeg",
    },
    {
        "title": "ACP Cladding",
        "slug": "acp-cladding",
        "short_description": "Modern residential and shop ACP cladding for clean facades, signage bands, and premium exterior identity in Darbhanga.",
        "description": "ACP cladding creates a sharp, modern exterior surface for home elevations, shop fronts, and commercial facades with durable, low-maintenance visual impact.",
        "image": "services/acp-cladding/acp-cladding_applications_3.jpeg",
    },
    {
        "title": "False Ceiling",
        "slug": "false-ceiling",
        "short_description": "PVC, WPC, POP, and gypsum false ceiling services in Bihar with layered lighting, clean proportions, and premium room depth.",
        "description": "False ceiling design shapes lighting, conceals services, improves proportions, and gives rooms a more complete interior atmosphere.",
        "image": "services/false-ceiling/false-ceiling_pop_1.jpeg",
    },
    {
        "title": "Steel & SS Railing",
        "slug": "steel-ss-railing",
        "short_description": "Modern steel and stainless steel staircase and balcony railings with matte, polished, and premium finish options.",
        "description": "Steel and SS railing systems bring safety, long-term durability, and a refined architectural line to staircases, balconies, terraces, and commercial interiors.",
        "image": "services/steel-ss-railing/photo_2026-05-13_00-03-03.jpg",
    },
    {
        "title": "Panels",
        "slug": "panels",
        "short_description": "PVC panels, fluted panels, WPC louvers, and PU panels for luxury wall styling, TV walls, partitions, and interior feature zones.",
        "description": "Decorative panels add texture, depth, and premium rhythm to interior walls while giving clients a faster way to transform plain surfaces.",
        "image": "services/panels/pvc-panels_3.jpeg",
    },
    {
        "title": "UV Marble Sheets",
        "slug": "uv-marble-sheets",
        "short_description": "Glossy UV marble sheets for luxury wall applications, moisture-resistant surfaces, TV walls, counters, and premium interiors.",
        "description": "UV marble sheets create a polished marble-like finish for feature walls and commercial surfaces with lighter installation and easy maintenance.",
        "image": "services/uv-marble-sheets/digital-uvs_2.jpeg",
    },
    {
        "title": "Laminates",
        "slug": "laminates",
        "short_description": "Mica, acrylic, and PVC laminates for kitchens, wardrobes, furniture, doors, and premium surface finishing in Darbhanga.",
        "description": "Laminates provide durable, design-rich surface finishes for modular interiors, helping clients balance budget, texture, gloss, and long-term usability.",
        "image": "services/laminates/acrylic-laminates_3.jpeg",
    },
]


def rebuild_services(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    Service.objects.all().delete()
    for item in REAL_SERVICES:
        Service.objects.create(**item)


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0005_luxury_studio_rebuild"),
    ]

    operations = [
        migrations.RunPython(rebuild_services, migrations.RunPython.noop),
    ]
