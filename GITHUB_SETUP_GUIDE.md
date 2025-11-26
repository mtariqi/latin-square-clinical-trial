# Complete GitHub & Zenodo Setup Guide

This guide will take you from zero to a fully professional, publication-ready GitHub repository with Zenodo DOI integration.

## 📋 Prerequisites

- [ ] GitHub account ([Sign up here](https://github.com/join))
- [ ] Zenodo account ([Sign up here](https://zenodo.org/signup/))
- [ ] ORCID iD (optional but recommended) ([Get one here](https://orcid.org/register))
- [ ] Git installed on your computer
- [ ] Python 3.7+ installed

---

## Part 1: Local Repository Setup (30 minutes)

### Step 1: Create Project Structure

```bash
# Create main directory
mkdir latin-square-clinical-trial
cd latin-square-clinical-trial

# Create all subdirectories
mkdir -p examples data docs tests notebooks .github/workflows figures

# Initialize git
git init

# Create empty __init__.py
touch __init__.py
```

### Step 2: Create All Core Files

Copy these files from the artifacts provided:

**Root Directory Files:**
1. `latin_square_analyzer.py` - Main analyzer
2. `analyze_real_clinical_data.py` - Real data analyzer
3. `README.md` - Main documentation
4. `LICENSE` - MIT License
5. `CONTRIBUTING.md` - Contribution guidelines
6. `CITATION.cff` - Citation metadata
7. `.zenodo.json` - Zenodo metadata
8. `QUICKSTART.md` - Quick start guide
9. `DATA_SOURCES.md` - Data acquisition guide
10. `requirements.txt` - Dependencies
11. `requirements-dev.txt` - Dev dependencies
12. `setup.py` - Package setup
13. `MANIFEST.in` - Package manifest
14. `.gitignore` - Git ignore file

**Create .gitignore:**
```bash
cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/
*.egg-info/
.coverage
htmlcov/
.pytest_cache/
*.ipynb_checkpoints/
.DS_Store
*.swp
*.csv
!data/sample_*.csv
*.png
!figures/*.png
EOF
```

**examples/ Directory:**
- `example_pain_study.py` (from artifact)

**tests/ Directory:**
- `__init__.py` (empty file)
- `test_design.py` (from artifact)

**docs/ Directory:**
- `methodology.md` (from artifact)
- `api_reference.md` (create basic structure)

**.github/workflows/ Directory:**
- `tests.yml` (from artifact)

**data/ Directory:**
- Create `sample_data.csv` with example data:

```bash
cat > data/sample_data.csv << 'EOF'
Subject,Period,Treatment,Response
P1,1,Drug_A,65
P1,2,Drug_B,72
P1,3,Drug_C,68
P1,4,Placebo,52
P2,1,Drug_B,70
P2,2,Drug_C,75
P2,3,Placebo,48
P2,4,Drug_A,63
P3,1,Drug_C,77
P3,2,Placebo,50
P3,3,Drug_A,67
P3,4,Drug_B,74
P4,1,Placebo,45
P4,2,Drug_A,60
P4,3,Drug_B,69
P4,4,Drug_C,71
EOF
```

### Step 3: Customize Your Information

**Replace these placeholders in ALL files:**

1. **In README.md, CITATION.cff, .zenodo.json, setup.py:**
   - Replace `Your Name` with your actual name
   - Replace `your.email@example.com` with your email
   - Replace `yourusername` with your GitHub username
   - Replace `Your Institution` with your affiliation

2. **In CITATION.cff:**
   - Replace `0000-0000-0000-0000` with your ORCID iD (or remove if you don't have one)

3. **Update version date** in CITATION.cff to today's date

### Step 4: Test Locally

```bash
# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run the main analyzer
python latin_square_analyzer.py

# Run tests
pytest tests/ -v

# Check code style
flake8 *.py --max-line-length=100
black *.py --check
```

### Step 5: Initial Git Commit

```bash
# Add all files
git add .

# Make initial commit
git commit -m "Initial commit: Latin Square Clinical Trial Analyzer v1.0.0"
```

---

## Part 2: GitHub Repository Setup (15 minutes)

### Step 6: Create GitHub Repository

1. **Go to GitHub**: https://github.com/new

2. **Fill in repository details:**
   - **Repository name**: `latin-square-clinical-trial`
   - **Description**: 
     ```
     A comprehensive Python toolkit for designing, simulating, and analyzing 
     crossover clinical trials using Latin Square experimental designs
     ```
   - **Visibility**: ✅ Public (required for Zenodo)
   - **DO NOT** initialize with README (you already have one)
   - **DO NOT** add .gitignore (you already have one)
   - **DO NOT** choose a license (you already have one)

3. **Click "Create repository"**

### Step 7: Push to GitHub

```bash
# Add remote (replace yourusername with your GitHub username)
git remote add origin https://github.com/yourusername/latin-square-clinical-trial.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 8: Configure Repository Settings

1. **Go to your repository on GitHub**

2. **Settings → General:**
   - ✅ Enable "Issues"
   - ✅ Enable "Wiki" (optional)
   - ✅ Enable "Discussions" (optional)

3. **Settings → Features:**
   - ✅ Wikis
   - ✅ Issues
   - ✅ Preserve this repository (optional, for important projects)

4. **Add Repository Topics** (click gear icon next to "About"):
   - `latin-square`
   - `clinical-trials`
   - `crossover-design`
   - `biostatistics`
   - `experimental-design`
   - `health-science`
   - `python`
   - `data-analysis`
   - `anova`
   - `statistical-analysis`

5. **Add Website and Description** in "About" section:
   - Description: "Python toolkit for Latin Square crossover clinical trials"
   - Website: (leave blank for now)

### Step 9: Create GitHub Release (v1.0.0)

1. **Click "Releases"** on right sidebar

2. **Click "Create a new release"**

3. **Fill in release details:**
   - **Tag version**: `v1.0.0`
   - **Target**: `main`
   - **Release title**: `Latin Square Analyzer v1.0.0`
   - **Description**:
     ```markdown
     ## 🎉 Initial Release
     
     First stable release of the Latin Square Clinical Trial Analyzer.
     
     ### Features
     - ✅ Latin Square design generation
     - ✅ Data simulation with customizable parameters
     - ✅ Statistical analysis (ANOVA, paired t-tests)
     - ✅ Publication-ready visualizations
     - ✅ Real data analysis tools
     - ✅ Comprehensive documentation
     
     ### Installation
     ```bash
     pip install -r requirements.txt
     ```
     
     ### Quick Start
     ```python
     from latin_square_analyzer import LatinSquareDesign
     trial = LatinSquareDesign(['A', 'B', 'C', 'D'])
     ```
     
     See [README.md](README.md) for full documentation.
     ```

4. **Click "Publish release"**

---

## Part 3: Zenodo Integration (20 minutes)

### Step 10: Connect GitHub to Zenodo

1. **Log in to Zenodo**: https://zenodo.org/

2. **Click on your name** (top right) → **GitHub**

3. **Click "Connect"** if not already connected

4. **Authorize Zenodo** to access your GitHub repositories

5. **Find your repository** in the list:
   - Search for "latin-square-clinical-trial"
   - Click the **toggle button** to **ON** (green)

   ![Toggle ON](https://i.imgur.com/example.png)

6. **Webhook is now active** - Zenodo will archive all future releases

### Step 11: Create Zenodo Archive

**Option A: Trigger from new release (Recommended)**

1. **Go back to GitHub**

2. **Create a new release** (or edit v1.0.0):
   - Tag: `v1.0.0`
   - This will automatically trigger Zenodo

3. **Wait 5-10 minutes** for Zenodo to process

4. **Check Zenodo**:
   - Go to https://zenodo.org/
   - Click "Upload" → "My uploads"
   - Your repository should appear!

**Option B: Manual upload (if automatic didn't work)**

1. **Download your repository as ZIP from GitHub**

2. **Go to Zenodo**: https://zenodo.org/deposit/new

3. **Upload the ZIP file**

4. **Fill in metadata** (should auto-populate from .zenodo.json):
   - Title: Latin Square Clinical Trial Analyzer
   - Authors: Your name
   - Description: (from .zenodo.json)
   - Keywords: (from .zenodo.json)
   - License: MIT

5. **Click "Publish"**

### Step 12: Get Your DOI

1. **On Zenodo**, after publishing:
   - You'll see your DOI: `10.5281/zenodo.XXXXXXX`
   - Copy this DOI

2. **Update README.md badge**:
   ```markdown
   [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
   ```

3. **Update CITATION.cff**:
   ```yaml
   doi: 10.5281/zenodo.XXXXXXX
   ```

4. **Commit and push**:
   ```bash
   git add README.md CITATION.cff
   git commit -m "Add Zenodo DOI"
   git push
   ```

---

## Part 4: Professional Polish (30 minutes)

### Step 13: Add Badges

Update your README.md with these badges (replace placeholders):

```markdown
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/latin-square-clinical-trial?style=social)](https://github.com/yourusername/latin-square-clinical-trial/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/latin-square-clinical-trial?style=social)](https://github.com/yourusername/latin-square-clinical-trial/network/members)
[![Tests](https://github.com/yourusername/latin-square-clinical-trial/workflows/Tests/badge.svg)](https://github.com/yourusername/latin-square-clinical-trial/actions)
[![codecov](https://codecov.io/gh/yourusername/latin-square-clinical-trial/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/latin-square-clinical-trial)
```

### Step 14: Create Project Banner

**Option 1: Use Canva (Free)**
1. Go to https://www.canva.com/
2. Create 1200x400px banner
3. Add text: "Latin Square Clinical Trial Analyzer"
4. Add relevant medical/statistical graphics
5. Download as PNG
6. Save as `figures/banner.png`

**Option 2: Simple text banner**
```bash
# Use ImageMagick (install first)
convert -size 1200x400 xc:white \
  -gravity center \
  -pointsize 60 \
  -annotate +0+0 "Latin Square Clinical Trial Analyzer" \
  figures/banner.png
```

### Step 15: Set Up GitHub Actions

The workflow file is already created. To enable:

1. **Go to repository → Actions tab**
2. **Enable workflows** if prompted
3. **Make a commit** to trigger first run
4. **Verify tests pass**

### Step 16: Add Code Coverage (Optional)

1. **Sign up for Codecov**: https://codecov.io/

2. **Connect your GitHub repository**

3. **Add Codecov token** to GitHub Secrets:
   - Settings → Secrets → New repository secret
   - Name: `CODECOV_TOKEN`
   - Value: (from Codecov)

### Step 17: Create Project Website (Optional)

**Using GitHub Pages:**

1. **Settings → Pages**

2. **Source**: Deploy from branch

3. **Branch**: `main`, folder: `/docs` or `/root`

4. **Create docs/index.md**:
   ```markdown
   # Latin Square Clinical Trial Analyzer
   
   [View on GitHub](https://github.com/yourusername/latin-square-clinical-trial)
   
   [Download Latest Release](https://github.com/yourusername/latin-square-clinical-trial/releases/latest)
   ```

5. **Update website URL** in repository About section

### Step 18: Social Media Preview

1. **Settings → General → Social Preview**

2. **Upload an image** (1280x640px recommended)
   - Use your banner or a relevant graphic

3. **This appears** when sharing on Twitter, LinkedIn, etc.

---

## Part 5: Maintenance & Updates

### Making Updates

```bash
# Make changes to code
# ...

# Test locally
pytest tests/
flake8 *.py

# Commit and push
git add .
git commit -m "feat: add new feature"
git push

# Create new release for major updates
# Go to GitHub → Releases → Create new release
# Tag: v1.1.0
# This automatically updates Zenodo!
```

### Version Numbering

Follow [Semantic Versioning](https://semver.org/):
- `v1.0.0` - Initial release
- `v1.0.1` - Bug fixes
- `v1.1.0` - New features (backwards compatible)
- `v2.0.0` - Breaking changes

---

## ✅ Final Checklist

### Local Setup
- [ ] All files created and in correct locations
- [ ] Personal information updated (name, email, GitHub username)
- [ ] Tests run successfully locally
- [ ] Code passes linting (flake8, black)

### GitHub Repository
- [ ] Repository created and pushed
- [ ] README displays correctly
- [ ] Topics/tags added
- [ ] v1.0.0 release created
- [ ] Issues enabled
- [ ] GitHub Actions running

### Zenodo Integration
- [ ] Zenodo connected to GitHub
- [ ] Repository toggle enabled on Zenodo
- [ ] DOI obtained
- [ ] DOI added to README and CITATION.cff
- [ ] .zenodo.json metadata correct

### Professional Elements
- [ ] All badges added to README
- [ ] Banner image added
- [ ] LICENSE file present
- [ ] CONTRIBUTING.md present
- [ ] CITATION.cff present
- [ ] Documentation complete

### Testing & Quality
- [ ] Tests pass on GitHub Actions
- [ ] Code coverage tracked (optional)
- [ ] No broken links in documentation
- [ ] Example code runs without errors

---

## 🎉 You're Done!

Your repository is now:
- ✅ Professionally structured
- ✅ Fully documented
- ✅ Citable with DOI
- ✅ Archived on Zenodo
- ✅ Ready for collaboration
- ✅ Portfolio-ready

### Next Steps

1. **Share your work:**
   - Tweet about it
   - Post on LinkedIn
   - Share in relevant communities

2. **Get feedback:**
   - Ask colleagues to review
   - Share in biostatistics forums
   - Present at lab meetings

3. **Maintain regularly:**
   - Respond to issues
   - Update documentation
   - Add new features

4. **Cite in your work:**
   - Use the DOI in your papers
   - Include in your CV
   - Reference in presentations

---

## 📚 Additional Resources

- [GitHub Docs](https://docs.github.com/)
- [Zenodo Help](https://help.zenodo.org/)
- [Semantic Versioning](https://semver.org/)
- [Choose a License](https://choosealicense.com/)
- [Writing Good Commit Messages](https://chris.beams.io/posts/git-commit/)

## 🆘 Troubleshooting

### Zenodo not archiving?
- Check webhook is active (green toggle)
- Verify repository is public
- Try creating a new release
- Wait 10-15 minutes

### GitHub Actions failing?
- Check Python version compatibility
- Verify all dependencies in requirements.txt
- Check for syntax errors

### DOI badge not showing?
- Make sure you're using the correct DOI
- Badge URL format: `https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg`

---

**Congratulations! You now have a professional, publication-ready GitHub repository! 🎊**
