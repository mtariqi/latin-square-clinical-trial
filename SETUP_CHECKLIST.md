# Master Setup Checklist

Print this and check off each item as you complete it!

## 📦 Phase 1: File Preparation (30-45 minutes)

### Core Python Files
- [ ] `latin_square_analyzer.py` - Main analyzer module
- [ ] `analyze_real_clinical_data.py` - Real data analyzer
- [ ] `__init__.py` - Package initialization file

### Documentation Files
- [ ] `README.md` - Main project documentation with badges
- [ ] `QUICKSTART.md` - Quick start guide
- [ ] `DATA_SOURCES.md` - Data acquisition guide
- [ ] `CONTRIBUTING.md` - Contribution guidelines
- [ ] `LICENSE` - MIT License file
- [ ] `CITATION.cff` - Citation metadata
- [ ] `.zenodo.json` - Zenodo metadata

### Configuration Files
- [ ] `requirements.txt` - Main dependencies
- [ ] `requirements-dev.txt` - Development dependencies
- [ ] `setup.py` - Package setup configuration
- [ ] `MANIFEST.in` - Package manifest
- [ ] `.gitignore` - Git ignore rules

### Examples Directory (`examples/`)
- [ ] `example_pain_study.py` - Pain medication study example
- [ ] Create subdirectory if needed

### Tests Directory (`tests/`)
- [ ] `__init__.py` - Empty file
- [ ] `test_design.py` - Unit tests
- [ ] `test_analysis.py` - Analysis tests (optional)

### Docs Directory (`docs/`)
- [ ] `methodology.md` - Detailed methodology
- [ ] `api_reference.md` - API documentation (basic structure)

### Data Directory (`data/`)
- [ ] `sample_data.csv` - Example dataset
- [ ] README explaining data format (optional)

### GitHub Workflows (`.github/workflows/`)
- [ ] `tests.yml` - GitHub Actions workflow

### Figures Directory (`figures/`)
- [ ] `banner.png` - Repository banner (1200x400px)
- [ ] Create placeholder if needed

---

## ✏️ Phase 2: Personalization (15-20 minutes)

### Update Personal Information in ALL Files

**Your Name:**
- [ ] README.md (multiple locations)
- [ ] CITATION.cff (author field)
- [ ] .zenodo.json (creators field)
- [ ] setup.py (author field)
- [ ] CONTRIBUTING.md (contact info)
- [ ] LICENSE (copyright holder)

**Your Email:**
- [ ] README.md (contact section)
- [ ] CITATION.cff
- [ ] .zenodo.json
- [ ] setup.py
- [ ] CONTRIBUTING.md

**Your GitHub Username:**
- [ ] README.md (all URLs with `yourusername`)
- [ ] CITATION.cff (repository-code URL)
- [ ] .zenodo.json (related_identifiers)
- [ ] setup.py (all URLs)
- [ ] CONTRIBUTING.md (project links)

**Your Institution/Affiliation:**
- [ ] CITATION.cff (affiliation field)
- [ ] .zenodo.json (affiliation field)

**Your ORCID (if you have one):**
- [ ] CITATION.cff (orcid field)
- [ ] .zenodo.json (orcid field)
- [ ] If no ORCID, remove these fields

**Version Date:**
- [ ] CITATION.cff (update to today's date)

---

## 🧪 Phase 3: Local Testing (15 minutes)

### Environment Setup
- [ ] Python 3.7+ installed
- [ ] Virtual environment created
  ```bash
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate
  ```

### Install Dependencies
- [ ] Main dependencies installed
  ```bash
  pip install -r requirements.txt
  ```
- [ ] Dev dependencies installed
  ```bash
  pip install -r requirements-dev.txt
  ```

### Run Tests
- [ ] Main analyzer runs
  ```bash
  python latin_square_analyzer.py
  ```
- [ ] Example runs
  ```bash
  python examples/example_pain_study.py
  ```
- [ ] Unit tests pass
  ```bash
  pytest tests/ -v
  ```
- [ ] Code style check
  ```bash
  flake8 *.py --max-line-length=100
  ```
- [ ] Format check
  ```bash
  black *.py --check
  ```

### Verify Outputs
- [ ] Output files created in correct location
- [ ] Figures generated properly
- [ ] No error messages in console

---

## 🔧 Phase 4: Git Setup (10 minutes)

### Initialize Repository
- [ ] Git installed
- [ ] Repository initialized
  ```bash
  git init
  ```
- [ ] `.gitignore` created
- [ ] All files added
  ```bash
  git add .
  ```
- [ ] Initial commit made
  ```bash
  git commit -m "Initial commit: Latin Square Clinical Trial Analyzer v1.0.0"
  ```

### Verify Git Status
- [ ] No uncommitted changes
  ```bash
  git status
  ```
- [ ] Branch named `main`
  ```bash
  git branch -M main
  ```

---

## 🌐 Phase 5: GitHub Repository (20 minutes)

### Create Repository
- [ ] Logged in to GitHub
- [ ] New repository created at https://github.com/new
- [ ] Repository name: `latin-square-clinical-trial`
- [ ] Description added
- [ ] Set to **Public** (required for Zenodo)
- [ ] **NO** README initialization
- [ ] **NO** .gitignore addition
- [ ] **NO** license selection

### Push to GitHub
- [ ] Remote added
  ```bash
  git remote add origin https://github.com/YOURUSERNAME/latin-square-clinical-trial.git
  ```
- [ ] Pushed to GitHub
  ```bash
  git push -u origin main
  ```
- [ ] Verified repository displays correctly

### Repository Settings
- [ ] Issues enabled (Settings → General)
- [ ] Wiki enabled (optional)
- [ ] Discussions enabled (optional)
- [ ] Topics added (at least 5):
  - [ ] `latin-square`
  - [ ] `clinical-trials`
  - [ ] `crossover-design`
  - [ ] `biostatistics`
  - [ ] `python`
  - [ ] Additional relevant topics

### About Section
- [ ] Description added
- [ ] Website URL added (if applicable)
- [ ] Topics visible

---

## 🚀 Phase 6: First Release (10 minutes)

### Create v1.0.0 Release
- [ ] Click "Releases" → "Create a new release"
- [ ] Tag version: `v1.0.0`
- [ ] Target: `main`
- [ ] Release title: `Latin Square Analyzer v1.0.0`
- [ ] Description added (feature list, installation, quick start)
- [ ] **Published** (not draft)

### Verify Release
- [ ] Release appears in Releases section
- [ ] Tag created: `v1.0.0`
- [ ] Source code zip/tar.gz available
- [ ] Release description renders correctly

---

## 📚 Phase 7: Zenodo Integration (25 minutes)

### Zenodo Account
- [ ] Zenodo account created at https://zenodo.org/signup/
- [ ] Email verified
- [ ] Logged in

### GitHub Integration
- [ ] Zenodo connected to GitHub (Zenodo → Settings → GitHub)
- [ ] Authorization granted
- [ ] Repository list loaded

### Enable Archiving
- [ ] Found `latin-square-clinical-trial` in repository list
- [ ] Toggled switch to **ON** (green)
- [ ] Webhook confirmed active

### Trigger Archive
**Option A: From New Release (Recommended)**
- [ ] Created new GitHub release (or re-released v1.0.0)
- [ ] Waited 10-15 minutes
- [ ] Checked Zenodo uploads

**Option B: Manual Upload (if automatic failed)**
- [ ] Downloaded repository ZIP from GitHub
- [ ] Uploaded to Zenodo manually
- [ ] Filled in metadata
- [ ] Published

### Obtain DOI
- [ ] DOI received: `10.5281/zenodo.XXXXXXX`
- [ ] DOI copied to clipboard

### Update Files with DOI
- [ ] README.md badge updated with actual DOI
  ```markdown
  [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
  ```
- [ ] CITATION.cff updated with DOI
  ```yaml
  doi: 10.5281/zenodo.XXXXXXX
  ```
- [ ] Committed and pushed changes
  ```bash
  git add README.md CITATION.cff
  git commit -m "docs: add Zenodo DOI"
  git push
  ```

---

## 🎨 Phase 8: Professional Polish (30 minutes)

### Badges
- [ ] All badges added to README.md
- [ ] Python version badge
- [ ] License badge
- [ ] DOI badge (with actual DOI)
- [ ] GitHub stars badge
- [ ] Tests/Actions badge
- [ ] Code coverage badge (optional)
- [ ] Badges render correctly (check on GitHub)

### Banner Image
- [ ] Banner created (1200x400px)
- [ ] Saved as `figures/banner.png`
- [ ] Added to repository
- [ ] Referenced in README.md
- [ ] Displays correctly

### GitHub Actions
- [ ] Workflow file present (`.github/workflows/tests.yml`)
- [ ] Actions tab enabled
- [ ] First workflow run triggered
- [ ] Tests passing (green checkmark)

### Social Preview
- [ ] Image uploaded (Settings → General → Social Preview)
- [ ] Image dimensions correct (1280x640px recommended)
- [ ] Preview looks good

### Optional Enhancements
- [ ] Codecov account created and connected
- [ ] GitHub Pages enabled (optional)
- [ ] Project website created (optional)
- [ ] Wiki started (optional)

---

## 📝 Phase 9: Documentation Review (20 minutes)

### README.md
- [ ] All sections complete
- [ ] No broken links
- [ ] Code examples work
- [ ] Installation instructions clear
- [ ] Quick start is actually quick
- [ ] Contact information correct
- [ ] License mentioned

### CITATION.cff
- [ ] All fields filled correctly
- [ ] Date is current
- [ ] DOI included
- [ ] ORCID correct (if included)

### CONTRIBUTING.md
- [ ] Guidelines clear
- [ ] Examples provided
- [ ] Contact info correct

### Other Documentation
- [ ] QUICKSTART.md complete
- [ ] DATA_SOURCES.md helpful
- [ ] docs/methodology.md informative

---

## ✅ Phase 10: Final Verification (15 minutes)

### Repository Checklist
- [ ] README displays correctly on GitHub
- [ ] All badges work (click each one)
- [ ] License is visible
- [ ] Topics show up
- [ ] Release is accessible
- [ ] Issues work
- [ ] Actions run successfully

### Zenodo Checklist
- [ ] Archive appears on Zenodo
- [ ] DOI resolves correctly (click DOI badge)
- [ ] Metadata correct on Zenodo page
- [ ] All authors listed
- [ ] Keywords appropriate
- [ ] License shown

### Functionality Checklist
- [ ] Clone repository fresh
  ```bash
  git clone https://github.com/YOURUSERNAME/latin-square-clinical-trial.git
  cd latin-square-clinical-trial
  ```
- [ ] Install dependencies
  ```bash
  pip install -r requirements.txt
  ```
- [ ] Run main script
  ```bash
  python latin_square_analyzer.py
  ```
- [ ] Verify outputs created
- [ ] Run example
  ```bash
  python examples/example_pain_study.py
  ```
- [ ] Run tests
  ```bash
  pytest tests/
  ```
- [ ] All work without errors

### Professional Appearance
- [ ] Repository looks polished
- [ ] No TODOs or FIXMEs in visible code
- [ ] No "test" commits in history
- [ ] No broken links
- [ ] No placeholder text remaining
- [ ] Banner image displays
- [ ] Badges aligned nicely

---

## 🎊 Phase 11: Publication & Sharing (10 minutes)

### Share Your Work
- [ ] Star your own repository (optional but fun!)
- [ ] Tweet about it (if you use Twitter)
- [ ] Post on LinkedIn (if you use LinkedIn)
- [ ] Share in relevant communities:
  - [ ] Reddit: r/bioinformatics, r/statistics
  - [ ] Discord/Slack biostatistics groups
  - [ ] University mailing lists

### Add to Your Portfolio
- [ ] Add to CV/Resume
- [ ] Add to personal website
- [ ] Include in GitHub profile README
- [ ] Mention in cover letters

### Citation
- [ ] Copy citation text from CITATION.cff
- [ ] Save for future use
- [ ] Share with collaborators

---

## 📊 Completion Summary

**Total Time Estimate:** 3-4 hours

**Files Created:** ~25 files
**Documentation Pages:** ~8 documents
**Code Modules:** 3 main Python files
**Tests:** Unit test suite
**Integrations:** GitHub + Zenodo + GitHub Actions

---

## 🆘 Troubleshooting Contacts

If you get stuck:
1. Check GITHUB_SETUP_GUIDE.md troubleshooting section
2. Search GitHub Docs: https://docs.github.com/
3. Check Zenodo Help: https://help.zenodo.org/
4. Ask in GitHub Discussions (if enabled)

---

## 🎉 Congratulations!

When all boxes are checked, you have:
- ✅ A professional GitHub repository
- ✅ A citable DOI from Zenodo
- ✅ Complete documentation
- ✅ Automated testing
- ✅ A portfolio-ready project
- ✅ A foundation for future research

**You did it! 🎊🎉🎈**

---

## 📅 Maintenance Schedule

### Weekly
- [ ] Check for new issues
- [ ] Review pull requests (if any)
- [ ] Monitor GitHub Actions

### Monthly
- [ ] Update dependencies if needed
- [ ] Review and improve documentation
- [ ] Add new examples if inspired

### Quarterly
- [ ] Consider new features
- [ ] Update methodology docs
- [ ] Create new release if substantial changes

---

**Keep this checklist for reference and future projects!**
