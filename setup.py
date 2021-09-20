from setuptools import setup, find_packages

with open("requirements.txt") as req:
  install_requires = req.read()

setup(
  name = "teste_python",
  version = "0.0.1",
  description = "API Villain",
  url = "https://github.com/lucasharzer/teste_python",
  author = "Lucas Harzer",
  author_email = "lucasmatos592@gmail.com",
  license = "BSD",
  packages = find_packages(),
  install_requires = [install_requires],
  zip_safe = False
)