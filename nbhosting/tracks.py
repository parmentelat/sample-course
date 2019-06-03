"""
This module is for nbhosting
"""

from nbhosting.courses import (
    Track, Section, Notebook,
    notebooks_by_pattern, track_by_directory)

def tracks(coursedir):
    return [
        Track(coursedir,
              name="main",
              sections=[
                Section(name="bash",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"bash*.ipynb")),
                Section(name="python",
                        coursedir=coursedir,
                        notebooks=notebooks_by_pattern(coursedir,"python*.ipynb")),
                ],
              description="dual-language single track"),
        ]
