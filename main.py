import random
import pandas
from jinja2 import Template

t = Template('''
<html>
  <body>
    <table border="1">

      <tr>
      {%- for col in header %}
        <td>{{col}}</td>
      {%- endfor %}
      </tr>

      {% for row in rows -%}
      <tr>
      {%- for col in row %}
        <td>{{col if col is not none else '' }}</td>
      {%- endfor %}
      </tr>
      {% endfor %}

    </table>
  </body>
</html>
''')

class Jogo:
    def __init__(self, dezenas, total):
        self._dezenas    = None
        self._resultado  = None
        self._total      = None
        self._jogos      = None

        self.set_dezenas(dezenas)
        self.set_total(total)



    def get_dezenas(self):
        return self._dezenas

    def get_total(self):
        return self._total

    def set_dezenas(self, dezenas):
        if dezenas not in [6,7,8,9,10]:
            print("dezena precisa estar entre  6,7,8,9,10")

        else:
            self._dezenas = dezenas

    def set_total(self, total):
        self._total = total

    def __list_dezenas(self):
        dezenas = []
        while len(dezenas) < self._dezenas:
            rnd = random.randint(0,60)
            if rnd not in dezenas:
                dezenas.append(rnd)

        return sorted(dezenas)

    def add_jogos(self):
        jogos_list = []
        for i in range(self._total):
            jogos_list.append(self.__list_dezenas())

        self._jogos = jogos_list

    def sorteio(self):
        dezenas = []
        while len(dezenas) < 6:
            rnd = random.randint(0,60)
            if rnd not in dezenas:
                dezenas.append(rnd)

        self._resultado = sorted(dezenas)

    def print_jogos(self):
        return self._jogos

    def resultado_final(self):
        tabela_final = []
        for  jogo in self._jogos:
            ac = 0
            for dez in jogo:
                if dez in self._resultado:
                    ac += 1

            tabela_final.append([jogo, ac])

        #data = pandas.DataFrame(tabela_final, columns=['Jogo', 'Acertos'])
        #html = data.to_html()
        header = ['Jogo', 'Acertos']
        rows = tabela_final

        html = t.render(header=header, rows=rows)
        return html


j = Jogo(10,5)

j.add_jogos()
j.sorteio()
html = j.resultado_final()

print(html)
print(html)
with open('tabela.html',  'w') as tabela:
    tabela.write(html)