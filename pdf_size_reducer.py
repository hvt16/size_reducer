import os
from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet

def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def compress_file(input_file: str, output_file: str):
    if not output_file:
        output_file = input_file
    initial_size = os.path.getsize(input_file)
    try:
        PDFNet.Initialize()
        doc = PDFDoc(input_file)
        doc.InitSecurityHandler()
        Optimizer.Optimize(doc)
        doc.Save(output_file, SDFDoc.e_linearized)
        doc.Close()
    except Exception as e:
        print("Error compress_file=", e)
        doc.Close()
        return False
    compressed_size = os.path.getsize(output_file)
    ratio = 1 - (compressed_size / initial_size)
    return True

if __name__ == "__main__":
    input_file = "pt_msc.pdf"
    output_file = "pt_msc.pdf"
    compress_file(input_file, output_file)