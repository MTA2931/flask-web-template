# 🧩 قالب آماده وب فارسی با Flask

یک پروژه **Open Source، رایگان و قابل شخصی‌سازی** برای راه‌اندازی وبسایت دانلود و مدیریت قالب‌های آماده **HTML / CSS / JavaScript** با استفاده از **Python و Flask**.

این پروژه با تمرکز روی رابط کاربری فارسی، راست‌چین، SEO، پنل مدیریت و ساختار ساده و قابل توسعه طراحی شده است.

> 🚀 مناسب برای توسعه‌دهندگان، طراحان وب و افرادی که می‌خواهند یک پلتفرم دانلود قالب را شخصی‌سازی و توسعه دهند.

---

## ✨ ویژگی‌ها

### 🌐 بخش عمومی

* 🏠 صفحه اصلی
* 🎨 نمایش قالب‌های آماده
* 📄 صفحه جزئیات هر قالب
* 📥 دانلود قالب‌ها
* 🎫 سیستم پشتیبانی و تیکت
* 📞 صفحه تماس
* ℹ️ صفحه درباره ما
* 📱 طراحی کاملاً Responsive
* 🌙 رابط کاربری مدرن
* ✨ انیمیشن‌ها و Hover Effects
* 🇮🇷 پشتیبانی کامل از زبان فارسی و RTL

### 🔐 پنل مدیریت

* 🔑 سیستم ورود مدیر
* 📊 داشبورد مدیریت
* 🎨 مدیریت قالب‌ها
* ➕ افزودن قالب جدید
* ✏️ ویرایش قالب‌ها
* 🗑️ حذف قالب‌ها
* 📥 مدیریت دانلودها
* 👥 مدیریت مدیران
* 🎫 مدیریت تیکت‌های پشتیبانی

### 🚀 SEO

* Meta Title
* Meta Description
* Meta Keywords
* Open Graph
* Twitter Card
* JSON-LD
* `sitemap.xml`
* `robots.txt`
* URLهای مناسب موتورهای جستجو
* ساختار مناسب برای توسعه SEO

---

## 🛠️ تکنولوژی‌ها

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge\&logo=flask\&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Frontend-1572B6?style=for-the-badge\&logo=css3\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)

</div>

---

## 📋 پیش‌نیازها

برای اجرای پروژه به موارد زیر نیاز دارید:

* 🐍 Python 3.10 یا بالاتر
* 📦 pip
* 🧰 Git

---

## 🚀 نصب و اجرا

### 1️⃣ دریافت پروژه

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### 2️⃣ ساخت Virtual Environment

#### Windows

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

---

### 4️⃣ اجرای پروژه

```bash
python app.py
```

بعد از اجرای سرور، پروژه به صورت پیش‌فرض روی آدرس زیر در دسترس خواهد بود:

```text
http://localhost:5000
```

---

## 🔐 پنل مدیریت

پنل مدیریت از مسیر زیر قابل دسترسی است:

```text
/admin/login
```

برای امنیت بیشتر، اطلاعات ورود مدیر را در محیط توسعه خودتان تنظیم کنید و **اطلاعات ورود واقعی را داخل Repository عمومی قرار ندهید.**

---

## 📦 افزودن قالب

بعد از ورود به پنل مدیریت:

1. وارد بخش **قالب‌ها** شوید.
2. گزینه **افزودن قالب** را انتخاب کنید.
3. نام قالب را وارد کنید.
4. توضیحات قالب را اضافه کنید.
5. تصویر Preview را آپلود کنید.
6. فایل ZIP قالب را آپلود کنید.
7. اطلاعات SEO را وارد کنید.
8. قالب را ذخیره کنید.

قالب پس از ذخیره در بخش عمومی سایت قابل نمایش خواهد بود.

---

## 📁 ساختار پروژه

```text
project/
│
├── app.py                  # نقطه ورود Flask
├── config.py               # تنظیمات پروژه
├── requirements.txt        # وابستگی‌های Python
├── .env                    # تنظیمات محیطی - در Git قرار نگیرد
├── .gitignore
│
├── models/
│   └── database.py         # مدل‌های دیتابیس
│
├── routes/
│   ├── public.py           # مسیرهای عمومی
│   └── admin.py            # مسیرهای پنل مدیریت
│
├── templates/              # قالب‌های HTML
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/            # فایل‌های آپلودی
│
└── instance/
    └── *.db                # دیتابیس SQLite
```

---

## ⚙️ تنظیمات محیطی

می‌توانید تنظیمات پروژه را از طریق فایل `.env` مدیریت کنید.

نمونه:

```env
SECRET_KEY=your-secret-key
SITE_URL=http://localhost:5000
DATABASE_URL=sqlite:///instance/database.db
```

> ⚠️ فایل `.env` را در GitHub قرار ندهید.

همچنین بهتر است فایل دیتابیس، فایل‌های آپلودی و سایر اطلاعات خصوصی را در `.gitignore` قرار دهید.

---

## 🔒 نکات امنیتی

قبل از استفاده در Production:

* 🔑 یک `SECRET_KEY` تصادفی و قدرتمند ایجاد کنید.
* 🐛 مقدار `debug` را روی `False` قرار دهید.
* 🔐 رمز عبور پیش‌فرض مدیر را تغییر دهید.
* 🚫 اطلاعات حساس را در Repository قرار ندهید.
* 🔒 کلیدهای API و Passwordها را داخل `.env` نگهداری کنید.
* 📁 دسترسی فایل‌های آپلودی را بررسی کنید.
* 🛡️ محدودیت نوع و حجم فایل‌های Upload را تنظیم کنید.
* 🌐 در Production از HTTPS استفاده کنید.

---

## 🌍 اجرای Production

برای اجرای پروژه در محیط Production می‌توانید از **Waitress** یا **Gunicorn** استفاده کنید.

### Windows

```bash
pip install waitress
```

سپس:

```bash
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

### Linux

```bash
pip install gunicorn
```

سپس:

```bash
gunicorn app:app
```

---

## 🗺️ مسیرهای اصلی

| مسیر                | توضیح          |
| ------------------- | -------------- |
| `/`                 | صفحه اصلی      |
| `/templates`        | لیست قالب‌ها   |
| `/templates/<slug>` | جزئیات قالب    |
| `/download/<slug>`  | دانلود قالب    |
| `/support`          | پشتیبانی       |
| `/about`            | درباره پروژه   |
| `/admin/login`      | ورود مدیر      |
| `/admin/dashboard`  | داشبورد مدیریت |
| `/sitemap.xml`      | نقشه سایت      |
| `/robots.txt`       | فایل Robots    |

---

## 🎨 قابل شخصی‌سازی

یکی از اهداف اصلی این پروژه، **Customizable بودن** آن است.

می‌توانید بخش‌های مختلف پروژه را مطابق نیاز خود تغییر دهید:

* 🎨 رنگ‌بندی
* 🖌️ UI/UX
* 🧩 کامپوننت‌ها
* 📄 صفحات
* 🗄️ دیتابیس
* 🔐 سیستم احراز هویت
* 📦 سیستم دانلود
* 🔎 SEO
* 🌐 زبان و RTL
* ⚙️ قابلیت‌های پنل مدیریت

---

## 🤝 مشارکت در پروژه

این پروژه Open Source است و از مشارکت توسعه‌دهندگان استقبال می‌شود.

برای مشارکت:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

یک Branch جدید ایجاد کنید:

```bash
git checkout -b feature/new-feature
```

تغییرات خود را اعمال کنید:

```bash
git add .
git commit -m "Add new feature"
```

سپس Branch را Push کرده و Pull Request ایجاد کنید.

---

## 💡 ایده‌های توسعه

برخی قابلیت‌هایی که می‌توانند در آینده به پروژه اضافه شوند:

* 🔍 جستجوی پیشرفته
* 🏷️ سیستم دسته‌بندی و Tag
* ⭐ امتیازدهی به قالب‌ها
* ❤️ علاقه‌مندی‌ها
* 👤 سیستم حساب کاربری
* 📈 آمار دقیق دانلود
* 🔔 سیستم اعلان
* 🌐 چندزبانه شدن
* 💳 سیستم پرداخت
* 📦 سیستم Versioning برای قالب‌ها
* 🔗 API
* 🐳 Docker
* ☁️ پشتیبانی بهتر از Storageهای ابری

---

## 📜 License

این پروژه به صورت **Open Source و رایگان** منتشر شده است.

شما می‌توانید پروژه را:

* استفاده کنید
* تغییر دهید
* شخصی‌سازی کنید
* توسعه دهید
* برای پروژه‌های خود استفاده کنید

لطفاً شرایط License موجود در Repository را نیز بررسی کنید.

---

## ⭐ حمایت از پروژه

اگر این پروژه برای شما مفید بود:

⭐ به Repository ستاره بدهید.

🍴 پروژه را Fork کنید.

🐛 مشکلات را در Issues گزارش دهید.

💡 برای قابلیت‌های جدید پیشنهاد ارائه دهید.

🤝 در توسعه پروژه مشارکت کنید.

---

<div align="center">

### 🧩 Built with Python & Flask

**Open Source • Free • Customizable • Persian RTL**

</div>
