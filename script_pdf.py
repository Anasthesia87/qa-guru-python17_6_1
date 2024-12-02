import os.path

from pypdf import PdfReader

reader = PdfReader(r"tmp\Python Testing with Pytest (Brian Okken).pdf")

print(reader.pages)
print(len(reader.pages))

print(reader.pages[1].extract_text())

assert "Simple, Rapid, Effective, and Scalable" in reader.pages[1]
print(os.path.getsize(r"tmp\Python Testing with Pytest (Brian Okken).pdf"))
assert os.path.getsize(r"tmp\Python Testing with Pytest (Brian Okken).pdf") == 3035139
