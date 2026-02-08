from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data Jadwal Kuliah berdasarkan gambar KRS Anda
jadwal_kuliah = [
    {"id": 0, "hari": "Senin", "jam": "06.30 - 08.10", "matkul": "Studi Al-Quran dan Al-Hadits", "ruang": "D.222", "deskripsi": "Mempelajari ayat-ayat Al-Quran dan hadits Nabi Muhammad SAW serta penerapannya dalam kehidupan sehari-hari", "tugas": []},
    {"id": 1, "hari": "Senin", "jam": "09.50 - 11.30", "matkul": "Database", "ruang": "B.306", "deskripsi": "Fundamental database design, SQL, normalization, dan manajemen data dalam sistem informasi", "tugas": []},
    {"id": 2, "hari": "Senin", "jam": "12.20 - 14.00", "matkul": "Web Programming Practicum", "ruang": "Lab. Multimedia", "deskripsi": "Praktek langsung mengembangkan aplikasi web responsif menggunakan HTML, CSS, JavaScript, dan framework modern", "tugas": []},
    {"id": 3, "hari": "Selasa", "jam": "06.30 - 09.00", "matkul": "Computer Network", "ruang": "B.317", "deskripsi": "Konsep jaringan komputer, protokol komunikasi, OSI model, dan arsitektur jaringan modern", "tugas": []},
    {"id": 4, "hari": "Selasa", "jam": "09.00 - 11.30", "matkul": "Software Engineering", "ruang": "B.316", "deskripsi": "Metodologi pengembangan software, SDLC, design patterns, dan best practices dalam engineering", "tugas": []},
    {"id": 5, "hari": "Rabu", "jam": "06.30 - 08.10", "matkul": "Web Programming", "ruang": "B.306", "deskripsi": "Teori dan praktek web programming termasuk frontend development dan server-side technologies", "tugas": []},
    {"id": 6, "hari": "Rabu", "jam": "08.10 - 09.50", "matkul": "Algorithm Complexity", "ruang": "B.314", "deskripsi": "Analisis kompleksitas algoritma, Big O notation, optimisasi algoritma, dan problem solving", "tugas": []},
    {"id": 7, "hari": "Rabu", "jam": "10.40 - 12.20", "matkul": "Computer Network Practicum", "ruang": "Lab. Computer Network", "deskripsi": "Praktek konfigurasi jaringan, troubleshooting, routing, dan security dalam lingkungan lab", "tugas": []},
    {"id": 8, "hari": "Kamis", "jam": "06.30 - 08.10", "matkul": "Database Practicum", "ruang": "Lab. Database", "deskripsi": "Praktek membuat database kompleks, query optimization, dan administrasi database real-world", "tugas": []},
    {"id": 9, "hari": "Kamis", "jam": "09.00 - 11.30", "matkul": "Bahasa Inggris Akademik", "ruang": "D.222", "deskripsi": "Peningkatan kemampuan bahasa Inggris akademik untuk presentasi, writing, dan komunikasi profesional", "tugas": []},
    {"id": 10, "hari": "Kamis", "jam": "11.30 - 14.00", "matkul": "Data Science", "ruang": "B.306", "deskripsi": "Machine learning, data analysis, visualization, dan practical application menggunakan Python", "tugas": []},
    {"id": 11, "hari": "Kamis", "jam": "14.00 - 15.40", "matkul": "Software Engineering Practicum", "ruang": "Lab. Mobile Programming", "deskripsi": "Pengembangan aplikasi mobile modern, architecture patterns, dan deployment ke production", "tugas": []},
]

@app.route('/')
def index():
    return render_template('index.html', jadwal=jadwal_kuliah)

@app.route('/matkul/<int:matkul_id>')
def matkul_detail(matkul_id):
    matkul = None
    for item in jadwal_kuliah:
        if item['id'] == matkul_id:
            matkul = item
            break
    if matkul is None:
        return redirect(url_for('index'))
    return render_template('matkul_detail.html', matkul=matkul, jadwal=jadwal_kuliah)

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