import requests
from django.core.management.base import BaseCommand
from ...models import Country


class Command(BaseCommand):
    help = "Fetch and store country data from restcountries.com"

    def handle(self, *args, **kwargs):
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)
        if response.status_code != 200:
            self.stderr.write(self.style.ERROR("Failed to fetch data"))
            return

        data = response.json()

        for item in data:
            try:
                country, created = Country.objects.update_or_create(
                    cca3=item.get("cca3"),
                    defaults={
                        "name_common": item["name"]["common"],
                        "name_official": item["name"]["official"],
                        "cca2": item.get("cca2", ""),
                        "cioc": item.get("cioc", ""),
                        "region": item.get("region", ""),
                        "subregion": item.get("subregion", ""),
                        "capital": item.get("capital", []),
                        "area": item.get("area", 0.0),
                        "population": item.get("population", 0),
                        "timezones": item.get("timezones", []),
                        "flag_emoji": item.get("flag", ""),
                        "flag_png": item.get("flags", {}).get("png"),
                        "flag_svg": item.get("flags", {}).get("svg"),
                        "borders": item.get("borders", []),
                        "languages": item.get("languages", {}),
                        "currencies": item.get("currencies", {}),
                        "maps_google": item.get("maps", {}).get("googleMaps"),
                        "maps_osm": item.get("maps", {}).get("openStreetMaps"),
                        "landlocked": item.get("landlocked", False),
                        "tlds": item.get("tld", []),
                    }
                )
                msg = "Created" if created else "Updated"
                self.stdout.write(self.style.SUCCESS(f"{msg} {country.name_common}"))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Error processing country: {e}"))
