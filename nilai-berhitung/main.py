"""
Web Profile : https://ryodev.my.id
Repo        : https://github.com/ryotwell/learn-python
"""

nilai_berhitung = [["Upin", 80, 90], ["Jarjit", 70, 75], ["Ipin", 94, 90], ["Mail", 88, 96], ["Ehsan", 92, 75]]

def getNilaiTertinggi(data):
    nilai_tertinggi = {"name": 0, "rata": 0}

    for user in data:
        rata_rata = (user[1] + user[2]) / 2
        
        if(rata_rata > nilai_tertinggi['rata']):
            nilai_tertinggi = {"name": user[0], "rata": rata_rata}

    return nilai_tertinggi
    
user = getNilaiTertinggi(nilai_berhitung)
print( f"Nilai tertinggi oleh {user['name']} dengan rata-rata {user['rata']}\n\nNama : {user['name']}\nNilai : {user['rata']}" )