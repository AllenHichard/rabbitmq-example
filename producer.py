import pika
from enviroments import env


class Producer:

    def __init__(self):
        self.bootstrap_servers = env.bootstrap_servers
        self.connection = None
        self.channel = None

    def callback(self, method, properties, body):
        print("Mensagem recebida: %r" % body)

    def connect_rabbitmq_server(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.bootstrap_servers))
        self.channel = self.connection.channel()

    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name)

    def send_message_queue(self, queue_name, msg):
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=msg)

    def close_connection(self):
        self.connection.close()
