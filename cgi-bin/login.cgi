#!/usr/bin/python
#-*- coding: utf8 -*-

var = raw_input()
login=var.split("&")[0].split("=")[1]
senha=var.split("&")[1].split("=")[1]
def cabecalho():
	print ("content-type: text/html")
	print ("")

def imprimir(conteudo):
	cabecalho()
	print("<html><head><title>" + conteudo + "</title></head>")
	print("<body><h1>" + conteudo + "</h1></body></html>")

if login == "gabriel" and senha == "senha":
	cabecalho()
	f = open("site/menu.html", "r")
	arquivo=f.read()
	f.close
	print(arquivo)
else:
	imprimir("Usuário não encontrado ou senha incorreta")

