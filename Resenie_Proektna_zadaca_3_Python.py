#Опис:Систем каде вработените внесуваат дневни задачи и добиваат извештај за 
#работното време

vk_br_vrab = int(input("Vnesete go vkupniot broj na vraboteni: "))

casovi_site_vrab = 0
vraboteni_info = []


for i in range(vk_br_vrab):
    print(f"n\Vraboten {i+1}")
    ime = input("Vnesete go imeto na vraboteniot: ")

    br_zad = int(input("Vnesete go brojot na zadaci po vraboten: "))
    casovi_po_vraboten = 0
    zadaci = []
    for j in range (br_zad):
        opis = input("Vnesi opis na {j} zadaca")
        casovi_po_zadaca = float(input("Vnesi broj na casovi potreben za zavrsuvanje na {j} zadaca"))
        casovi_po_vraboten += casovi_po_zadaca
        zadaci.append((opis,casovi_po_zadaca))

    casovi_site_vrab += casovi_po_vraboten
    vraboteni_info.append({
        "ime": ime,
        "zadaci": zadaci,
        "Vkupno casovi": casovi_po_vraboten
    })



#Output
print("\n----Izvestaj za rabotnoto vreme----")

for vraboten in vraboteni_info:
    print(f"\nVraboten: {vraboten['ime']}")
    print("Zadaci: ")
    for zadaca in zadaci:
        print(f"  - {zadaca[0]}: {zadaca[1]} casovi")

    print(f"Vkupno casovi za {vraboten['ime']}: {vraboten['Vkupno casovi']} casovi")

print("\n------------------------------------------------")
print(f"Vkupen broj casovi za site vraboteni e {casovi_site_vrab} casovi") 