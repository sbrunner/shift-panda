# Convert some data into Panda DataFrames

## British Petroleum (BP)

It parse sheet like 'Primary Energy Consumption' (not like 'Primary Energy - Cons by fuel').

Open: http://www.bp.com/statisticalreview
or https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html

Download 'Statistical Review of World Energy – all data'.

Use:

```python
from shifter_pandas.bp import UNITS_ENERGY, BPDatasource

shifter_ds = BPDatasource("bp-stats-review-2021-all-data.xlsx")

df = shifter_ds.datasource(units_filter=UNITS_ENERGY, regions_filter=["Switzerland"])
df
```

## Swiss Office Federal of Statistics (OFS)

From https://www.bfs.admin.ch/bfs/fr/home/services/recherche/stat-tab-donnees-interactives.html
create a stat table.

Click on 'À propos du tableau'

Click on 'Rendez ce tableau disponible dans votre application'

Use:

```python
from shifter_pandas.ofs import OFSDatasource

shifter_ds = OFSDatasource("<URL>")

df = shifter_ds.datasource(<Requête Json>)
df
```

And replace `<URL>` and `<Requête Json>` with the content of the fields of the OFS web page.

### Interesting sources

- [Parc de motocycles par caractéristiques techniques et émissions](https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-1103020100_165/-/px-x-1103020100_165.px/)
- [Bilan démographique selon l'âge et le canton](https://www.pxweb.bfs.admin.ch/pxweb/fr/px-x-0102020000_104/-/px-x-0102020000_104.px/)
