from rest_framework.serializers import Serializer, FileField, CharField

class UploadExcelSerializer(Serializer):
    excel_file = FileField()
    columns = CharField()
    class Meta:
        fields = ['excel_file', 'columns']