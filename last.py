import requests
import os
import signal
import subprocess

# Informasi Pembuat
AUTHOR = "InfernalXploit"
CREATOR = "InfernalXploit"
INSTAGRAM = "InfernalXploit"
TIKTOK = "renxploit1"
WHATSAPP = "6289648191199"

# Tampilkan informasi pembuat
os.system("clear")
print(f"""
######################################
#        DORKING BY {AUTHOR}
#    Creator : {CREATOR}
#    Instagram: {INSTAGRAM}          
#    TikTok: {TIKTOK}                
#    WhatsApp: {WHATSAPP}            
######################################
""")

# API Key dari Serper.dev
API_KEY = "313ae70288bcdb8f9ad25dfc46895a220ef72dae"

# Mulai memutar lagu di background
mpv_process = subprocess.Popen(["mpv", "--loop=inf", "p.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def google_dork(api_key, query):
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
    data = {"q": query, "gl": "id", "hl": "id", "num": 1000}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        results = response.json().get("organic", [])
        return [result["link"] for result in results]
    else:
        return []

# Nama file untuk menyimpan hasil
file_name = "hasil_dorking.txt"

# Loop input dork dari user
try:
    while True:
        dork_input = input("\nMasukkan dork (atau ketik 'exit' untuk keluar): ")
        if dork_input.lower() == "exit":
            break

        hasil = google_dork(API_KEY, dork_input)

        # Simpan hasil ke file
        with open(file_name, "a") as file:
            file.write(f"\n[DORK] {dork_input}\n")
            if hasil:
                for link in hasil:
                    file.write(link + "\n")
            else:
                file.write("Tidak ada hasil.\n")

        # Tampilkan hasil di terminal
        print("\n[HASIL DORKING]")
        if hasil:
            for link in hasil:
                print(link)
        else:
            print("Tidak ada hasil.")

        print(f"\nHasil juga disimpan di: {file_name}")

# Saat program dihentikan, musik juga berhenti
finally:
    os.kill(mpv_process.pid, signal.SIGTERM)
    print("\nProgram dihentikan, musik berhenti.")
