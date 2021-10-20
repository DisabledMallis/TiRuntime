#!/bin/bash

# Generate antlr
java -jar antlr4.jar -Dlanguage=Python3 "src/antlr/TiBasic.g4"

# Run python
python src/main.py