# Contributing to Latin Square Clinical Trial Analyzer

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)

## 🤝 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

### Expected Behavior

- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- Basic understanding of Latin Square designs (optional but helpful)

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/YOUR_USERNAME/latin-square-clinical-trial.git
cd latin-square-clinical-trial
```

3. Add upstream remote:

```bash
git remote add upstream https://github.com/ORIGINAL_OWNER/latin-square-clinical-trial.git
```

## 💡 How to Contribute

### Types of Contributions

We welcome many types of contributions:

1. **🐛 Bug Reports**
   - Report bugs using GitHub Issues
   - Include detailed steps to reproduce
   - Specify your environment (OS, Python version)

2. **✨ Feature Requests**
   - Suggest new features via GitHub Issues
   - Explain the use case and benefits
   - Consider submitting a PR if you can implement it

3. **📝 Documentation**
   - Fix typos or clarify existing docs
   - Add examples or tutorials
   - Improve README or guides

4. **🔧 Code Contributions**
   - Bug fixes
   - New features
   - Performance improvements
   - Test coverage improvements

5. **🎨 Design Improvements**
   - Visualization enhancements
   - UI/UX improvements
   - Figure quality improvements

## 🛠️ Development Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
# Install main dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt
```

### 3. Install Pre-commit Hooks

```bash
pip install pre-commit
pre-commit install
```

## 📏 Coding Standards

### Style Guide

We follow PEP 8 with some modifications:

- **Line length**: Maximum 100 characters
- **Imports**: Group and sort (stdlib, third-party, local)
- **Docstrings**: Google style
- **Type hints**: Encouraged for new code

### Code Formatting

We use `black` for code formatting:

```bash
black latin_square_analyzer.py
```

### Linting

We use `flake8` for linting:

```bash
flake8 latin_square_analyzer.py --max-line-length=100
```

### Example Function

```python
def analyze_treatment_effects(data: pd.DataFrame, 
                              alpha: float = 0.05) -> dict:
    """
    Analyze treatment effects using ANOVA.
    
    Args:
        data: DataFrame with columns ['Subject', 'Treatment', 'Response']
        alpha: Significance level for hypothesis testing (default: 0.05)
    
    Returns:
        Dictionary containing:
            - f_statistic: F-statistic from ANOVA
            - p_value: Corresponding p-value
            - significant: Boolean indicating significance
    
    Raises:
        ValueError: If data is missing required columns
    
    Example:
        >>> results = analyze_treatment_effects(trial_data)
        >>> print(f"P-value: {results['p_value']:.4f}")
    """
    # Implementation here
    pass
```

## 🧪 Testing Guidelines

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Run specific test file
pytest tests/test_design.py -v
```

### Writing Tests

- Place tests in `tests/` directory
- Name test files as `test_*.py`
- Name test functions as `test_*`
- Use descriptive test names
- Include docstrings for complex tests

**Example Test:**

```python
def test_latin_square_balance():
    """Test that generated design satisfies Latin Square properties."""
    trial = LatinSquareDesign(['A', 'B', 'C', 'D'])
    design = trial.generate_design()
    
    # Each treatment appears once per row
    for idx in design.index:
        assert len(set(design.loc[idx])) == 4
    
    # Each treatment appears once per column
    for col in design.columns:
        assert len(set(design[col])) == 4
```

### Test Coverage

- Aim for >80% code coverage
- Test both success and failure cases
- Include edge cases

## 📚 Documentation

### Docstring Format

Use Google-style docstrings:

```python
def function_name(param1: int, param2: str) -> bool:
    """
    Short description of function.
    
    Longer description if needed. Can span multiple lines.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When param1 is negative
        TypeError: When param2 is not a string
    
    Example:
        >>> result = function_name(5, "test")
        >>> print(result)
        True
    """
```

### README Updates

If adding a new feature:
1. Update the Features section
2. Add to Quick Start if appropriate
3. Create an example in `examples/`
4. Update documentation links

## 🔄 Pull Request Process

### Before Submitting

1. **Update your fork:**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes:**
   - Write code
   - Add tests
   - Update documentation

4. **Run tests:**
   ```bash
   pytest tests/ --cov=.
   flake8 *.py
   black *.py --check
   ```

5. **Commit changes:**
   ```bash
   git add .
   git commit -m "Add feature: brief description"
   ```

### Commit Message Format

Follow conventional commits:

```
<type>: <description>

[optional body]

[optional footer]
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

**Examples:**
```
feat: add support for 5x5 Latin squares

fix: correct ANOVA calculation for unbalanced designs

docs: update installation instructions in README
```

### Submitting Pull Request

1. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open Pull Request on GitHub**

3. **Fill out PR template:**
   - Describe changes
   - Link related issues
   - Add screenshots if applicable
   - Check all boxes in checklist

4. **Respond to feedback:**
   - Address reviewer comments
   - Update PR as needed
   - Be patient and respectful

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts
- [ ] Changes are focused and atomic

## 🐛 Reporting Bugs

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Run '....'
3. See error

**Expected behavior**
What you expected to happen.

**Actual behavior**
What actually happened.

**Screenshots**
If applicable, add screenshots.

**Environment:**
 - OS: [e.g., Ubuntu 20.04]
 - Python Version: [e.g., 3.8.5]
 - Package Version: [e.g., 1.0.0]

**Additional context**
Any other context about the problem.
```

## 💡 Feature Requests

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Alternative solutions or features you've considered.

**Additional context**
Any other context or screenshots.

**Would you like to implement this feature?**
Yes/No. If yes, we'll help guide you!
```

## 🎓 Resources

### Learning Resources

- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Git Tutorial](https://git-scm.com/docs/gittutorial)
- [Latin Square Designs](https://www.itl.nist.gov/div898/handbook/pri/section3/pri3341.htm)

### Project-Specific Resources

- [Methodology Documentation](docs/methodology.md)
- [API Reference](docs/api_reference.md)
- [Example Studies](examples/)

## 📞 Getting Help

If you need help:

1. Check existing [Issues](https://github.com/yourusername/latin-square-clinical-trial/issues)
2. Read the [Documentation](docs/)
3. Ask in [Discussions](https://github.com/yourusername/latin-square-clinical-trial/discussions)
4. Contact maintainers: your.email@example.com

## 🏆 Recognition

Contributors will be:
- Listed in [CONTRIBUTORS.md](CONTRIBUTORS.md)
- Mentioned in release notes
- Added to README acknowledgments

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎉

Every contribution, no matter how small, makes a difference!
