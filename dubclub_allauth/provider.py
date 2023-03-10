from allauth.account.models import EmailAddress
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class DubClubProvider(OAuth2Provider):
    id = "dubclub"
    name = "DubClub"
    account_class = ProviderAccount

    def get_default_scope(self):
        return ["openid"]

    def extract_uid(self, data):
        return str(data["sub"])

    def extract_common_fields(self, data):
        return dict(
            email=data.get("email"),
            last_name=data.get("family_name"),
            first_name=data.get("given_name"),
            username=data.get("preferred_username"),
        )

    def extract_email_addresses(self, data):
        return [EmailAddress(email=data.get("email"), verified=True, primary=True)]


provider_classes = [DubClubProvider]
