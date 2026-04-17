# Tools Repository

Questa cartella contiene gli script Python legacy utilizzati storicamente per le build, la pulizia e il refactoring della repository `Villa-del-Conte`.

In un progetto vanilla (senza bundler), questi script fungono da rimpiazzo occasionale di task-runner. 

**ATTENZIONE**: Molti di questi script sono ormai obsoleti e legati a migrazioni precedenti. Usare con cautela e solo in casi in cui si conosca esattamente lo scope del file.

## File chiave
- `fix_*.py` / `update_*.py` / `build_*.py` -> Task generici usati per bulk update nel tempo.
- `optimize_images.py` -> Esempio di script Python + Pillow usato per compilare formati wepb/breakpoints.
