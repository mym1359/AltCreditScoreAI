# نمونهٔ آموزشی امتیازدهی اعتباری جایگزین | Alternative credit scoring prototype

این پروژه روی دادهٔ نمونه، مراحل پاک‌سازی، ساخت ویژگی و مقایسهٔ رگرسیون لجستیک، XGBoost و LightGBM را نشان می‌دهد.

This prototype uses example data to demonstrate cleaning, feature engineering, and comparison of logistic regression, XGBoost, and LightGBM.

## اجزای قابل بررسی | Reviewable components

- [پردازش داده / Data preparation](src/preprocessing)
- [ساخت ویژگی / Feature engineering](src/feature_engineering)
- [آموزش و ارزیابی / Training and evaluation](src/models/train_model.py)
- [آزمون‌ها / Tests](tests)

آموزش و گزارش معیارها روی دادهٔ نمونه، تمرین فنی مقایسهٔ مدل است. این مخزن شواهد ارزیابی در سطح متقاضی، اثر بر دسترسی به اعتبار یا عملکرد در محیط عملیاتی را گزارش نمی‌کند.

Training and metrics on example data demonstrate a technical model comparison. This repository does not report applicant-level validation, effects on access to credit, or production performance.

[پژوهش بازپرداخت وام مسکن / Mortgage repayment research](https://github.com/mym1359/mortgage-repayment-review)
