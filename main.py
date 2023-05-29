from producer import Producer
from consumer import Consumer

producer = Producer()
consumer = Consumer()

producer.declare_queue("chat")
producer.send_message_queue(queue_name="chat", msg='sync')
consumer.declare_queue("chat")
consumer.register_callback_function(queue_name='chat')
consumer.starts_consuming_messages()
