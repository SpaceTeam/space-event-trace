from PIL import Image
import base45
import zlib
import flynn
import json
from pyzbar.pyzbar import decode
from datetime import date, datetime, time, timedelta, timezone
from cose.messages import CoseMessage
from cryptography import x509
from cose.keys import EC2Key
from werkzeug.datastructures import FileStorage
from pdf2image import convert_from_bytes


def extract_data(file: FileStorage) -> str:
    # if the file is a pdf convert it to an image
    if file.filename.rsplit(".", 1)[1].lower() == "pdf":
        img = convert_from_bytes(file.read())[0]
    else:
        img = Image.open(file)

    # decode the qr code
    result = decode(img)
    if result == []:
        raise Exception("No QR Code was detected in the image")

    # decode base45
    data_zlib = base45.b45decode(result[0].data[4:])

    # decompress zlib
    cose_data = zlib.decompress(data_zlib)

    # TODO: I think cbor2 is a more modern library than flynn
    # decode cose
    cbor_data = flynn.decoder.loads(cose_data)[1][2]

    # decode cbor
    data = flynn.decoder.loads(cbor_data)
    return data


with open("COVID-19-Testzertifikat-Hoeller-20211210.pdf", "rb") as file:
    print(json.dumps(extract_data(FileStorage(file))))
