import asyncio
import csv
from pathlib import Path
from playwright.async_api import async_playwright

OUTFILE = Path("msspalert_top250_2024.csv")

async def scrape():
    results = []

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, slow_mo=300)
        page = await browser.new_page()

        for page_num in range(1, 27):  # MSSPAlert tiene 26 páginas
            url = f"https://msspalert.com/top-250-2024?page={page_num}"
            print(f"Scraping {url}...")
            await page.goto(url)

            # Esperar que aparezca la lista
            await page.wait_for_selector("ul.list-unstyled li")

            # Extraer todos los <li>
            items = await page.query_selector_all("ul.list-unstyled li")

            for li in items:
                text = (await li.inner_text()).split("\n")
                # Ejemplo text: ["225 Aurora InfoTech", "Orlando, Florida, United States", "Aurora InfoTech is a highly specialized..."]

                if len(text) >= 3:
                    rank_name = text[0].strip()
                    location = text[1].strip()
                    description = text[2].strip()

                    # rank y nombre separados
                    parts = rank_name.split(" ", 1)
                    rank = parts[0]
                    name = parts[1] if len(parts) > 1 else ""

                    # url de la empresa (si existe link)
                    link_tag = await li.query_selector("a")
                    url = await link_tag.get_attribute("href") if link_tag else ""

                    results.append({
                        "rank": rank,
                        "name": name,
                        "url": url,
                        "location": location,
                        "description": description,
                    })

        await browser.close()

    return results


def main():
    data = asyncio.run(scrape())
    with OUTFILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["rank", "name", "url", "location", "description"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Wrote {len(data)} rows to {OUTFILE.resolve()}")


if __name__ == "__main__":
    main()