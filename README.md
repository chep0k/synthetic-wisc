# Simulated UW-Madison

100% data-accurate synthetic student population of UW-Madison. Access via [Live Explorer](#live-explorer).

## Documentation Index

```text
DATA.md  --->  ALGO.md, PRD.md   --->  UI.md
```
**[DATA.md](DATA.md)**: Documentation of the raw registrar source datasets and schemas. <br>
**[PRD.md](PRD.md)**: Product requirements and accuracy validation target metrics. <br>
**[ALGO.md](ALGO.md)**: Parallel generation dependency tree and step-by-step algorithms. <br>
**[UI.md](UI.md)**: User interface decisions, styling rules, and visualizer specifications. <br>

## Directory Structure

`./index.html`: [Live Explorer](#live-explorer) frontend.

`./eval_viewer.html`: Validation metrics viewer.

`./data`: All input tables from the university website, generated sqlite database (`virtual_university.db`), output validation files, and web assets. See [DATA.md](DATA.md).

`./src`: Python scripts for data preparation, synthetic generation, and lightweight validation guardrails:
```python
# generate `data/virtual_university.db` and `data/validation_data.js`
# uses `src/prepare_data.py` and `src/populate.py`
python src/build_database.py

# check 100% accuracy
python src/check_guardrails.py
```

`./*md`: documentation.

## Live Explorer

The interactive campus visualizer is deployed on GitHub Pages. Click the link to explore the simulated campus:

👉 **[https://chep0k.github.io/synthetic-wisc/](https://chep0k.github.io/synthetic-wisc/)**

## Authors & License

By [chep0k](https://github.com/chep0k). Released under MIT License.
