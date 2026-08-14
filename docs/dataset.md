# Dataset

This repo produces the `deezer_artists` dataset: a JSONL dump of Deezer artist records from the public Deezer API. The harvester walks sequential artist IDs and keeps rows that resolve to a named artist.

One row represents one artist.

## Format

The output is a JSONL file at `{output_dir}/deezer_artists.jsonl`. Each line is a flat JSON object with these fields:

| Field | Type | Description |
| --- | --- | --- |
| `deezer_id` | integer | Deezer artist ID |
| `name` | string | Artist name |
| `picture_url` | string or null | Artist picture URL |
| `nb_album` | integer or null | Number of albums |
| `nb_fan` | integer or null | Number of fans |
| `url` | string or null | Deezer artist page URL |

## How to generate

Install the package:

```bash
pip install pydeezer
```

Harvest artists:

```bash
pydeezer-harvest deezer_artists --output ~/.cache/metadatarr/scrapers/
```

Limit the ID range:

```bash
pydeezer-harvest deezer_artists --start 1 --end 100000 --output ~/.cache/metadatarr/scrapers/
```

Python equivalent:

```python
from pathlib import Path
from pydeezer.harvest.deezer_artists import DeezerArtistsSource

src = DeezerArtistsSource()
src.run(Path.home() / ".cache/metadatarr/scrapers")
```

## Publish on Hugging Face

Yes, with caveats. The dataset is a clean, compact artist catalog with fan and album counts. Before publishing, verify that redistribution of Deezer-derived metadata complies with the Deezer terms of service.

## ML tasks served

- Artist popularity prediction from album and fan counts.
- Music-artist entity linking.
- Recommendation-system candidate generation.
- Catalog coverage and gap analysis.
