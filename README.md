# 🔢 Base Converter

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)

A lightweight and bidirectional Python utility designed to convert standard numbers (Base 10) into custom base representations ranging from Base 2 to Base 36, as well as converting them back to Base 10.

## 📋 Summary
- [Technologies](#-technologies)
- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)

---

## 🛠 Technologies
- **Python 3.x**: Core logic, positional notation arithmetic, and string manipulation.

## ✨ Features
- **Bidirectional Base Conversion:** Seamlessly convert Base 10 integers to any target base (2 to 36) and parse custom base strings back into Base 10.
- **Alphanumeric Encoding & Decoding:** Maps digits above 9 to uppercase letters (`A-Z`) for standard representation (e.g., Binary, Hexadecimal, Base36).
- **Boundary Validation:** Validates input bases and returns informative messages if the provided base falls outside the allowed range (`2 <= base <= 36`).
- **Edge Case Handling:** Gracefully processes edge cases, such as converting `0`.

## 📂 Project Architecture
The project is split into two specialized scripts:
* `Base10ToBase_.py`: Handles conversion from decimal numbers (Base 10) to a specified target base (Base 2 to 36).
* `Base_ToBase10.py`: Handles conversion from a custom base string (Base 2 to 36) back into a decimal integer (Base 10).

## 📚 What I Learned
* **Positional Notation Algorithms:** Utilizing modulo (`%`) and floor division (`//`) for encoding to custom bases, and exponentiation with string indexing ($\sum \text{digit} \times \text{base}^i$) for decoding back to decimal.
* **String Reversal & Inversion:** Leveraging Python's extended slicing (`[::-1]`) to order remainders correctly and process strings from least to most significant digit.
* **Alphanumeric Lookup Mapping:** Mapping digits directly through index lookup strings (`chars.index()`) to seamlessly translate characters to numeric values.

## 🔮 Future Improvements
- [ ] Add support for direct Base-A to Base-B conversion (without intermediate Base 10 conversion).
- [ ] Add support for negative numbers.
- [ ] Support for floating-point / fractional conversions.
- [ ] Create an interactive CLI interface for custom user prompts.
