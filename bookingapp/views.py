from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from django.utils import timezone
from sambandhanewapp.serializers import UserAccountSerializer







@api_view(['POST'])
def postBookings(request):
    datas = request.data
    patientID = datas['patientID']
    patient = UserAccount.objects.get(userID = patientID)
    datas["patientID"] = patient.id
    booking_serializer = BookingSerializer(data = datas)
    if booking_serializer.is_valid():
        booking = Booking.objects.create(
            patientID_id = datas["patientID"],
            uuID = datas['uuID'],
            bookingDate = datas['bookingDate'],
            bookingTime = datas['bookingTime'],
            doctorID = datas['doctorID'],
            payment = datas['payment'],
            status = datas['status'],
            createdAt = timezone.now(),
            updatedAt = timezone.now()
        )
        return Response({"success": True, "data": booking_serializer.data})
    else:
        return Response({"success": False})



@api_view(['POST'])
def getMyBookings(request):
    data = request.data
    userID = data["patientID"]
    if userID:
        try:
            user_account = UserAccount.objects.get(userID = userID)
            myBookings = Booking.objects.filter(patientID=user_account.id).order_by("-id")
            booking_serializer = BookingSerializer(myBookings, many=True)
            datas = booking_serializer.data
            for f in datas:
                f["userName"] = user_account.userName
            return Response({ "success":True, "data": datas})
        except Exception as e:
            return Response({ "success":False})
    else:
        return Response({"success":False})




@api_view(['POST'])
def updateBookings(request):
    data = request.data
    bookingID = data["id"]
    if bookingID:
        try:
            booking = Booking.objects.get(id = bookingID)
            booking.payment = data["payment"]
            booking.status = data["status"]
            booking.updatedAt = timezone.now()
            booking.save()
            data = BookingSerializer(booking).data
            return Response({"success": True, "data": data})
        except Exception as e:
            return Response({"success": False})
    else:
        return Response({"success": False})






@api_view(['POST'])
def getDoctorBookings(request):
    data = request.data
    doctorID = data["doctorID"]
    bookings = Booking.objects.filter(doctorID = doctorID).order_by("-id")
    bookingSerializer = BookingSerializer(bookings, many=True)
    datas = bookingSerializer.data
    for f in datas:
        f["userInfo"] = UserAccountSerializer(UserAccount.objects.get(id=f["patientID"]), many=False).data if bookings else None
    return Response({"success": True, "Bookinginfo": datas})
    
    


