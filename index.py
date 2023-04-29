#Analisador Quake

with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
    mensagem = arquivo.read()
print(mensagem)
for linha in mensagem:
    if "Os doi morreram" in linha:
        print(linha)
        
   #Quake Parser
#Task 1

#O player1 "RPG" morreu pois estava ferido e caiu de uma altura que o matou. Ele tentou resistir, mas não conseguiu.

#O player1 "RPG" antes de morrer, matou o player2 "Inimigo" e "Zeh", que era uns dos maiores animigos dele usando a arma laser.

#Os três morreram "game_1: {
    #total_kills: 45;
    #players: ["Inimigo", "RPG", "Zeh"]
    #kills: {
      #"Inimigo": 5,
      #"RPG": 18,
      #"Zeh": 20
 #   }
 # }" "
     
import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
  return 'O Player1 matou os dois animigos e acabou se ferindo e morrendo'
  
app.route('/')
def contatos():
  return 'O player1 "RPG" antes de morrer, matou o player2 "Inimigo" e "Zeh", que era uns dos maiores animigos dele usando a arma laser.'
  
app.run(host='0.0.0.0')
  
game = pd.read_csv("mensagem.txt")
print(game)