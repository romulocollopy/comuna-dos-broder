"""Render the BR contract draft (branches/br/contract-draft.md) as a site page.

Run with the project venv python:
    ./.venv/bin/python presentation/build_contract.py
Writes presentation/html/contrato.html.
"""

import os
import re

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "branches", "br", "contract-draft.md")
OUT = os.path.join(HERE, "html", "contrato.html")

md_text = open(SRC, encoding="utf-8").read()
lines = md_text.split("\n")

# title = first `# ` line
title = ""
body_lines = lines
for i, ln in enumerate(lines):
    if ln.startswith("# "):
        title = ln[2:].strip()
        body_lines = lines[i + 1:]
        break

body = "\n".join(body_lines)
# drop the single leading `---` right after the title block (cosmetic)
body = re.sub(r"^\s*---\s*\n", "", body, count=1)

html_body = markdown.markdown(
    body,
    extensions=["tables", "sane_lists"],
)

page = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Terra Coletiva</title>
<link rel="stylesheet" href="../css/style.css">
</head>
<body>

<nav>
  <div class="wrap">
    <a class="brand" href="index.html">Terra Coletiva</a>
    <a href="index.html">Início</a>
    <a href="cenarios.html">Cenários</a>
    <a href="estresse.html">Estresse</a>
    <a href="renda.html">Renda</a>
    <a href="riscos.html">Riscos &amp; Vantagens</a>
    <a href="contrato.html" class="active">Contrato</a>
  </div>
</nav>

<header>
  <div class="wrap">
    <p class="kicker">Contrato</p>
    <h1>{title}</h1>
    <p class="lede">Rascunho completo, para revisão por advogado(a). Não é aconselhamento jurídico.</p>
  </div>
</header>

<main class="wrap">
{html_body}
</main>

<footer>
  <div class="wrap">
    <p><strong>Rascunho — não é aconselhamento jurídico.</strong> O texto final deve ser
    redigido e validado por advogado(a) antes da assinatura. Itens entre colchetes são
    parâmetros a definir; os pontos marcados exigem manifestação técnica.</p>
  </div>
</footer>

</body>
</html>
"""

open(OUT, "w", encoding="utf-8").write(page)
print("wrote", os.path.relpath(OUT, HERE), f"({len(page)} chars)")
