import qrcode

chave_PIX = input('Digite a chave do PIX: ')
descricaoTransacao = input('Informe a descriçao da transaçao: ')
valor_PIX = int(input('Informe o valor inteiro da transaçao do PIX'))

pix_data = {
    "chave": chave_PIX,
    "descricao": descricaoTransacao,
    "valor": valor_PIX,
}

#pix_format = f"t={pix_data['chave']}&desc={pix_data['descricao']}&v={pix_data['valor']}&s=200"
pix_format = f"00020101021226370014BR.GOV.BCB.PIX{pix_data['chave']}52040000530398654041{pix_data['valor']}5802BR5915{pix_data['descricao']}6009BRASIL.G0112https://www.bcb.gov.br/pix/dadosqr"


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(pix_format)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QRCode_PIX.png")