from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def pagar(self, pedido):
        pass

class Notificador(ABC):
    @abstractmethod
    def notificar(self, pedido):
        pass

class PagamentoCartaoCredito(MetodoPagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} com cartão de crédito...")

class PagamentoBoleto(MetodoPagamento):
    def pagar(self, pedido):
        print(f"Gerando boleto no valor de R$ {pedido['valor']:.2f}...")

class PagamentoPix(MetodoPagamento):
    def pagar(self, pedido):
        print(f"Realizando pagamento via PIX no valor de R$ {pedido['valor']:.2f}...")

class NotificadorEmail(Notificador):
    def notificar(self, pedido):
        print(f"Enviando e-mail de confirmação para {pedido['cliente_email']}...")

class NotificadorSMS(Notificador):
    def notificar(self, pedido):
        print(f"Enviando SMS de confirmação para o número {pedido.get('cliente_telefone', 'N/A')}...")

class ProcessadorDePedidos:
    def __init__(self, metodo_pagamento: MetodoPagamento, notificador: Notificador):
        self.metodo_pagamento = metodo_pagamento
        self.notificador = notificador

    def processar(self, pedido):
        print(f"Processando o pedido #{pedido['id']} no valor de R$ {pedido['valor']:.2f}...")
        self.metodo_pagamento.pagar(pedido)
        self.notificador.notificar(pedido)
        pedido['status'] = 'concluido'
        print("Pedido concluído!")

if __name__ == "__main__":
    pedido1 = {
        'id': 123,
        'valor': 150.75,
        'cliente_email': 'cliente@exemplo.com',
        'status': 'pendente'
    }

    pedido2 = {
        'id': 456,
        'valor': 300.50,
        'cliente_email': 'outro@exemplo.com',
        'cliente_telefone': '(11) 99999-8888',
        'status': 'pendente'
    }

    processador1 = ProcessadorDePedidos(PagamentoCartaoCredito(), NotificadorEmail())
    processador1.processar(pedido1)

    print("-" * 40)

    processador2 = ProcessadorDePedidos(PagamentoPix(), NotificadorSMS())
    processador2.processar(pedido2)
