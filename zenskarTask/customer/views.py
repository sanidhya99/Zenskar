from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics
import json
from customer.tasks.producer import publish_to_queue

#create API for inward sync
class CustomerCreateView(generics.ListCreateAPIView):
    serializer_class = customerSerializer
    queryset = Customer.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data.get('data', {}).get('object', {})  # Access nested "data" and "object" keys

        if not data:
            return Response({"error": "Invalid JSON data format. Required keys are missing."}, status=400)

        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return Response({"error": "Both 'name' and 'email' are required fields."}, status=400)

        data_to_serialize = {'name': name, 'email': email}
        serializer = self.get_serializer(data=data_to_serialize)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"error": serializer.errors}, status=400)

#create API for outward sync
class CustomerOutCreateView(generics.CreateAPIView):
    serializer_class = customerSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        name=request.data.get('name')
        # Check if a customer with the same email already exists
        existing_customer = Customer.objects.filter(email=email).first()

        if existing_customer:
            # Update the existing customer
            serializer = self.get_serializer(existing_customer, data=request.data)
        else:
            # Create a new customer
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        pbd={
   "next_invoice_sequence":"1",
   "email":email,
   "name":name
}
        # Pass the data to the publish_to_queue function
        publish_to_queue(pbd)

        return Response({"message":"Customer successfully created"},status=201)

        
class CustomerEditView(generics.CreateAPIView):
    serializer_class = customerSerializer
    queryset = Customer.objects.all()
    
    def post(self, request, *args, **kwargs):
        # Get the email from the JSON request data
        email = request.data.get('data', {}).get('object', {}).get('email')
        
        if email:
            try:
                # Try to get the customer with the provided email
                customer = Customer.objects.get(email=email)
                
                # Delete the customer
                customer.delete()
                
                return Response({'message': f'Customer with email {email} has been deleted.'})
            except Customer.DoesNotExist:
                return Response({'message': f'Customer with email {email} does not exist.'})
        else:
            return Response({'error': 'Email not found in the request data.'}, status=400)
        
    
# # views.py

# from django.shortcuts import render
# from rest_framework.response import Response
# from .serializers import *
# from rest_framework import generics
# from django.http import JsonResponse
# import pika  # Import the RabbitMQ library or use your queuing system of choice

# class CustomerCreateView(generics.ListCreateAPIView):
#     serializer_class = customerSerializer
#     queryset = Customer.objects.all()

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         customer = serializer.instance

#         # Send an event to the queue for outward sync
#         send_customer_update_to_queue(customer.id)

#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=201, headers=headers)

# class CustomerEditView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = customerSerializer
#     queryset = Customer.objects.all()
#     lookup_field = 'id'

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         data = request.data

#         # Handle regular updates to the customer
#         serializer = self.get_serializer(instance, data=data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         # Send an event to the queue for outward sync
#         send_customer_update_to_queue(instance.id)

#         return Response(serializer.data)

# def send_customer_update_to_queue(customer_id):
#     # Code to send the customer update event to the queue (RabbitMQ or your queuing system)
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
#     channel = connection.channel()
#     channel.queue_declare(queue='customer_updates')
#     channel.basic_publish(exchange='', routing_key='customer_updates', body=str(customer_id))
#     connection.close()


