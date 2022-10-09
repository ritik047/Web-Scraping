from bs4 import BeautifulSoup
import requests
from rich.console import Console
from rich.table import Table

table = Table(title="Coin's Price")

table.add_column("S. No.", style="cyan", no_wrap=True)
table.add_column("Coin Name", style="magenta")
table.add_column("Price", justify="left", style="green")

url="https://coinmarketcap.com/"
result=requests.get(url).text
doc=BeautifulSoup(result,"html.parser")

tbody=doc.tbody
trs=tbody.contents
    

for i,tr in enumerate(trs[:10]):
    name,price=tr.contents[2:4]
    table.add_row(str(i+1),name.text,price.text)

console = Console()
console.print(table)
