produto=float(input('digite o preço do produto!R$'))
novo= produto - (produto * 10 / 100)
print('o preço atual é R${:2f}, \ncom pagamento a vista ganha 10% de desconto que é R${:.2f}'.format(produto, novo))
novo2= produto + (produto * 10 / 100)
print('parcelado em 10 x, terá um aumento de 10% que sairá no valor de R${:.2f}'.format(novo2))