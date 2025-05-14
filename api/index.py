# api/index.py
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder="../templates")
produk = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "nama" in request.form and "stok" in request.form:
            nama = request.form["nama"]
            try:
                stok = int(request.form["stok"])
            except ValueError:
                stok = 0
            if nama not in produk:
                produk[nama] = stok
            return redirect(url_for("index"))
        elif "hapus_produk" in request.form:
            nama_hapus = request.form["hapus_produk"]
            if nama_hapus in produk:
                del produk[nama_hapus]
            return redirect(url_for("index"))
    return render_template("index.html", produk=produk)

@app.route("/tambah/<nama>")
def tambah_stok(nama):
    if nama in produk:
        produk[nama] += 1
    return redirect(url_for("index"))

@app.route("/kurangi/<nama>")
def kurangi_stok(nama):
    if nama in produk and produk[nama] > 0:
        produk[nama] -= 1
    return redirect(url_for("index"))

# Vercel akan menjalankan ini otomatis, tidak perlu `if __name__ == '__main__':`
