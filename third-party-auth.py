from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "common-env-features",
        '"ENABLE_THIRD_PARTY_AUTH": True, "ENABLE_COMBINED_LOGIN_REGISTRATION": True'
    )
)

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-auth",
        '"SOCIAL_AUTH_OAUTH_SECRETS": {"google-oauth2": "", "linkedin-oauth2": "", "facebook": "", "azuread-oauth2": ""}'
    )
)

hooks.Filters.ENV_PATCHES.add_item(
    (
        "lms-env",
        '"THIRD_PARTY_AUTH_BACKENDS": ["social_core.backends.google.GoogleOAuth2", "social_core.backends.linkedin.LinkedinOAuth2", "social_core.backends.facebook.FacebookOAuth2", "social_core.backends.azuread.AzureADOAuth2"]'
    )
)