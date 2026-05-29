#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    input_html = "resume.html"
    output_pdf = "Resume_Rakesh_Pandey_202605.pdf"

    if not os.path.exists(chrome_path):
        print(f"Error: Google Chrome was not found at '{chrome_path}'")
        sys.exit(1)

    if not os.path.exists(input_html):
        print(f"Error: Input HTML file '{input_html}' does not exist.")
        sys.exit(1)

    print(f"Compiling '{input_html}' to '{output_pdf}'...")
    
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf}",
        input_html
    ]

    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Success! PDF compiled successfully.")
        print(f"File size: {os.path.getsize(output_pdf)} bytes")
    except subprocess.CalledProcessError as e:
        print(f"Error compiling PDF: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    main()
