from pathlib import Path


raiz = Path('.\hero-fandom')
pastas = ["imagens", "bootstrap"]
arquivos = ["index.html", "batman.html", "aranhico.html", "beleza.css"]


for pasta in pastas:
    subpasta = raiz / pasta
    subpasta.mkdir(parents=True, exist_ok=True)



for ficheiro in arquivos:
    (raiz / f"{ficheiro}").write_text("")



(raiz / "LICENSE").write_text("""

Licença Personalizada - Todos os Direitos Reservados\n\n


Copyright (c) 2025 Beny B Reis II 
Email: itsbenyreis@gmail.com 
Redes sociais: @bkapa8  or  @bybenb

Este software/projecto e todo o seu conteúdo são propriedade intelectual de "Beny B. Reis II".
É estritamente proibido copiar, modificar, distribuir, utilizar, sublicenciar ou comercializar qualquer parte deste código-fonte ou material relacionado, no todo ou 
em parte, sem autorização expressa e por escrito do autor. 

O uso não autorizado será considerado uma violação dos direitos autorais e poderá resultar em medidas legais.

""")
(raiz / "README.md").write_text("""
# Hero Fandom
Montei uma ___simples rede___ de paginas que fala de alguns personagens fictícios bwé conhecidos como Steve Rogers, Bruce Wayne.

Usei um [framework](BootsTrap)* para o CSS, que achei dias atrás. Muito Otimizador (^_^)

---

### Autor
*Beny B Reis II*
- Email: [itsbenyreis@gmail.com](mailto:itsbenyreis@gmail.com)

- Redes sociais: [@bkapa8](https://www.instagram.com/bkapa8) or também [@bybenb](https://linktr.ee/bybenb)


---

__Licença__: Este projeto está protegido por uma [__licença personalizada__](LICENSE) (_é curta,  então leia_ ^_^ ). Todos os
direitos reservados a __Beny B. Reis II__.


""")
print(f"\nO projecto foi criado com exito neste caminho\n>>> \"{raiz.as_posix()}\"")

print('--' * 25)
print(f"\n{'© 2025 KiamSoft. All rights reserved.':-^53}")
# programado por: Beny B.K. | @bkapa8
info_do_programador = input()
if info_do_programador == '24062005':
    print('''   * Info do Programador
Programado por: Beny Basaula Kiamvu
Idade: 19 anos
Rank: D
Level: Ge-Creator Baixo''')

    input()