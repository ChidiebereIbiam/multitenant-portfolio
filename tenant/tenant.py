from tenant.models import Client, Domain

# create your public tenant
tenant = Client(schema_name='public',
                name='Chidiebere',
                address="Nnwqi",
                paid_until='2024-12-05',
                on_trial=False)
tenant.save()

# Add one or more domains for the tenant
domain = Domain()
domain.domain = 'localhost' # don't add your port or www here! on a local server you'll want to use localhost here
domain.tenant = tenant
domain.is_primary = True
domain.save()