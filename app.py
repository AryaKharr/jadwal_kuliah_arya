from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# ============= Database Configuration =============
DATABASE_URL = os.environ.get('DATABASE_URL')
# Konversi URL ke format pg8000 driver
if DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql+pg8000://', 1) if DATABASE_URL.startswith('postgres://') else DATABASE_URL.replace('postgresql://', 'postgresql+pg8000://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ============= Database Models =============
class Jadwal(db.Model):
    __tablename__ = 'jadwal_kuliah'
    
    id = db.Column(db.Integer, primary_key=True)
    hari = db.Column(db.String(50), nullable=False)
    jam = db.Column(db.String(50), nullable=False)
    matkul = db.Column(db.String(100), nullable=False)
    ruang = db.Column(db.String(50), nullable=False)
    deskripsi = db.Column(db.Text, nullable=False)
    
    # Relationship dengan Tugas
    tugas_list = db.relationship('Tugas', backref='jadwal', lazy=True, cascade='all, delete-orphan', order_by='Tugas.id')
    
    def to_dict(self):
        return {
            'id': self.id,
            'hari': self.hari,
            'jam': self.jam,
            'matkul': self.matkul,
            'ruang': self.ruang,
            'deskripsi': self.deskripsi,
            'tugas': [{'id': tugas.id, 'nama': tugas.nama} for tugas in self.tugas_list]
        }

class Tugas(db.Model):
    __tablename__ = 'tugas'
    
    id = db.Column(db.Integer, primary_key=True)
    jadwal_id = db.Column(db.Integer, db.ForeignKey('jadwal_kuliah.id'), nullable=False)
    nama = db.Column(db.Text, nullable=False)

# Auto-create tables saat app start
with app.app_context():
    db.create_all()


# ============= Routes =============

@app.route('/')
def index():
    jadwal = Jadwal.query.all()
    jadwal_list = [item.to_dict() for item in jadwal]
    return render_template('index.html', jadwal=jadwal_list)

@app.route('/matkul/<int:matkul_id>')
def matkul_detail(matkul_id):
    matkul = Jadwal.query.get_or_404(matkul_id)
    jadwal = Jadwal.query.all()
    jadwal_list = [item.to_dict() for item in jadwal]
    matkul_dict = matkul.to_dict()
    return render_template('matkul_detail.html', matkul=matkul_dict, jadwal=jadwal_list)

@app.route('/tambah_tugas', methods=['POST'])
def tambah_tugas():
    matkul_id = int(request.form.get('matkul_id'))
    tugas_baru = request.form.get('tugas', '').strip()
    
    if tugas_baru:
        matkul = Jadwal.query.get(matkul_id)
        if matkul:
            new_tugas = Tugas(jadwal_id=matkul_id, nama=tugas_baru)
            db.session.add(new_tugas)
            db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/hapus_tugas', methods=['POST'])
def hapus_tugas():
    tugas_id = int(request.form.get('tugas_id'))
    
    tugas = Tugas.query.get(tugas_id)
    if tugas:
        db.session.delete(tugas)
        db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/init-db')
def init_db():
    """Endpoint untuk initialize database dengan data awal"""
    db.create_all()
    
    # Cek apakah data sudah ada
    if Jadwal.query.first() is not None:
        return "Database sudah diisi dengan data!"
    
    # Data Jadwal Kuliah awal
    initial_data = [
        {"hari": "Senin", "jam": "06.30 - 08.10", "matkul": "Studi Al-Quran dan Al-Hadits", "ruang": "D.222", "deskripsi": "Mempelajari ayat-ayat Al-Quran dan hadits Nabi Muhammad SAW serta penerapannya dalam kehidupan sehari-hari"},
        {"hari": "Senin", "jam": "09.50 - 11.30", "matkul": "Database", "ruang": "B.306", "deskripsi": "Fundamental database design, SQL, normalization, dan manajemen data dalam sistem informasi"},
        {"hari": "Senin", "jam": "12.20 - 14.00", "matkul": "Web Programming Practicum", "ruang": "Lab. Multimedia", "deskripsi": "Praktek langsung mengembangkan aplikasi web responsif menggunakan HTML, CSS, JavaScript, dan framework modern"},
        {"hari": "Selasa", "jam": "06.30 - 09.00", "matkul": "Computer Network", "ruang": "B.317", "deskripsi": "Konsep jaringan komputer, protokol komunikasi, OSI model, dan arsitektur jaringan modern"},
        {"hari": "Selasa", "jam": "09.00 - 11.30", "matkul": "Software Engineering", "ruang": "B.316", "deskripsi": "Metodologi pengembangan software, SDLC, design patterns, dan best practices dalam engineering"},
        {"hari": "Rabu", "jam": "06.30 - 08.10", "matkul": "Web Programming", "ruang": "B.306", "deskripsi": "Teori dan praktek web programming termasuk frontend development dan server-side technologies"},
        {"hari": "Rabu", "jam": "08.10 - 09.50", "matkul": "Algorithm Complexity", "ruang": "B.314", "deskripsi": "Analisis kompleksitas algoritma, Big O notation, optimisasi algoritma, dan problem solving"},
        {"hari": "Rabu", "jam": "10.40 - 12.20", "matkul": "Computer Network Practicum", "ruang": "Lab. Computer Network", "deskripsi": "Praktek konfigurasi jaringan, troubleshooting, routing, dan security dalam lingkungan lab"},
        {"hari": "Kamis", "jam": "06.30 - 08.10", "matkul": "Database Practicum", "ruang": "Lab. Database", "deskripsi": "Praktek membuat database kompleks, query optimization, dan administrasi database real-world"},
        {"hari": "Kamis", "jam": "09.00 - 11.30", "matkul": "Bahasa Inggris Akademik", "ruang": "D.222", "deskripsi": "Peningkatan kemampuan bahasa Inggris akademik untuk presentasi, writing, dan komunikasi profesional"},
        {"hari": "Kamis", "jam": "11.30 - 14.00", "matkul": "Data Science", "ruang": "B.306", "deskripsi": "Machine learning, data analysis, visualization, dan practical application menggunakan Python"},
        {"hari": "Kamis", "jam": "14.00 - 15.40", "matkul": "Software Engineering Practicum", "ruang": "Lab. Mobile Programming", "deskripsi": "Pengembangan aplikasi mobile modern, architecture patterns, dan deployment ke production"},
    ]
    
    for data in initial_data:
        jadwal = Jadwal(**data)
        db.session.add(jadwal)
    
    db.session.commit()
    return "Database berhasil diinisialisasi dengan data awal!"




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)