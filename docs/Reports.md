---
title: Reports
layout: page
nav_order: 6
---

MSML has a variety of reports that can be produced in markdown files which can also be converted to PDF.

## PDF Conversion

- To use PDF conversion, a few other things need to be installed
- One must install pandoc, which can be done with "brew install pandoc" on a mac
- Installing pdflatex might be required which can be done with "brew install --cask basictex" on a mac
- If the pdflatex path is not recognized by the system, you may need to pass the path to it. For example, on a mac this would be: pdflatex_path='/Library/TeX/texbin/pdflatex'