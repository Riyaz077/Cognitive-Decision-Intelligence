# GitHub upload guide

1. Sign in at https://github.com and click **New repository**.
2. Repository name: `Cognitive-Decision-Intelligence`.
3. Description: `Multi-domain AI predictive analytics framework for retail forecasting, customer sentiment analysis, and business decision support.`
4. Choose **Public** for a portfolio repository (unless you have a reason to keep it private).
5. Do not initialize with a README if you are uploading this prepared folder, because it already contains one.
6. Extract this ZIP, open a terminal in the extracted folder, then run:

```bash
git init
git add .
git commit -m "Initial commit: Cognitive Decision Intelligence Framework"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Cognitive-Decision-Intelligence.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If Git asks you to authenticate, complete the browser sign-in flow or use GitHub's supported credential manager.

## Before publishing
- Replace profile placeholders and add your LinkedIn URL.
- Run the code and tests locally.
- Add only datasets you are legally allowed to redistribute; default `.gitignore` excludes CSV data.
- Capture actual dashboard screenshots and place them in `screenshots/`.
- Add your real evaluation results; do not invent metrics.
- Verify all claims in README and presentation match the code you actually ran.
