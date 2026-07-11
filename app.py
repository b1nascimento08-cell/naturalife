from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/cosmeticos")
def cosmeticos():
    return render_template("cosmeticos.html")

@app.route("/hidratante")
def hidratante():
    return render_template("hidratante.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/abacate")
def abacate():
    return render_template("abacate.html")

@app.route("/cenoura")
def cenoura():
    return render_template("cenoura.html")

@app.route("/tomate")
def tomate():
    return render_template("tomate.html")

@app.route("/serum")
def serum():
    return render_template("serum.html")

@app.route("/protetor")
def protetor():
    return render_template("protetor.html")

@app.route("/mirtilo")
def mirtilo():
    return render_template("mirtilo.html")

@app.route("/uva")
def uva():
    return render_template("uva.html")

@app.route("/manga")
def manga():
    return render_template("manga.html")

@app.route("/banana")
def banana():
    return render_template("banana.html")

@app.route("/brocolis")
def brocolis():
    return render_template("brocolis.html")

@app.route("/castanhas")
def castanhas():
    return render_template("castanhas.html")

@app.route("/melancia")
def melancia():
    return render_template("melancia.html")

@app.route("/coco")
def coco():
    return render_template("coco.html")

@app.route("/ovo")
def ovo():
    return render_template("ovo.html")

@app.route("/salmao")
def salmao():
    return render_template("salmao.html")

@app.route("/espinafre")
def espinafre():
    return render_template("espinafre.html")

@app.route("/amendoas")
def amendoas():
    return render_template("amendoas.html")

@app.route("/receitas")
def receitas():
    return render_template("receitas.html")

@app.route("/vitamina-banana")
def vitamina_banana():
    return render_template("vitamina_banana.html")

@app.route("/vitamina-morango")
def vitamina_morango():
    return render_template("vitamina_morango.html")

@app.route("/suco-laranja-cenoura")
def suco_laranja_cenoura():
    return render_template("suco_laranja_cenoura.html")

@app.route("/vitamina-abacate")
def vitamina_abacate():
    return render_template("vitamina_abacate.html")

@app.route("/smoothie-kiwi")
def smoothie_kiwi():
    return render_template("smoothie_kiwi.html")

@app.route("/smoothie-manga")
def smoothie_manga():
    return render_template("smoothie_manga.html")

@app.route("/morango")
def morango():
    return render_template("morango.html")

@app.route("/kiwi")
def kiwi():
    return render_template("kiwi.html")

@app.route("/laranja")
def laranja():
    return render_template("laranja.html")

@app.route("/sabonete")
def sabonete():
    return render_template("sabonete.html")


@app.route("/creme")
def creme():
    return render_template("creme.html")

@app.route("/agua-micelar")
def agua_micelar():
    return render_template("agua_micelar.html")


@app.route("/mascara")
def mascara():
    return render_template("mascara.html")


@app.route("/esfoliante")
def esfoliante():
    return render_template("esfoliante.html")

@app.route("/gel-limpeza")
def gel_limpeza():
    return render_template("gel_limpeza.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)