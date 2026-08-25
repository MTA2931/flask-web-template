# بی-فرانت (Bi-Front)

وبسایت فارسی دانلود قالب‌های آماده HTML / CSS / JavaScript با پنل مدیریت Flask.

## ویژگی‌ها

- **صفحات عمومی:** صفحه اصلی، قالب‌ها، پشتیبانی (تیکت + تماس)، درباره ما
- **پنل مدیریت:** لاگین، داشبورد، مدیریت قالب‌ها، دانلودها، ادمین‌ها
- **SEO:** متا تگ‌ها، Open Graph، Twitter Card، sitemap.xml، robots.txt، JSON-LD
- **UI/UX:** طراحی RTL فارسی، انیمیشن، هاور، ریسپانسیو

## پیش‌نیازها

- Python 3.10+
- pip

## نصب و اجرا (قدم به قدم)

### ۱. رفتن به پوشه پروژه

```powershell
cd C:\Users\Mani\Projects\bi-front
```

### ۲. ساخت محیط مجازی

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### ۳. نصب وابستگی‌ها

```powershell
pip install -r requirements.txt
```

### ۴. اجرای سرور

```powershell
python app.py
```

### ۵. باز کردن در مرورگر

- **سایت:** http://localhost:5000
- **پنل مدیریت:** http://localhost:5000/admin/login

### ۶. ورود به پنل (پیش‌فرض)

| فیلد | مقدار |
|------|-------|
| نام کاربری | `admin` |
| رمز عبور | `admin123` |

> **مهم:** بعد از اولین ورود، رمز عبور را تغییر دهید.

## افزودن قالب

1. وارد پنل مدیریت شوید
2. منوی **قالب‌ها** → **افزودن قالب**
3. نام، توضیحات، تصویر پیش‌نمایش (PNG/JPG) و فایل ZIP را آپلود کنید
4. فیلدهای SEO (Meta Title, Description, Keywords) را پر کنید
5. ذخیره — قالب در صفحه `/templates` نمایش داده می‌شود

## ساختار پروژه

```
bi-front/
├── app.py              # نقطه ورود Flask
├── config.py           # تنظیمات
├── requirements.txt
├── models/
│   └── database.py     # مدل‌های دیتابیس
├── routes/
│   ├── public.py       # مسیرهای عمومی
│   └── admin.py        # مسیرهای پنل
├── templates/          # قالب‌های HTML
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/        # فایل‌های آپلود شده
└── instance/           # دیتابیس SQLite
```

## تنظیمات محیط (اختیاری)

فایل `.env` در ریشه پروژه:

```
env
SECRET_KEY=your-secret-key-here
SITE_URL=https://yourdomain.com
DATABASE_URL=sqlite:///instance/bifront.db
```

## استقرار (Production)

1. `SECRET_KEY` قوی تنظیم کنید
2. `debug=False` در `app.py`
3. از Gunicorn یا waitress استفاده کنید:

```powershell
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

## صفحات سایت

| URL | توضیح |
|-----|-------|
| `/` | صفحه اصلی |
| `/templates` | لیست قالب‌ها |
| `/templates/<slug>` | جزئیات قالب |
| `/download/<slug>` | دانلود ZIP |
| `/support` | پشتیبانی و تیکت |
| `/about` | درباره ما |
| `/admin/login` | ورود پنل |
| `/admin/dashboard` | داشبورد |
| `/sitemap.xml` | نقشه سایت |
| `/robots.txt` | ربات‌ها |

## لایسنس

MTA Company ©
B-Front 2026 © 
