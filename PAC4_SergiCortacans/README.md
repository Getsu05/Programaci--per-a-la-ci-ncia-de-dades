# PAC4: Anàlisi Històrica de LaLiga (1995-2025)
**Estudiant:** Sergi Cortacans  
**Assignatura:** Programació per a la ciència de dades (22.503)  
**Universitat:** Universitat Oberta de Catalunya (UOC)  
**Data:** Juny 2026  

---

## 1. Descripció del Projecte
Aquest projecte consisteix en una aplicació modular de consola programada en Python per a l'anàlisi estadístic i exploratori de dades històriques de LaLiga (temporades 1995-96 a 2025-26). L'aplicació calcula mètriques de partits, distribucions de gols, taules de classificació històrica i genera visualitzacions avançades com un pòdium tricolor i un graf de xarxa d'enfrontaments directes.

---

## 2. Estructura i Organització de Carpetes
El projecte s'organitza de manera modular segons l'estàndard professional requerit:

```text
PAC4/
├── doc/                  # Documentació en format HTML generada de forma automàtica
├── img/                  # Gràfiques exportades durant l'anàlisi
├── screenshots/          # Captures de pantalla de validació d'autoria i execució
├── src/                  # Codi font de l'aplicació
│   ├── data/             # Conté el dataset
│   ├── exercises/        # Mòduls independents per a cada exercici de la PAC
│   │   ├── __init__.py   # Inicialitzador de paquet Python
│   │   ├── ex1.py, ex2.py, ex3.py, ex4.py, ex5.py, ex6.py, ex7.py
│   └── main.py           # Orquestrador principal del projecte (Punt d'entrada)
├── tests/                # Proves unitàries del projecte
│   └── tests_ex6.py
├── LICENSE               # Fitxer de llicència de distribució (MIT)
├── README.md             # Instruccions i documentació general del projecte (aquest fitxer)
└── requirements.txt      # Dependències de producció de l'aplicació