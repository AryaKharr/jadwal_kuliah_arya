from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data Jadwal Kuliah berdasarkan gambar KRS Anda
jadwal_kuliah = [
    {"id": 0, "hari": "Senin", "jam": "08.30 - 09.10", "matkul": "Studi Al-Quran dan Al-Hadits", "ruang": "D.222", "tugas": []},
    {"id": 1, "hari": "Senin", "jam": "09.50 - 11.30", "matkul": "Database", "ruang": "B.306", "tugas": []},
    {"id": 2, "hari": "Senin", "jam": "12.20 - 14.00", "matkul": "Web Programming Practicum", "ruang": "Lab. Multimedia", "tugas": []},
    {"id": 3, "hari": "Selasa", "jam": "08.30 - 09.10", "matkul": "Computer Network", "ruang": "B.317", "tugas": []},
    {"id": 4, "hari": "Selasa", "jam": "09.50 - 11.30", "matkul": "Software Engineering", "ruang": "B.316", "tugas": []},
    {"id": 5, "hari": "Rabu", "jam": "08.30 - 09.10", "matkul": "Web Programming", "ruang": "B.306", "tugas": []},
    {"id": 6, "hari": "Rabu", "jam": "09.10 - 10.40", "matkul": "Algorithm Complexity", "ruang": "B.314", "tugas": []},
    {"id": 7, "hari": "Rabu", "jam": "10.40 - 12.20", "matkul": "Computer Network Practicum", "ruang": "Lab. Computer Network", "tugas": []},
    {"id": 8, "hari": "Kamis", "jam": "08.30 - 09.10", "matkul": "Database Practicum", "ruang": "Lab. Database", "tugas": []},
    {"id": 9, "hari": "Kamis", "jam": "09.10 - 11.30", "matkul": "Bahasa Inggris Akademik", "ruang": "D.222", "tugas": []},
    {"id": 10, "hari": "Kamis", "jam": "11.30 - 13.10", "matkul": "Data Science", "ruang": "B.306", "tugas": []},
    {"id": 11, "hari": "Kamis", "jam": "13.10 - 14.50", "matkul": "Software Engineering Practicum", "ruang": "Lab. Mobile Programming", "tugas": []},
]

@app.route('/')
def index():
    return render_template('index.html', jadwal=jadwal_kuliah)

@app.route('/tambah_tugas', methods=['POST'])
def tambah_tugas():
    matkul_id = int(request.form.get('matkul_id'))
    tugas_baru = request.form.get('tugas', '').strip()
    if tugas_baru:
        for item in jadwal_kuliah:
            if item['id'] == matkul_id:
                item['tugas'].append(tugas_baru)
                break
    return redirect(url_for('index'))

@app.route('/hapus_tugas', methods=['POST'])
def hapus_tugas():
    matkul_id = int(request.form.get('matkul_id'))
    tugas_index = int(request.form.get('tugas_index'))
    for item in jadwal_kuliah:
        if item['id'] == matkul_id and 0 <= tugas_index < len(item['tugas']):
            item['tugas'].pop(tugas_index)
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)