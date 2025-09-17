from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_id_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False),
        ),
    ]