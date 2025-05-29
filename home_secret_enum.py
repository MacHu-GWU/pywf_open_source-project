
try:
    from home_secret import hs
except ImportError:  # pragma: no cover
    pass


class Secret:
    # fmt: off

    codecov_io__accounts__sh__account_id = hs.t("providers.codecov_io.accounts.sh.account_id")
    codecov_io__accounts__sh__admin_email = hs.t("providers.codecov_io.accounts.sh.admin_email")
    codecov_io__accounts__sh__users__sh__user_id = hs.t("providers.codecov_io.accounts.sh.users.sh.user_id")
    codecov_io__accounts__sh__users__sh__email = hs.t("providers.codecov_io.accounts.sh.users.sh.email")
    codecov_io__accounts__sh__users__sh__secrets__dev__value = hs.t("providers.codecov_io.accounts.sh.users.sh.secrets.dev.value")
    github__accounts__sh__account_id = hs.t("providers.github.accounts.sh.account_id")
    github__accounts__sh__admin_email = hs.t("providers.github.accounts.sh.admin_email")
    github__accounts__sh__users__sh__user_id = hs.t("providers.github.accounts.sh.users.sh.user_id")
    github__accounts__sh__users__sh__email = hs.t("providers.github.accounts.sh.users.sh.email")
    github__accounts__sh__users__sh__secrets__full_repo_access__name = hs.t("providers.github.accounts.sh.users.sh.secrets.full_repo_access.name")
    github__accounts__sh__users__sh__secrets__full_repo_access__value = hs.t("providers.github.accounts.sh.users.sh.secrets.full_repo_access.value")
    github__accounts__sh__users__sh__secrets__full_repo_access__type = hs.t("providers.github.accounts.sh.users.sh.secrets.full_repo_access.type")
    readthedocs__accounts__sh__admin_email = hs.t("providers.readthedocs.accounts.sh.admin_email")
    readthedocs__accounts__sh__users__sh__email = hs.t("providers.readthedocs.accounts.sh.users.sh.email")
    readthedocs__accounts__sh__users__sh__secrets__dev__value = hs.t("providers.readthedocs.accounts.sh.users.sh.secrets.dev.value")

    # fmt: on


def _validate_secret():
    print("Validate secret:")
    for key, token in Secret.__dict__.items():
        if key.startswith("_") is False:
            print(f"{key} = {token.v}")


if __name__ == "__main__":
    _validate_secret()
