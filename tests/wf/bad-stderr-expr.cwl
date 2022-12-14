#!/usr/bin/env cwl-runner

class: CommandLineTool
cwlVersion: v1.0

inputs:
  file1: File

outputs:
  output:
    type: File
    outputBinding: { glob: output }

baseCommand: [cat]

stdin: $(inputs.file1.path)
stdout: output
stderr: $(inputs.file1.size)
