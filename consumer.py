import pika
from enviroments import env


class Consumer:

    def __init__(self):
        self.bootstrap_servers = env.bootstrap_servers
        self.connection = None
        self.channel = None
        self.__connect_rabbitmq_server()


    def callback(self, ch, method, properties, body):
        print("Mensagem recebida: %r" % body)

    def __connect_rabbitmq_server(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.bootstrap_servers))
        self.channel = self.connection.channel()

    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name)

    def register_callback_function(self, queue_name):
        self.channel.basic_consume(queue=queue_name, on_message_callback=self.callback, auto_ack=True)

    def starts_consuming_messages(self):
        self.channel.start_consuming()
