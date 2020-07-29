from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ObjectDoesNotExist
from tenant_schemas.middleware import BaseTenantMiddleware
from tenant_schemas.utils import get_public_schema_name


class RequestIDTenantMiddleware(BaseTenantMiddleware):

    def get_tenant(self, model, hostname, request):
        try:
            public_schema = model.objects.get(schema_name=get_public_schema_name())
        except ObjectDoesNotExist:
            public_schema = model.objects.create(
                domain_url=hostname,
                schema_name=get_public_schema_name(),
                tenant_name=get_public_schema_name().capitalize(),
                paid_until=date.today() + relativedelta(months=+1),
                on_trial=True)
        public_schema.save()
        x_request_id = request.META.get('HTTP_X_REQUEST_ID', public_schema.tenant_uuid)
        tenant_model = model.objects.get(tenant_uuid=x_request_id)
        print(tenant_model, public_schema)
        return tenant_model if not None else public_schema
