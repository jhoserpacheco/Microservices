from distutils.log import Log
from django.db.models import Q
from tokenize import group
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
import jwt, qrcode, time, base64, os, json, datetime, uuid
from datetime import timezone
from PIL import Image
from .serializers import RequestSerializer, ConfirmSerializer, LogSerializer
from ..models import Request, Log

class ObtainQRViewBase():
    def search_request(self, serializer):
        try:
            return Request.objects.get(user_id=self.request.user.id)
        except Request.DoesNotExist:
            return None

    def get_qr(self, instance):
        img = qrcode.make({
            'user_id': instance.id,
            'key': instance.key,
        }) # qrcode.image.pil.PilImage

        img.save("static/qr_codes/some_file.png")

        image_base_64 = self.convert_to_base64("static/qr_codes/some_file.png")

        os.remove("static/qr_codes/some_file.png")

        return image_base_64

    def convert_to_base64(self, img):
        with open(img, "rb") as img_file:
            my_string = base64.b64encode(img_file.read())
        return my_string


class ObtainQRView(APIView, ObtainQRViewBase):
    def post(self, request):
        request_serializer = RequestSerializer(data=request.data)
        if request_serializer.is_valid():
            request_user = self.search_request(request_serializer)

            if not request_user:
                instance = request_serializer.save(
                    user_id=self.request.user.id,
                    time=time.time(),
                    key=uuid.uuid4().hex
                )
            else:
                request_user.time = datetime.datetime.now(timezone.utc)
                request_user.key = uuid.uuid4().hex
                request_user.is_used = False
                request_user.save()
                instance = request_user

            return Response({'qrcode': self.get_qr(instance)})

        return Response(request_serializer.errors, status=400)

class ConfirmQREntranceView(APIView):
    def post(self, request):
        confirm_serializer = ConfirmSerializer(data=request.data)
        if confirm_serializer.is_valid():
            try:
                request_user = Request.objects.filter(
                    user_id=confirm_serializer.validated_data['user_id'],
                    key=confirm_serializer.validated_data['key']
                ).first()
                
                if not request_user:
                    raise Request.DoesNotExist

                time_now = datetime.datetime.now(timezone.utc)
                if (time_now - request_user.time).total_seconds() > 180:
                    return Response({'error': 'Request is too old'})

                if request_user.log_id:
                    log = Log.objects.get(id=request_user.log_id.id)
                    log.entrance_time = time_now
                    log.save()
                    print('update')
                else:
                    log = Log()
                    log.user_id = request_user.user_id
                    log.group_id = request_user.group_id
                    log.entrance_time = time_now
                    log.save()
                    request_user.log_id = log
                request_user.is_used = True
                request_user.save()
            except Request.DoesNotExist:
                return Response({'error': 'Request does not exist'})
        else:
            return Response(confirm_serializer.errors, status=400)
        return Response(status=200)

class ConfirmQRExitView(APIView):
    def post(self, request):
        confirm_serializer = ConfirmSerializer(data=request.data)
        if confirm_serializer.is_valid():
            try:
                request_user = Request.objects.filter(
                    user_id=confirm_serializer.validated_data['user_id'],
                    key=confirm_serializer.validated_data['key'],
                    is_used=False
                ).first()
                
                if not request_user:
                    raise Request.DoesNotExist

                time_now = datetime.datetime.now(timezone.utc)
                if (time_now - request_user.time).total_seconds() > 180:
                    return Response({'error': 'Request is too old'})

                log = Log.objects.filter(id=request_user.log_id.id).first()
                log.exit_time = time_now
                log.save()

                request_user.delete()
            except Request.DoesNotExist:
                return Response({'error': 'Request does not exist'})
        else:
            return Response(confirm_serializer.errors, status=400)
        return Response(status=200)

class EntranceUserLogs(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        print('token', self.request.user.custom_groups[0].id)
        log = Log.objects.get(Q(user_id=user_id))
        serializer = LogSerializer(log)
        return Response(serializer.data)

class EntranceGroupLogs(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, group_id):
        print('token', self.request.user.custom_groups[0].id)
        log = Log.objects.get(Q(group_id=group_id))
        serializer = LogSerializer(log)
        return Response(serializer.data)
