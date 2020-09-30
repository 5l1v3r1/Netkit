<h1>🐉 Netkit</h1>

[![License](https://img.shields.io/badge/License-MIT-critical.svg?style=flat-square)](https://github.com/Fzinxl/Netkit/blob/master/LICENSE/)
[![Python3.8](https://img.shields.io/badge/Python-3.8-yellow.svg?style=flat-square&logo=python)](https://www.python.org/)

> Netkit é uma tool de canivete suiço inspirado no netcat, o seu diferencial é que ele é focado em ações diferentes, como automatização sqli, sniffing e etc.... 


**Versão:** *`1.0 em desenvolvimento.`*


![Netkit](https://i.imgur.com/UWLFK2a_d.webp?maxwidth=640&shape=thumb&fidelity=medium)

*Imagem meramente ilustrativa do Netkit Alpha 1.0.*

<br>

**Instalação:**

```
$ git clone https://github.com/Fzinxl/Netkit
$ cd Netkit ; pip3 install -r requirements.txt
```

<br>

**Com ele você pode:**

> **•  Escutar portas;**

> **• Se conectar a hosts;**

> **• Após se conectar ou começar a escutar uma porta pode executar algo;**

> **• Usar como dns resolver;**

> **• Usar como reverse dns resolver;**

> **• Usar para automatização sqli.**

<br>

<h1>Netkit Help</h1>


**Netkit Help:**

<table>
 
 <tr>
  <td>Parâmetro</td><td>Argumento</td><td>Descrição</td>
  </tr>
 
  <tr>
 <td>-l</td><td>[port]</td><td>To listen a port.</td>
 </tr>
 
 <tr>
   <td>-m</td><td>[number]</td><td>To set max of connections.</td>
 </tr>

<tr> 
 <td>-c</td><td>[address] [port]</td><td>To connect in something.</td>
  </tr>

<tr>
  <td>-e</td><td>[command]</td><td>To exec one command.</td>
</tr>

<tr>
   <td>--dnsr</td><td>[domain]</td><td>To exec dns resolver.</td>
  </tr>
  
  <tr>
   <td>--rdns</td><td>[address]</td><td>To exec reverse dns resolver.</td>
  </tr>
  
  <tr>
   <td>--sqli</td><td>[url] [options]</td><td>To unlock sqli automation commands.</td>
  </tr>
  
</table>
