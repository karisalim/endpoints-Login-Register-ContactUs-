from django.shortcuts import render
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactUsSerializer

from rest_framework.permissions import AllowAny
# Create your views here.



class ContactUsView(APIView):
    permission_classes = [AllowAny]  # السماح للجميع بالوصول إلى هذه الوظيفة

    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            # استخراج البيانات
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']

            # إرسال البريد الإلكتروني
            send_mail(
                subject=f"New Contact Form Submission: {subject}",
                message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
                from_email=email,
                recipient_list=['ks0894976@gmail.com'],  # البريد الإلكتروني الذي ستصل إليه الرسائل
            )

            # إرجاع رسالة نجاح
            return Response({"message": "Your message has been sent successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)