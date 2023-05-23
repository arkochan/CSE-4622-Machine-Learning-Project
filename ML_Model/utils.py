def toOutput(filename):
    dot_index = filename.rfind('.')
    if dot_index != -1:
        filename = filename[:dot_index] + '(output)' + filename[dot_index:]
    return filename
