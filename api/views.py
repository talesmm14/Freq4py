from os import system
from django.shortcuts import render
from django.http import Http404, StreamingHttpResponse
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Sheet
from api.serializers import Sheet_Serializer

import io, sys, docx, datetime, locale, os
from calendar import monthrange
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
# Create your views here.


class Sheet_View(APIView):
    def get(self, request, format=None):
        snippets = Sheet.objects.all()
        serializer = Sheet_Serializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Sheet_Serializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Sheet_Detail_View(APIView):
    def get_object(self, pk):
        try:
            sheet = Sheet.objects.get(pk=pk)
            return sheet
        except Sheet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippets = self.get_object(pk)
        serializer = Sheet_Serializer(snippets, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippets = self.get_object(pk)
        serializer = Sheet_Serializer(snippets, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippets = self.get_object(pk)
        serializer = Sheet_Serializer(snippets, many=True)

        if serializer.is_valid():
            serializer.delete()
            return Response(status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ExportDocx(APIView):
    def get_object(self, pk):
        try:
            sheet = Sheet.objects.get(pk=pk)
            return sheet
        except Sheet.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        sheet = self.get_object(pk)
        # create an empty document object
        # print(settings.STATIC_ROOT + sheet.path, file=sys.stderr)
        
        path = settings.STATIC_ROOT + sheet.path
        document = docx.Document(path)

        # replace(document, sheet)

        # save document info
        buffer = io.BytesIO()
        document.save(buffer)  # save your memory stream
        buffer.seek(0)  # rewind the stream

        # put them to streaming content response
        # within docx content_type
        response = StreamingHttpResponse(
            streaming_content=buffer,  # use the stream's content
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )

        response['Content-Disposition'] = 'attachment;filename=Test.docx'
        response["Content-Encoding"] = 'UTF-8'

        return response


def replace(doc, sheet):
    year = sheet.date.year
    month = sheet.date.month
    month_days = monthrange(year, month)[1]
    key_table = {}
    key_words = {}

    day = 0
    weekday = 0
    for variable_key, variable_value in key_words.items():
        for paragraph in doc.paragraphs:
            replace_text_in_paragraph(paragraph, variable_key, variable_value)

        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    if cell.text == "HM1":
                        day += 1
                        if day <= month_days:
                            weekday = date(
                                year=year, month=month, day=day).weekday()

                    for key, value in key_table.items():
                        value = not_working_days(day, weekday, key, value)
                        replace_text_in_paragraph(paragraph, key, value)

                    for paragraph in cell.paragraphs:
                        replace_text_in_paragraph(paragraph, variable_key, variable_value)

def not_working_days(weekday, day, key, value, not_working_days):
    if weekday == 5 or weekday == 6:
        if key[0] != 'H':
            if weekday == 5:
                value = "SÁBADO"
            if weekday == 6:
                value = "DOMINGO"
        else:
            value = "****"
    elif self.not_working_days != None:
        if key[0] != 'H':
            for not_working_day, not_working_day_value in not_working_days.items():
                if day == not_working_day:
                    value = not_working_day_value
    return value

def replace_text_in_paragraph(paragraph, key, value):
    if key in paragraph.text:
        inline = paragraph.runs
        for item in inline:
            if key in item.text:
                item.text = item.text.replace(key, value)

