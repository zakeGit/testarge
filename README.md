# testarge

Yeni başlayan bir testarge projesi — Hermes Agent ile Zafer K. tarafından oluşturuldu.

## Hakkında

Bu repo bir başlangıç iskeleti olarak hazırlandı. Python ile yazılmış basit bir CLI uygulaması içerir.

## Kurulum

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Kullanım

```bash
python -m testarge --name Dünya
# çıktı: Merhaba, Dünya!
```

## Geliştirme

```bash
# Testleri çalıştır
pytest

# Lint
ruff check src/
```

## Lisans

MIT
