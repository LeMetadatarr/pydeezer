# pydeezer

Deezer artist catalog bulk harvester grouped onto the
[harvestkit](https://github.com/LeMetadatarr/harvestkit) resumable-harvest
engine. Extracted from [metadatarr](https://github.com/TigreGotico/metadatarr)'s
scraper collection into its own standalone package.

## Sources

| Scraper | Registry name | Source |
| --- | --- | --- |
| `deezer_artists` | `deezer_artists` | Deezer public API, sequential artist-id walk |

## Install

```bash
pip install pydeezer
# or, for the HuggingFace publisher (via harvestkit):
pip install "pydeezer[hf]"
# or, for Cloudflare-guarded sources:
pip install "pydeezer[stealth]"
```

## Usage

```bash
# list every registered scraper
pydeezer-harvest --list

# harvest one source (resumable — safe to Ctrl-C and rerun)
pydeezer-harvest deezer_artists --output ~/.cache/metadatarr/scrapers/
```

Every scraper is a `harvestkit.engine.Source` subclass: checkpoint/dedup/
pagination/throttle are handled by the shared engine, each module only
answers `initial_cursor()` and `fetch(cursor)`. See
[harvestkit](https://github.com/LeMetadatarr/harvestkit) for the full engine
API.

## License

Apache-2.0
