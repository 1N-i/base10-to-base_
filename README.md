# 🔢 Base10 to Base-N Converter

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)

A lightweight Python utility designed to convert standard numbers (Base 10) into custom base representations ranging from Base 2 to Base 36.

## 📋 Summary
- [Technologies](#-technologies)
- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)

---

## 🛠 Technologies
- **Python 3.x**: Core logic, string slicing, and numerical operations.

## ✨ Features
- **Dynamic Base Conversion:** Easily convert base-10 integers to any target base between 2 and 36.
- **Alphanumeric Encoding:** Maps remainders above 9 to uppercase letters (`A-Z`) for standard representation (e.g., Hexadecimal, Base36).
- **Boundary Validation:** Returns an informative message if the provided base falls outside the allowed range (`2 <= base <= 36`).
- **Zero & Edge Case Handling:** Gracefully handles base cases such as converting `0`.

## 📂 Project Architecture
The project consists of a concise and modular script:
* `base_converter.py`: Contains the `Base10ToBase_` function logic and execution sample.

## 📚 What I Learned
* **Positional Notation Algorithm:** Using modulo (`%`) to compute positional remainders and floor division (`//`) to iteratively break down decimal values.
* **String Inversion:** Utilizing Python's extended slicing (`[::-1]`) to reverse collected remainders into the correct order.
* **Character Mapping:** Using a lookup string (`chars`) to efficiently convert numeric indices directly into alphanumeric representations.

## 🔮 Future Improvements
- [ ] Add support for negative numbers.
- [ ] Implement reverse conversion (Base-N to Base 10).
- [ ] Add support for floating-point / fractional conversions.
- [ ] Create an interactive CLI interface for custom user prompts.
