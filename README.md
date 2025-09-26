# Mushroom Automation System

Project untuk sistem otomatisasi kumbung jamur tiram.
Fitur:
- Membaca sensor suhu & kelembapan (DHT22).
- Mengendalikan kipas (AC) dan pompa (DC) via relay.
- Log data setiap 2 detik.
- Kirim data ke database / file Excel.
- Aturan otomatis:
  - Kipas ON jika suhu > 27°C, OFF jika < 23°C.
  - Pompa ON jika kelembapan < 80%, OFF jika > 95%.
