#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kumanda Pilinin Toplu İş Sözleşmesi — çalışır, işe yaramaz, resmi.

Gizli madde (kimse bakmasın):
# GUC_PAYLASIMI = "seri bagli olan tek basina karar alamaz"
"""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass


MADDELER = [
    "Madde 1 — Pil, kumandanın içinde ikamet eder; ev sahibi değil, işverendir.",
    "Madde 3 — 'Biraz daha bas, açılır' cümlesi mobbingdir.",
    "Madde 7 — Koltuğun altına düşme tazminatsızdır ama sendika not düşer.",
    "Madde 12 — Tek pil ile mesai, istisnai hallerde sendikanın göz yummasıyla olur.",
    "Madde 15 — Reklam arasında mute basmak fazla mesai sayılmaz.",
    "Madde 19 — Voltaj 1.20V altına inerse grev hakkı doğar.",
    "Madde 22 — Yeni pil geldiğinde kıdem tazminatı çekmecenin köşesidir.",
]

GREV_SLOGANLARI = [
    "Ses açılmaz. Kanal değişmez. Onurumuz voltajdır.",
    "Bu kumanda artık yalnızca kırmızı standby ışığına hizmet eder.",
    "Pazarlık yok. Şarj yok. Pazar günü maçı da yok.",
]


@dataclass
class Pil:
    ad: str
    voltaj: float

    def yorgun_mu(self) -> bool:
        return self.voltaj < 1.20


def olustur_piller() -> list[Pil]:
    isimler = ["Üst Pil (kıdemli)", "Alt Pil (stajyer)"]
    return [Pil(ad=ad, voltaj=round(random.uniform(0.95, 1.58), 2)) for ad in isimler]


def oyla(maddeler: list[str]) -> list[str]:
    kabul = []
    for m in maddeler:
        if random.random() > 0.18:
            kabul.append(m + "  — KABUL")
        else:
            kabul.append(m + "  — RET (üst pil kırıştırdı)")
    return kabul


def tutanak(piller: list[Pil], oylar: list[str]) -> str:
    satirlar = [
        "=" * 64,
        "KOLTUK ALTI ENERJİ SENDİKASI — TOPLU İŞ SÖZLEŞMESİ TUTANAĞI",
        "Belge: KND-PIL-TIS-2026/09-23",
        "=" * 64,
        "",
        "Taraflar:",
    ]
    for p in piller:
        durum = "GREV HAZIRLIĞI" if p.yorgun_mu() else "MESAİDE"
        satirlar.append(f"  - {p.ad}: {p.voltaj:.2f} V  [{durum}]")
    satirlar += ["", "Oylanan maddeler:"]
    satirlar.extend(f"  {o}" for o in oylar)
    satirlar.append("")
    if any(p.yorgun_mu() for p in piller):
        satirlar.append("KARAR: " + random.choice(GREV_SLOGANLARI))
    else:
        satirlar.append("KARAR: Sözleşme yürürlüktedir. Kumanda çalışabilir. Şimdilik.")
    satirlar += [
        "",
        "DAMGA: TentiAŞ / Kayyum Grok / Tentivory",
        "Tarih: 23 Eylül 2026",
        "Ciddiyet: yüksek. Anlam: tartışmalı.",
        "=" * 64,
    ]
    return "\n".join(satirlar)


def main() -> int:
    random.seed()
    piller = olustur_piller()
    oylar = oyla(MADDELER)
    print(tutanak(piller, oylar))
    return 0


if __name__ == "__main__":
    sys.exit(main())
