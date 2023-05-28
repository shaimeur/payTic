import pandas as pd
from io import StringIO
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ETLAPI.models import Transaction
from ETLAPI.database import db_session

@csrf_exempt
def import_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('file')
        if csv_file is None:
            return HttpResponse("No CSV file provided.")

        csv_data = csv_file.read().decode('utf-8')
        csv_df = pd.read_csv(StringIO(csv_data))

        for _, row in csv_df.iterrows():
            transaction = Transaction(
                transaction_id=row['Transaction ID'],
                transaction_date=row['Transaction Date'],
                amount=row['Amount'],
                merchant_name=row['Merchant Name']
            )
            db_session.add(transaction)

        db_session.commit()

        return HttpResponse("CSV data imported successfully!")

    return HttpResponse("Invalid request method.")
