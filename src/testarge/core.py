"""testarge çekirdek mantığı."""
from __future__ import annotations


def greet(name: str) -> str:
    """Verilen isme bir selam döndürür."""
    name = (name or "").strip() or "Dünya"
    return f"Merhaba, {name}!"
