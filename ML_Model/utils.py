def toOutput(filename , outputType):
    dot_index = filename.rfind('.')
    if dot_index != -1:
        filename = filename[:dot_index] + '('+outputType+')' + filename[dot_index:]
    return filename
