
## Features
- Modular design with preprocessing, feature engineering, and model training
- Explainable AI using SHAP and LIME
- CI/CD with GitHub Actions and Docker
- Bilingual documentation (English/Persian)
- Designed for global deployment and migration portfolio (NIW/NIV)

## Getting Started
```bash
git clone https://github.com/mym1359/AltCreditScoreAI.git
cd AltCreditScoreAI
pip install -r requirements.txtm
 

License
MIT


## 🧪 مرحله 3: ساخت محیط مجازی و نصب ابزارها

### ✅ دستورها:

```bash
# ساخت محیط مجازی
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate

# نصب ابزارهای پایه
pip install pandas numpy scikit-learn xgboost lightgbm matplotlib seaborn loguru pydantic pytest

# ذخیره در requirements.txt
pip freeze > requirements.txt