### **Streamlit – QRIS Payment Growth**

An interactive data application built with Streamlit.
This repository presents the results of a comprehensive 2025 survey analysis on the penetration and user experience of the Quick Response Code Indonesian Standard (**QRIS**). The data is visualized through an interactive web application developed using **Streamlit**, enabling flexible exploration across generational segments (Gen Z, Y, X).

![overviewpage1-Streamlit1.png](https://github.com/Ni-karo/Streamlit-QRISPaymentGrowth/blob/main/images/Overviewpage1.png?raw=true)
![overviewpage2-Streamlit2.png](https://github.com/Ni-karo/Streamlit-QRISPaymentGrowth/blob/main/images/Overviewpage2.png?raw=true)

### **Tech Stack & Dataset**

* **Platform:** **Streamlit** (Interactive Python web application)
* **Visualization:** Altair (Python visualization library)
* **Programming Language:** Python
* **Data:** [QRISPayment-Indonesia](https://github.com/Ni-karo/Streamlit-QRISPaymentGrowth/blob/main/QrisPayment.csv)
  (CSV data from a campus-wide survey on QRIS effectiveness)

### Key Insights**

1. **Gen Z dominates usage (85.3%)** → Strategy focus: **retention**, not acquisition.
2. **Satisfaction varies** → While Gen Y is satisfied with speed, **42%** of users want to reduce usage → *UX improvements needed*.
3. **High merchant-side errors** → **56.3%** of Gen Z experienced payment failures → requires better merchant education & system upgrades.
4. **Main barriers** → Concerns about **security/privacy** + **poor connectivity** remain major obstacles.

### **How to Run the Streamlit Application**

1. **Clone the Repository:**

   ```bash
   git clone [https://github.com/Ni-karo/Streamlit-QRISPaymentGrowth/tree/main]
   cd [Streamlit-QRISPaymentGrowth]
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *(Ensure `requirements.txt` includes `streamlit`, `pandas`, and `altair`*

3. **Run the App:**

   ```bash
   streamlit run qrisapp.py
   ```

### **Contributions**

Appreciate any form of contribution such as Streamlit code improvements, visualization suggestions, or discovering new insights from data.

---

### Streamlit - QRIS Payment Growth

Aplikasi Data Interaktif dengan Streamlit Streamlit.
Repositori ini menyajikan hasil analisis data survei komprehensif (Tahun 2025) mengenai penetrasi dan pengalaman pengguna Quick Response Code Indonesian Standard (**QRIS**). Data ini divisualisasikan melalui aplikasi web interaktif yang dikembangkan menggunakan **Streamlit**, memungkinkan eksplorasi data yang fleksibel berdasarkan segmentasi generasi (Gen Z, Y, X).

### Tech Stack & Dataset

  * **Platform:** **Streamlit** (Aplikasi web Python interaktif)
  * **Visualisasi:** Altair (python library)
  * **Bahasa Pemrograman:** Python
  * **Data:** [QRISPayment-Indonesia](https://github.com/Ni-karo/Streamlit-QRISPaymentGrowth/blob/main/QrisPayment.csv) (Data csv hasil survey lingkungan kampus terkait efektivitas QRIS).

### Key Insights

1. **Gen Z dominan (85.3%)** → Fokus strategi: **retensi**, bukan akuisisi.
2. **Kepuasan tidak merata** → Meski Gen Y puas soal kecepatan, **42%** pengguna ingin mengurangi pemakaian → *UX* perlu diperbaiki.
3. **Masalah di merchant tinggi** → **56.3%** Gen Z alami gagal bayar → butuh edukasi dan perbaikan sistem pedagang.
4. **Penghambat utama** → Kekhawatiran **keamanan/privasi** + **koneksi buruk** masih jadi barrier besar.

### Cara Menjalankan Aplikasi Streamlit:

1.  **Clone Repositori:**

    ```bash
    git clone [https://github.com/Ni-karo/Streamlit-QRISPaymentGrowth/tree/main]
    cd [Streamlit-QRISPaymentGrowth]
    ```

2.  **Instal Dependensi:**

    ```bash
    pip install -r requirements.txt
    ```

    *(Pastikan `requirements.txt` mencantumkan `streamlit`, `pandas`, dan `altair`*

3.  **Jalankan Aplikasi:**

    ```bash
    streamlit run qrisapp.py
    ```

### Kontribusi

Menghargai segala bentuk kontribusi seperti penyempurnaan kode Streamlit, saran visualisasi, atau penemuan wawasan baru dari data.
