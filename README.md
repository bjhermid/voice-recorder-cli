# Python Learning - VOICE RECORDER CLI
### [*Learning Purpose*]
🖥️ 📖 -Mini Project ini aku buat untuk belajar Python dengan model "Reverse Engineer" dan Trial & Error- 🚀 🚀.
Dalam proses pada mini project ini berfokus untuk mempelajari **alur dari *scratch*** hingga bisa mengerti bagaimana sebuah project dalam pemrograman python dilakukan. Juga belajar hal-hal lain termasuk dalam menulis README.MD ini.


> Status Belajar : Masuk Minggu ke-4 cheers 🥂🥂

## Apa Yang Dipelajari 📖 :

 1. Penggunaan uv (Python Pacakge and Project Manager)
 2. Penggunaan .git (.gitignore, .gitkeep dll)
 3. Struktur File suatu project pada Python.
 4. Virtual Environment
 5. Konfigurasi pada .yml, .toml, settings.json dan lainnya
 6. Inisiasi Project dari awal
 7. Basic CI Pipeline dengan (Pre-commit dan Ruff) menggunakkan uv/uvx
 8. Belajar CLI dengan click dan rich.
 9. Menulis.


### Recordings folder
- Semua hasil voice recorder ditaruh di folder `recordings/`.
- Git mengabaikan isi dari folder kecuali .gitkeep

`.gitignore` rules used:
```gitignore
recordings/*
!recordings/.gitkeep
```

## 📦 Depedencies
- [sounddevice](https://pypi.org/project/sounddevice/) – untuk merekam audio real-time melalui microphone
- [soundfile](https://pypi.org/project/SoundFile/) – untuk membaca/menulis file audio (format WAV, FLAC, OGG, dsb.)
- [wavio](https://pypi.org/project/wavio/) – untuk menyimpan audio ke format WAV
- [scipy](https://pypi.org/project/scipy/) – untuk pemrosesan sinyal (filtering, FFT, analisis audio)
- [numpy](https://pypi.org/project/numpy/) – untuk operasi numerik & array
- [click](https://pypi.org/project/click/) – untuk membuat command line interface (CLI)
- [rich](https://pypi.org/project/rich/) – untuk output CLI berwarna, tabel, progress bar, logging

## 🛠️ Installation
1. Install UV
	Bisa dilihat disini [https://github.com/astral-sh/uv]
```bash
#Dengan pip:
	pip install uv
```
```bash
#atau pipx:
	pipx install uv
```
2. Clone repo and :
```bash
#clone Repo and
cd vrecord-cli
#Install Depedencies
uv sync && uv sync --dev
# See CLI help
uv run vrecord --help
# List input devices
uv run vrecord devices
```
## 👟 Running

Untuk menjalankan bisa dilakukan sebagai berikut :
Gunakan ```--backend``` untuk pilih menggunakan apa file WAV ditulis:
- ```soundfile``` (default):
Streams mic input to disk via libsndfile. Lowest memory usage. Best for long recordings.
- ```wavio```:
Buffers entire recording in memory then writes once. Simple, suitable for short clips.
- ```scipy```:
Similar to wavio, writes with ```scipy.io.wavfile```.

### Jalankan:
```bash
uv sync
uv run vrecord --help
uv run vrecord devices
uv run vrecord record -d 5 -o recordings/sample.wav
uv run vrecord record -d 5 -o recordings/sample_wavio.wav --backend wavio
uv run vrecord record -d 5 -o recordings/sample_scipy.wav --backend scipy
```

😀😀😀
