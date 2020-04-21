#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# filename: transcriber.py
# author: Glenn Abastillas
# created: 2020-04-16
# description: This script contains code to transcribe text from PDFs
from pytesseract import image_to_string
from PyPDF2 import PdfFileReader

