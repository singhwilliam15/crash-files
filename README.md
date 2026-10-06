# The Crash Files

An interactive casebook of 57 market crashes, shocks and scams from Tulip Mania (1637) to the 2025 tariff crash, including Indian cases such as Harshad Mehta, Satyam, IL&FS and Adani–Hindenburg.

Each case covers:

- The story in five beats: build-up, execution, trigger, fallout and lesson
- Headline loss in US dollars, how far the market fell, and how long it took to recover
- Key dates
- Links to official and regulator reports (FCIC, SEC, Fed, SEBI, RBI, ESMA, FINMA and others), news coverage and background reading

The dashboard compares all cases: losses on a log scale, market fall against recovery time, and cases by decade.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Files

| File | What it is |
| --- | --- |
| `app.py` | Streamlit app that displays the casebook full screen |
| `crash_files.html` | The casebook itself (self-contained HTML, CSS and JavaScript) |
| `requirements.txt` | Python dependencies |
| `.streamlit/config.toml` | Streamlit settings |

## Note on figures

Figures are approximate and are drawn from the linked reports, news coverage and general knowledge. Dollar losses measure different things (market value, fraud size, fines, liabilities), so read them as orders of magnitude. Check exact numbers against the primary sources before quoting them.

Built by William ([@singhwilliam15](https://github.com/singhwilliam15)).
