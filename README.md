# IGonnaMakeYouCry

Höfundar:

Daníel Þór Guðmundsson dthg7@hi.is

Agnar Pétursson agp11@hi.is



í þessu verkefni fáum við að kynnast einföldum gíslatökubúnaði. Gíslatökubúnaður taka gögn á tölvu í gíslingu með
því að dulkóða þau og býðst til að afkóða gögnin gegn greiðslu, þá yfirleitt í formi rafmynntar (s.s. Bitcoin). Dæmi um þekktan gíslatökubúnað
er WannaCry sem herjaði meðal annars á breska heilbrigðiskerfið árið 2017.

Tilgangur verkefnisins er að sýna fram á svokallað "proof-of-conecpt" hvernig hægt er að smíða einfaldan gíslatökubúnað. Þrátt fyrir að 
flestir nútíma gíslatökubúnaðir eru flóknir og fágaðir þá er hægt að útfæra einfalda útgáfu af honum með tiltölulega litlum kóða. Höfundar hugbúnaðarins
mun vel eftir þegar WannaCry herjaði á tölvur heimsins og hugmyndin um að smíða sinn eigin gíslatökubúnað kom snemma upp í námskeiðinu. 

Ofan á þetta bættum við smá "social-engineering" twist á hugbúnaðinn. Hugbúnaðurinn dulbýr sig sem "Vírus hreinsir" þannig að fórnarlambið
keyrir forritið sjálft. Þegar "vírus hreinsirinn" eru keyrður mun tölvan verða dulkóðuð. Þá mun hugbúnaðurinn sína sitt rétta andlit og
krefst greiðslu til að geta afkóðað tölvuna aftur. 

Með því að notfæra okkur hina ýmsu pakka sem Python býður upp á ásamt einföldum gagnagrunnstengingum höfum við sýnt hvernig hægt er að smíða 
gíslatökubúnað. Hugbúnaðurinn samanstendur af þremur python skriftum sem eru skrifaðar í Python3:
* **ransom.py:** Sér um alla virkni sem kemur að dulkóðun og afkóðun
* **KeyManager.py:** Sér um gagnagrunnstengingar
* **GUI.py:** Útfærir viðmótið

Þessu er síðan öllu pakkað saman í eina keyranlega, **Virus Cleaner**, skrá sem finna má í **dist** möppunni.

# Keyrsluleiðbeiningar

Keyranlega skráin inniheldur alla þá pakka sem þarf svo það þarf ekki að setja upp neina pakka. Til að keyra hugbúnaðinn er nóg að keyra 
keyrsluskránna. Notendaviðmótið er einfalt og ætti það að skýra sig sjálft hvernig það virkar.



Setja upp:
sudo apt-get install python3-tk
sudo apt-get install python3-psycopg2
sudo apt-get install python3-dev

Setja upp pip pakka í virtualenv:
pip install -r requirements.txt

Þá er hægt að keyra forritið með
python3 GUI.py

Ef það er áhugi á að búa til nýja keyranlega skrá er hægt að keyra
pyinstaller GUI.spec 
áður en það er gert þarf að breyta slóðinni fyrir datas og pathex þannig hún sé rétt fyrir tölvuna þína.

