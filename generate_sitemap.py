from datetime import datetime

INPUT_FILE = "sitemap.txt"
OUTPUT_FILE = "sitemap.xml"
LASTMOD = datetime.today().strftime('%Y-%m-%d')
DEFAULT_CHANGEFREQ = "monthly"
DEFAULT_PRIORITY = "0.8"

with open(INPUT_FILE, "r") as f:
    urls = [line.strip() for line in f if line.strip()]

xml_parts = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

for url in urls:
    priority = "1.0" if url.endswith("/") else DEFAULT_PRIORITY
    xml_parts.append("  <url>")
    xml_parts.append(f"    <loc>{url}</loc>")
    xml_parts.append(f"    <lastmod>{LASTMOD}</lastmod>")
    xml_parts.append(f"    <changefreq>{DEFAULT_CHANGEFREQ}</changefreq>")
    xml_parts.append(f"    <priority>{priority}</priority>")
    xml_parts.append("  </url>")

xml_parts.append("</urlset>")

with open(OUTPUT_FILE, "w") as f:
    f.write("\n".join(xml_parts))

